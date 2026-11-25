import os

ENTRY_FILE = os.path.join(os.path.dirname(__file__), "entry.txt")


def load_epitaph():
    with open(ENTRY_FILE, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    line = load_epitaph()
    if not line:
        raise SystemExit("entry.txt is empty — nothing to carve.")
    print(line)


if __name__ == "__main__":
    main()
