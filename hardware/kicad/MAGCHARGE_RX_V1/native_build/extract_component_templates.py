from pathlib import Path

p = Path("hardware/kicad/MAGCHARGE_RX_V1/native_build/MAGCHARGE_RX_V1_SOURCE_FOR_NATIVE_BUILD.kicad_sch")
s = p.read_text()

print("=== LEGACY EMBEDDED LIBRARY CHECK ===")

targets = [
    "interf_u:C",
    "interf_u:CP",
    "interf_u:R",
    "interf_u:Crystal",
    "interf_u:LED",
    "interf_u:GND",
    "interf_u:VCC",
    "interf_u:PWR_FLAG",
    "BQ51013CRHLR",
]

for target in targets:
    print(f"{target}: {s.count(target)}")

print()
print("=== SYMBOL DEFINITIONS CONTAINING TARGETS ===")

# Locate the lib_symbols section.
lib_start = s.find("(lib_symbols")
if lib_start < 0:
    print("ERROR: lib_symbols section not found")
    raise SystemExit(1)

# Extract balanced blocks beginning with (symbol "...").
def extract_symbol_blocks(text, start):
    result = []
    pos = start

    while True:
        idx = text.find("(symbol ", pos)
        if idx < 0:
            break

        depth = 0
        quote = False
        escape = False
        end = None

        for i in range(idx, len(text)):
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
                    end = i + 1
                    break

        if end is None:
            break

        result.append(text[idx:end])
        pos = end

    return result


blocks = extract_symbol_blocks(s, lib_start)

print("Embedded symbol definitions found:", len(blocks))
print()

for target in targets:
    found = []

    for b in blocks:
        if f'(symbol "{target}"' in b:
            found.append(b)

    print(f"{target}: {len(found)} definition(s)")

    for b in found:
        first = b.splitlines()[0].strip()
        print("   ", first)

print()
print("=== NEW SCHEMATIC LIBRARY DEFINITIONS ===")

newp = Path("hardware/kicad/MAGCHARGE_RX_V1/MAGCHARGE_RX_V1_CONNECTED.kicad_sch")
new = newp.read_text()

new_start = new.find("(lib_symbols")
new_blocks = extract_symbol_blocks(new, new_start) if new_start >= 0 else []

print("New schematic embedded symbol definitions:", len(new_blocks))

for b in new_blocks:
    first = b.splitlines()[0].strip()
    print(first)

print()
print("RESULT: COMPONENT TEMPLATE ANALYSIS COMPLETE")
