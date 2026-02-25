import os

INPUT_FILE = "frames.txt"
OUTPUT_FILE = "frames_clean.txt"

def main():
    print("Starting cleanup...")
    print("Working directory:", os.getcwd())

    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = f.read()

    # Replace @ and % with spaces
    cleaned = data.replace("@", " ").replace("%", " ")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print("Done. Output written to", OUTPUT_FILE)

if __name__ == "__main__":
    main()
