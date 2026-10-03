from pathlib import Path

p = Path("hardware/kicad/MAGCHARGE_RX_V1/native_build/MAGCHARGE_RX_V1_SOURCE_FOR_NATIVE_BUILD.kicad_sch")
s = p.read_text()

print("=== LEGACY SYMBOL INSTANCE INVENTORY ===")

def balanced_blocks(text, token="(symbol"):
    blocks = []
    pos = 0

    while True:
        start = text.find(token, pos)
        if start < 0:
            break

        depth = 0
        quote = False
        escape = False
        end = None

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
                    end = i + 1
                    break

        if end is None:
            break

        blocks.append(text[start:end])
        pos = end

    return blocks


blocks = balanced_blocks(s)

print("Total symbol-like blocks:", len(blocks))
print()

for i, b in enumerate(blocks, 1):
    # Only report actual placed instances, not the large embedded
    # library definitions that also contain "(symbol ...)".
    if '(property "Reference"' not in b:
        continue

    ref = "?"
    value = "?"
    lib_id = "?"
    x = "?"
    y = "?"
    angle = "0"

    lines = b.splitlines()

    for line in lines:
        t = line.strip()

        if t.startswith('(lib_id "'):
            lib_id = t.split('"', 2)[1]

        elif t.startswith('(property "Reference"'):
            parts = t.split('"')
            if len(parts) >= 4:
                ref = parts[3]

        elif t.startswith('(property "Value"'):
            parts = t.split('"')
            if len(parts) >= 4:
                value = parts[3]

        elif t.startswith("(at "):
            parts = t.strip("()").split()
            if len(parts) >= 3:
                x = parts[1]
                y = parts[2]
            if len(parts) >= 4:
                angle = parts[3]

    print(
        f"{i:03d}: "
        f"REF={ref:8s} "
        f"VALUE={value[:35]:35s} "
        f"LIB={lib_id[:45]:45s} "
        f"AT=({x},{y},{angle})"
    )

print()
print("=== TEMPLATE AVAILABILITY ===")

refs = set()

for b in blocks:
    if '(property "Reference"' not in b:
        continue

    marker = '(property "Reference" "'
    start = b.find(marker)

    if start >= 0:
        start += len(marker)
        end = b.find('"', start)
        if end >= 0:
            refs.add(b[start:end])

for ref in ["C1","C2","C3","C4","C5","C6",
            "R1","R2","R3","R4","R5","D1",
            "U1","X1"]:
    print(f"{ref}: {'FOUND' if ref in refs else 'NOT FOUND'}")

print()
print("RESULT: LEGACY INSTANCE INVENTORY COMPLETE")
