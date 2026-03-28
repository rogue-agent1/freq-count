#!/usr/bin/env python3
"""freq_count - Count frequencies in text files."""
import sys, collections

def analyze(text, mode="char"):
    if mode == "word": items = text.lower().split()
    elif mode == "line": items = text.strip().split("\n")
    else: items = list(text)
    counter = collections.Counter(items)
    return counter.most_common(20)

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: freq_count <file> [char|word|line]"); sys.exit(1)
    mode = sys.argv[2] if len(sys.argv) > 2 else "word"
    with open(sys.argv[1]) as f: text = f.read()
    for item, count in analyze(text, mode):
        display = repr(item) if mode == "char" else item[:60]
        print(f"{count:6d}  {display}")
