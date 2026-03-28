#!/usr/bin/env python3
"""Character and word frequency counter."""
import sys, collections, json

def count(text, mode='word', top=20):
    if mode == 'char':
        items = collections.Counter(c for c in text if not c.isspace())
    else:
        items = collections.Counter(text.lower().split())
    return items.most_common(top)

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('file', nargs='?', default='-')
    p.add_argument('-m', '--mode', choices=['word','char'], default='word')
    p.add_argument('-n', '--top', type=int, default=20)
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    text = sys.stdin.read() if args.file == '-' else open(args.file).read()
    result = count(text, args.mode, args.top)
    if args.json:
        print(json.dumps(dict(result), indent=2))
    else:
        for item, cnt in result:
            bar = '█' * min(cnt, 40)
            print(f"{item:>15} {cnt:>5} {bar}")

if __name__ == '__main__':
    main()
