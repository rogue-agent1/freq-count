#!/usr/bin/env python3
"""freq_count - Frequency analysis tool."""
import sys, argparse, json, re
from collections import Counter

def count_chars(text):
    return Counter(text)

def count_words(text):
    return Counter(re.findall(r"\b\w+\b", text.lower()))

def count_lines(text):
    return Counter(text.splitlines())

def main():
    p = argparse.ArgumentParser(description="Frequency counter")
    p.add_argument("input", help="Text or @filename")
    p.add_argument("--mode", choices=["chars","words","lines"], default="words")
    p.add_argument("--top", type=int, default=20)
    p.add_argument("--min-count", type=int, default=1)
    args = p.parse_args()
    text = args.input
    if text.startswith("@"):
        with open(text[1:]) as f: text = f.read()
    if args.mode == "chars": freq = count_chars(text)
    elif args.mode == "words": freq = count_words(text)
    else: freq = count_lines(text)
    filtered = {k: v for k, v in freq.items() if v >= args.min_count}
    top = Counter(filtered).most_common(args.top)
    total = sum(freq.values())
    print(json.dumps({"mode": args.mode, "total": total, "unique": len(freq), "top": [{"item": k, "count": v, "pct": round(v/total*100, 2)} for k, v in top]}, indent=2))

if __name__ == "__main__": main()
