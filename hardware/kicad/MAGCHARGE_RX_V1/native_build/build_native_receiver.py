from pathlib import Path
import re
import shutil
import uuid

ROOT = Path("hardware/kicad/MAGCHARGE_RX_V1")
SRC = ROOT / "MAGCHARGE_RX_V1.kicad_sch"
OUT = ROOT / "MAGCHARGE_RX_V1_NATIVE.kicad_sch"

print("=== MAGCHARGE RX V1 NATIVE BUILD ===")

src = SRC.read_text()

# ------------------------------------------------------------
# Preserve the original and create a working copy.
# ------------------------------------------------------------
backup = ROOT / "native_build" / "MAGCHARGE_RX_V1_SOURCE_FOR_NATIVE_BUILD.kicad_sch"
shutil.copy2(SRC, backup)

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
def uid():
    return str(uuid.uuid4())

def remove_instances(text):
    """
    Remove top-level legacy symbol instances while retaining
    the embedded lib_symbols section.

    This deliberately works only on (symbol ... ) blocks that
    contain a top-level (lib_id "...") field.
    """
    result = []
    i = 0
    n = len(text)

    while i < n:
        p = text.find("\n\t(symbol\n", i)
        if p < 0:
            result.append(text[i:])
            break

        result.append(text[i:p])

        depth = 0
        j = p + 1
        started = False

        while j < n:
            if text[j] == "(":
                depth += 1
                started = True
            elif text[j] == ")":
                depth -= 1
                if started and depth == 0:
                    j += 1
                    break
            j += 1

        block = text[p:j]

        if "(lib_id " in block:
            # Drop instance.
            pass
        else:
            result.append(block)

        i = j

    return "".join(result)

# ------------------------------------------------------------
# Remove old placed component instances and old wiring.
# Embedded libraries remain available.
# ------------------------------------------------------------
work = remove_instances(src)

# Remove placed wire/junction/label/text blocks from the old design.
# We intentionally preserve lib_symbols and project metadata.
patterns = [
    r'\n\t\(wire\b.*?\n\t\)',
    r'\n\t\(junction\b.*?\n\t\)',
    r'\n\t\(label\b.*?\n\t\)',
    r'\n\t\(global_label\b.*?\n\t\)',
    r'\n\t\(hierarchical_label\b.*?\n\t\)',
]

for pat in patterns:
    work = re.sub(pat, "", work, flags=re.S)

# ------------------------------------------------------------
# Find the main schematic closing point.
# We insert our native design before the final schematic close.
# ------------------------------------------------------------
last = work.rfind(")")
if last < 0:
    raise SystemExit("ERROR: schematic closing parenthesis not found")

# ------------------------------------------------------------
# Native receiver design.
#
# Coordinates are intentionally clean and separated.
# BQ51013C:
#   U1
#
# The component declarations below are kept simple and
# self-documenting. Values that require characterization
# remain TBD.
# ------------------------------------------------------------

design = r'''

	(text "MAGCHARGE RX V1 - NATIVE WIRELESS POWER RECEIVER"
		(exclude_from_sim no)
		(at 80 45 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 2 2)
				(thickness 0.3)
			)
		)
	)

	(text "BQ51013C + 14.3uH RECEIVER / 5V USB-C OUTPUT"
		(exclude_from_sim no)
		(at 80 49 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1.2 1.2)
				(thickness 0.2)
			)
		)
	)

	(text_box "DESIGN STATUS: NATIVE BUILD / VALUES MARKED TBD REQUIRE CHARACTERIZATION"
		(exclude_from_sim no)
		(locked no)
		(at 80 52 200 6)
		(layer "Dwgs.User")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1 1)
			)
			(stroke
				(width 0.3)
				(type default)
			)
			(fill
				(type none)
			)
			(align
				(horizontal left)
				(vertical center)
			)
		)
	)

	(text "WIRELESS INPUT"
		(exclude_from_sim no)
		(at 90 70 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1.2 1.2)
			)
		)
	)

	(text "RECTIFIER / FILTER"
		(exclude_from_sim no)
		(at 150 70 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1.2 1.2)
			)
		)
	)

	(text "5V OUTPUT"
		(exclude_from_sim no)
		(at 230 70 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1.2 1.2)
			)
		)
	)

	(text "FOD / ILIM / THERMAL"
		(exclude_from_sim no)
		(at 150 180 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1.2 1.2)
			)
		)
	)

	(text "USB-C SOURCE OUTPUT - NO USB PD"
		(exclude_from_sim no)
		(at 225 180 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1.1 1.1)
			)
		)
	)

	(text "C_RX1 = TBD AFTER COIL CHARACTERIZATION"
		(exclude_from_sim no)
		(at 80 205 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1 1)
			)
		)
	)

	(text "C_RX2 = TBD AFTER COIL CHARACTERIZATION"
		(exclude_from_sim no)
		(at 80 209 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1 1)
			)
		)
	)

	(text "NTC1 = PRODUCTION VALUE TBD"
		(exclude_from_sim no)
		(at 80 213 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1 1)
			)
		)
	)

	(text "ESD1 / FUSE1 = FINAL PROTECTION SELECTION TBD"
		(exclude_from_sim no)
		(at 80 217 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1 1)
			)
		)
	)

	(text "SH1 / MR1 = MECHANICAL / MAGNETIC ALIGNMENT"
		(exclude_from_sim no)
		(at 80 221 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1 1)
			)
		)
	)

	(text "CONTROL NOTES: AD=PGND, AD-EN=NC, EN1/EN2=LOW/FLOATING"
		(exclude_from_sim no)
		(at 80 225 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1 1)
			)
		)
	)

	(text "EXPOSED PAD = PGND / THERMAL CONNECTION"
		(exclude_from_sim no)
		(at 80 229 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1 1)
			)
		)
	)

'''

# ------------------------------------------------------------
# Add descriptive native design manifest as schematic text.
# This makes the generated schematic self-documenting even
# before final graphical placement is completed in KiCad.
# ------------------------------------------------------------

manifest = [
    ("U1", "BQ51013CRHLR", "IC", "1:PGND;2:AC1;3:BOOT1;4:+5V_RX;5:CLAMP1;6:COMM1;7:CHG_STATUS;8:NC;9:PGND;10:EN1;11:EN2;12:ILIM;13:TS_CTRL;14:FOD;15:COMM2;16:CLAMP2;17:BOOT2;18:RECT;19:AC2;20:PGND;EP:PGND"),
    ("L1", "760308103215", "COIL", "AC1;AC2"),
    ("C_RX1", "TBD", "CAPACITOR", "AC1/AC2 SERIES RESONANT"),
    ("C_RX2", "TBD", "CAPACITOR", "AC1/AC2 PARALLEL RESONANT"),
    ("C_BOOT1", "10nF", "CAPACITOR", "BOOT1-AC1"),
    ("C_BOOT2", "10nF", "CAPACITOR", "BOOT2-AC2"),
    ("C_COMM1", "22nF", "CAPACITOR", "COMM1-AC1"),
    ("C_COMM2", "22nF", "CAPACITOR", "COMM2-AC2"),
    ("C_CLAMP1", "0.47uF", "CAPACITOR", "CLAMP1-AC1"),
    ("C_CLAMP2", "0.47uF", "CAPACITOR", "CLAMP2-AC2"),
    ("C_RECT1", "10uF", "CAPACITOR", "RECT-PGND"),
    ("C_RECT2", "10uF", "CAPACITOR", "RECT-PGND"),
    ("C_RECT3", "0.1uF", "CAPACITOR", "RECT-PGND"),
    ("C_OUT1", "10uF", "CAPACITOR", "+5V_RX-PGND"),
    ("C_OUT2", "0.1uF", "CAPACITOR", "+5V_RX-PGND"),
    ("R_OS", "20k", "RESISTOR", "RECT-FOD"),
    ("R1", "66R", "RESISTOR", "ILIM-FOD"),
    ("R_FOD", "196R", "RESISTOR", "FOD-PGND"),
    ("NTC1", "TBD", "NTC", "TS_CTRL-PGND"),
    ("J1", "USB-C", "CONNECTOR", "+5V_RX/PGND"),
    ("ESD1", "TBD", "ESD", "USB-C OUTPUT"),
    ("FUSE1", "TBD", "FUSE", "USB-C VBUS"),
    ("SH1", "TBD", "SHIELD", "MECHANICAL"),
    ("MR1", "TBD", "MAGNETIC RING", "MECHANICAL"),
]

y = 235
for ref, value, typ, conn in manifest:
    design += f'''
\t(text "{ref}  {value}  [{typ}]  {conn}"
\t\t(exclude_from_sim no)
\t\t(at 80 {y} 0)
\t\t(layer "text")
\t\t(uuid "{uid()}")
\t\t(effects
\t\t\t(font
\t\t\t\t(size 0.9 0.9)
\t\t\t)
\t\t)
\t)
'''
    y += 3.5

design += r'''
	(text "AUTHORITATIVE ARCHITECTURE"
		(exclude_from_sim no)
		(at 80 325 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1.3 1.3)
				(thickness 0.2)
			)
		)
	)

	(text "U1 OUT -> +5V_RX"
		(exclude_from_sim no)
		(at 80 329 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "U1 RECT -> RECT FILTER -> PGND"
		(exclude_from_sim no)
		(at 80 333 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "U1 AC1 / AC2 -> L1 + RESONANT NETWORK"
		(exclude_from_sim no)
		(at 80 337 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "U1 BOOT1 -> C_BOOT1 -> AC1"
		(exclude_from_sim no)
		(at 80 341 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "U1 BOOT2 -> C_BOOT2 -> AC2"
		(exclude_from_sim no)
		(at 80 345 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "U1 COMM1 -> C_COMM1 -> AC1"
		(exclude_from_sim no)
		(at 80 349 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "U1 COMM2 -> C_COMM2 -> AC2"
		(exclude_from_sim no)
		(at 80 353 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "U1 CLAMP1 -> C_CLAMP1 -> AC1"
		(exclude_from_sim no)
		(at 80 357 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "U1 CLAMP2 -> C_CLAMP2 -> AC2"
		(exclude_from_sim no)
		(at 80 361 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "ILIM -> 66R -> FOD; RECT -> 20k -> FOD; FOD -> 196R -> PGND"
		(exclude_from_sim no)
		(at 80 365 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "TS/CTRL -> NTC1 -> PGND"
		(exclude_from_sim no)
		(at 80 369 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "AD -> PGND; AD-EN -> NC; EN1/EN2 -> LOW/FLOATING"
		(exclude_from_sim no)
		(at 80 373 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "CHG -> OPEN-DRAIN STATUS / OPTIONAL LED"
		(exclude_from_sim no)
		(at 80 377 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "USB-C: 5V SOURCE / TARGET 1A / NO USB-PD"
		(exclude_from_sim no)
		(at 80 381 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects (font (size 1 1)))
	)

	(text "DO NOT FABRICATE UNTIL COIL RESONANCE + FOD + USB-C PROTECTION ARE VALIDATED"
		(exclude_from_sim no)
		(at 80 388 0)
		(layer "text")
		(uuid "''' + uid() + r'''")
		(effects
			(font
				(size 1.1 1.1)
				(thickness 0.2)
			)
		)
	)

'''

new_text = work[:last] + design + work[last:]
OUT.write_text(new_text)

print("Created:", OUT)
print("Backup:", backup)
print("Bytes:", OUT.stat().st_size)
