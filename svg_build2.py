import textwrap

INPUT_FILE = "frames.txt"      # your ASCII animation file
OUTPUT_FILE = "animation.svg"  # output SVG file

FRAME_WIDTH = 122
FRAME_HEIGHT = 91
DURATION = 6                   # seconds
X_POS = 470
Y_START = 0
LINE_HEIGHT = 15                # vertical spacing between tspans

# Scale to fit inside 600px height
SCALE_X = 0.7
SCALE_Y = 600 / (FRAME_HEIGHT * LINE_HEIGHT)  # ≈ 0.44


def load_frames():
    """
    Loads frames by treating ANY whitespace-only line as a separator.
    This works even when:
    - blank lines contain spaces
    - blank lines contain non-breaking spaces
    - frames have irregular line counts
    - asciigif inserts garbage or padding
    """

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = f.read().splitlines()

    frames = []
    current = []

    for line in raw:
        # Normalize whitespace: remove NBSP, tabs, CR, trailing spaces
        cleaned = (
            line.replace("\u00A0", "")  # NBSP
                .replace("\t", "")      # tabs
                .replace("\r", "")      # stray CR
                .strip()                # normal whitespace
        )

        # Blank line = frame boundary
        if cleaned == "":
            if len(current) > 0:
                frames.append(current)
                current = []
            continue

        # Normal ASCII line
        current.append(line)

    # Add last frame if needed
    if len(current) > 0:
        frames.append(current)

    return frames


def build_svg(frames):
    total_frames = len(frames)

    svg_header = textwrap.dedent(f"""
    <svg width="1400" height="600" xmlns="http://www.w3.org/2000/svg">
      <style>
        text {{
          font-family: monospace;
          font-size: 12px;
          fill: #c9d1d9;
          white-space: pre;
        }}
      </style>

      <g transform="scale({SCALE_X}, {SCALE_Y})">
    """)

    svg_footer = """
      </g>
    </svg>
    """

    body = []

    for i, frame in enumerate(frames):
        tspans = []
        for line_index, line in enumerate(frame):
            y = Y_START + line_index * LINE_HEIGHT
            tspans.append(f'<tspan x="{X_POS}" y="{y}">{line}</tspan>')

        values = ["none"] * total_frames
        values[i] = "inline"
        values_str = ";".join(values)

        group = f"""
        <g id="f{i}">
          <text>
            {''.join(tspans)}
          </text>
          <animate attributeName="display"
                   dur="{DURATION}s"
                   repeatCount="indefinite"
                   values="{values_str}"/>
        </g>
        """

        body.append(group)

    return svg_header + "\n".join(body) + svg_footer


def main():
    frames = load_frames()
    print(f"Loaded {len(frames)} frames.")

    svg = build_svg(frames)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"SVG written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
