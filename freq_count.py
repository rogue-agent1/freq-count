#!/usr/bin/env python3
"""freq_count - Count frequency of words, chars, or lines."""
import sys, re, collections
def count_words(text, n=20):
    words = re.findall(r"\w+", text.lower())
    return collections.Counter(words).most_common(n)
def count_chars(text, n=20):
    return collections.Counter(c for c in text if not c.isspace()).most_common(n)
def count_lines(text, n=20):
    return collections.Counter(text.strip().split("\n")).most_common(n)
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "words"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    text = sys.stdin.read()
    fn = {"words":count_words,"chars":count_chars,"lines":count_lines}.get(mode, count_words)
    for item, cnt in fn(text, n): print(f"{cnt:>6} {item}")
