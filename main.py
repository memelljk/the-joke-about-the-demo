"""Entry program: write one joke line to /output/entry.txt."""

import os

JOKE_TEXT = "My AI agent crashed the demo, then read the stack trace like a stranger's code — it wrote every line."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_entry() -> None:
    """Create /output if needed, then write the joke as raw UTF-8 bytes.

    Binary mode keeps the output exact: no trailing newline is added,
    so the file is precisely the joke text and nothing else.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    payload = JOKE_TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(payload)


if __name__ == "__main__":
    write_entry()
