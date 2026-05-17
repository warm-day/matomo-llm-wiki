import os
import sys
import argparse

def sanity_check(file_path):
    """
    Checks if a markdown file is readable and likely not scrambled.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    if not lines:
        print(f"Sanity Check FAILED: {file_path} is empty.")
        return False

    # Check for garbage characters (binary-ish)
    total_chars = 0
    garbage_chars = 0
    for line in lines:
        total_chars += len(line)
        for char in line:
            if not char.isprintable() and char not in ['\n', '\t', '\r']:
                garbage_chars += 1

    garbage_ratio = garbage_chars / total_chars if total_chars > 0 else 0
    if garbage_ratio > 0.05:
        print(f"Sanity Check FAILED: High garbage character density ({garbage_ratio:.2%}).")
        return False

    # Check for extremely long lines without whitespace (typical of PDF encoding errors)
    for i, line in enumerate(lines):
        if len(line) > 500 and ' ' not in line:
            print(f"Sanity Check FAILED: Extremely long line without whitespace at line {i+1}.")
            return False

    print(f"Sanity Check PASSED for {file_path}.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sanity check for converted sources.")
    parser.add_argument("file", help="Path to the file to check")
    args = parser.parse_args()

    if sanity_check(args.file):
        sys.exit(0)
    else:
        sys.exit(1)
