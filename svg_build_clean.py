import textwrap

INPUT_FILE = "frames_clean.txt"   # cleaned ASCII animation file
OUTPUT_FILE = "animation.svg"     # output SVG file

FRAME_WIDTH = 91
FRAME_HEIGHT = 91
FRAME_BLOCK = FRAME_HEIGHT + 1    # 91 lines + 1 blank line
DURATION = 15                     # seconds
X_POS = 470
Y_START = 0
LINE_HEIGHT = 15                 # vertical spacing between tspans

SCALE_Y = 600 / (FRAME_HEIGHT * LINE_HEIGHT)   # ≈ 0.44

# You can widen the animation by increasing SCALE_X
SCALE_X = 0.7   # adjust this to make it wider or narrower


def load_frames():
    """Load frames by fixed-size blocks, ignoring blank-line issues."""
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    frames = []
    total_lines = len(lines)

    for i in range(0, total_lines, FRAME_BLOCK):
        frame = lines[i:i + FRAME_HEIGHT]  # take exactly 91 lines
        if len(frame) == FRAME_HEIGHT:
            frames.append(frame)

    return frames


def build_svg(frames):
    total_frames = len(frames)

    svg_header = textwrap.dedent(f"""
    <svg width="970" height="600" xmlns="http://www.w3.org/2000/svg">
      <style>
        text {{
          font-family: monospace;
          font-size: 12px;
          fill: #c9d1d9;
          white-space: pre;
        }}
      </style>

      <!-- Scale X and Y independently -->
      <g transform="scale({SCALE_X}, {SCALE_Y})">
    """)

    svg_footer = """
      </g>
    </svg>
    """

    body = []

    for i, frame in enumerate(frames):
        # Build tspans for this frame
        tspans = []
        for line_index, line in enumerate(frame):
            y = Y_START + line_index * LINE_HEIGHT
            tspans.append(f'<tspan x="{X_POS}" y="{y}">{line}</tspan>')

        # Build animation values
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

