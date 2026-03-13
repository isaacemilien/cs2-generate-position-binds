import re
import sys
import argparse


def extract_setpos(text):
    pattern = re.compile(
        r'setpos\s+-?\d+(?:\.\d+)?\s+-?\d+(?:\.\d+)?\s+-?\d+(?:\.\d+)?'
        r'(?:;setang\s+-?\d+(?:\.\d+)?\s+-?\d+(?:\.\d+)?\s+-?\d+(?:\.\d+)?)?',
        re.IGNORECASE
    )
    return pattern.findall(text)


def main():
    parser = argparse.ArgumentParser(
        description='Extract clean setpos/setang commands from dirty input text.'
    )
    parser.add_argument(
        '--output', default='positions.txt',
        help='Output .txt file path (default: positions.txt)'
    )
    args = parser.parse_args()

    dirty_text = sys.stdin.read()
    matches = extract_setpos(dirty_text)

    if not matches:
        print('Error: no setpos commands found in input.', file=sys.stderr)
        sys.exit(1)

    with open(args.output, 'w') as f:
        for match in matches:
            f.write(match + '\n')

    print(args.output)


if __name__ == '__main__':
    main()
