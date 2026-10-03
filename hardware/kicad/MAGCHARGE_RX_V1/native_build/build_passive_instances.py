from pathlib import Path
import re
import uuid
import shutil

src = Path("hardware/kicad/MAGCHARGE_RX_V1/MAGCHARGE_RX_V1_CONNECTED.kicad_sch")
legacy = Path("hardware/kicad/MAGCHARGE_RX_V1/native_build/MAGCHARGE_RX_V1_SOURCE_FOR_NATIVE_BUILD.kicad_sch")
out = Path("hardware/kicad/MAGCHARGE_RX_V1/MAGCHARGE_RX_V1_COMPONENTS.kicad_sch")

s = src.read_text()
ls = legacy.read_text()

print("=== MAGCHARGE REAL COMPONENT INSTANCE BUILD ===")

def find_instance(text, ref):
    """
    Find the nearest enclosing top-level '(symbol ...)' block
    containing the exact Reference property.
    """
    marker = f'(property "Reference" "{ref}"'

    pos = text.find(marker)
    if pos < 0:
        return None

    # Search backwards for candidate symbol starts.
    start = text.rfind("(symbol", 0, pos)

    if start < 0:
        return None

    # Find matching closing parenthesis from that symbol start.
    depth = 0
    quote = False
    escape = False

    for i in range(start, len(text)):
        ch = text[i]

        if escape:
            escape = False
            continue

        if ch == "\\" and quote:
            escape = True
            continue

        if ch == '"':
            quote = not quote
            continue

        if quote:
            continue

        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1

            if depth == 0:
                block = text[start:i+1]

                # Make absolutely sure this is the requested reference.
                if marker in block:
                    return block

                return None

    return None


templates = {
    "C": find_instance(ls, "C2"),
    "CP": find_instance(ls, "C1"),
    "R": find_instance(ls, "R1"),
    "BQ": find_instance(ls, "U1"),
}

for name, block in templates.items():
    if block:
        print(f"Template {name}: FOUND ({len(block)} bytes)")
    else:
        print(f"Template {name}: MISSING")

if any(v is None for v in templates.values()):
    raise SystemExit("ERROR: Required templates could not be extracted")


def replace_first_property(block, prop, value):
    pattern = rf'(\(property\s+"{re.escape(prop)}"\s+")[^"]+(")'
    new, count = re.subn(
        pattern,
        lambda m: m.group(1) + value + m.group(2),
        block,
        count=1
    )

    if count != 1:
        raise RuntimeError(f"Could not replace {prop}")

    return new


def make_instance(template, ref, value, x, y, angle=0):
    b = template

    # Give every cloned placed symbol its own UUID.
    fresh_uuid = str(uuid.uuid4())

    # Insert UUID after the opening symbol line.
    opening = b.find("(symbol")
    if opening < 0:
        raise RuntimeError(f"Symbol opening not found for {ref}")

    opening_end = b.find("\n", opening)
    if opening_end < 0:
        raise RuntimeError(f"Symbol opening line not found for {ref}")

    b = (
        b[:opening_end + 1]
        + f"\t\t(uuid {fresh_uuid})\n"
        + b[opening_end + 1:]
    )

    # Replace reference and value.
    b = replace_first_property(b, "Reference", ref)
    b = replace_first_property(b, "Value", value)

    # Replace the first placement expression.
    # Legacy KiCad templates can use slightly different formatting,
    # so match the whole expression rather than a rigid coordinate pattern.
    placement_start = b.find("(at", opening)

    if placement_start < 0:
        raise RuntimeError(f"Placement expression not found for {ref}")

    placement_end = b.find(")", placement_start)

    if placement_end < 0:
        raise RuntimeError(f"Placement expression is incomplete for {ref}")

    new_placement = f"(at {x} {y} {angle})"

    b = (
        b[:placement_start]
        + new_placement
        + b[placement_end + 1:]
    )

    return b


components = [
    ("C_RX1",    "TBD",       145, 105, 90, "C"),
    ("C_RX2",    "TBD",       145, 135, 90, "C"),

    ("C_BOOT1",  "10nF",      165, 95, 90, "C"),
    ("C_BOOT2",  "10nF",      255, 95, 90, "C"),

    ("C_COMM1",  "22nF",      165, 110, 90, "C"),
    ("C_COMM2",  "22nF",      255, 110, 90, "C"),

    ("C_CLAMP1", "0.47uF",    165, 125, 90, "C"),
    ("C_CLAMP2", "0.47uF",    255, 125, 90, "C"),

    ("C_RECT1",  "10uF",      175, 155, 90, "CP"),
    ("C_RECT2",  "10uF",      190, 155, 90, "CP"),
    ("C_RECT3",  "0.1uF",     205, 155, 90, "C"),

    ("C_OUT1",   "10uF",      240, 155, 90, "CP"),
    ("C_OUT2",   "0.1uF",     255, 155, 90, "C"),

    ("R1",       "66R",       245, 80, 0,  "R"),
    ("R_OS",     "20k",       225, 165, 90, "R"),
    ("R_FOD",    "196R",      270, 165, 90, "R"),

    # Temporary generic resistor representation until a proper
    # thermistor symbol is embedded.
    ("NTC1",     "NTC TBD",   290, 140, 90, "R"),
]

instances = []

for ref, value, x, y, angle, template_name in components:
    instances.append(
        make_instance(
            templates[template_name],
            ref,
            value,
            x,
            y,
            angle
        )
    )

# Locate the root sheet_instances section regardless of indentation.
anchor = s.find("(sheet_instances")

if anchor < 0:
    raise SystemExit("ERROR: sheet_instances section not found")

new_text = s[:anchor] + "\n" + "\n\n".join(instances) + "\n" + s[anchor:]

backup = out.with_name(out.stem + ".PRE_COMPONENTS_BACKUP.kicad_sch")

if out.exists():
    shutil.copy2(out, backup)

out.write_text(new_text)

print()
print("Placed component instances:", len(instances))
print("Output:", out)

if backup.exists():
    print("Backup:", backup)

print()
print("=== PLACED COMPONENTS ===")

for ref, value, x, y, angle, template_name in components:
    print(f"{ref:12s} {value:12s}  ({x},{y},{angle})")

print()
print("=== STRUCTURAL VALIDATION ===")

text = out.read_text()

depth = 0
quote = False
escape = False
negative = False

for ch in text:
    if escape:
        escape = False
        continue

    if ch == "\\" and quote:
        escape = True
        continue

    if ch == '"':
        quote = not quote
        continue

    if quote:
        continue

    if ch == "(":
        depth += 1
    elif ch == ")":
        depth -= 1
        if depth < 0:
            negative = True

print("Parenthesis depth:", depth)
print("Quoted string open:", quote)
print("Negative depth:", negative)

required = [
    "BQ51013CRHLR",
    "C_RX1",
    "C_RX2",
    "C_BOOT1",
    "C_BOOT2",
    "C_COMM1",
    "C_COMM2",
    "C_CLAMP1",
    "C_CLAMP2",
    "C_RECT1",
    "C_RECT2",
    "C_RECT3",
    "C_OUT1",
    "C_OUT2",
    "R_OS",
    "R1",
    "R_FOD",
    "NTC1",
]

for item in required:
    print(f"{item:12s}", "PASS" if item in text else "MISSING")

if depth != 0 or quote or negative:
    raise SystemExit("RESULT: STRUCTURAL VALIDATION FAILED")

print()
print("RESULT: REAL COMPONENT INSTANCES CREATED")
