import os

TEXT = "My AI agent crashed the demo, then read the stack trace like a stranger's code — it wrote every line."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(TEXT.encode("utf-8"))

if __name__ == "__main__":
    main()
