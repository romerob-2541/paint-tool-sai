"""Paint Tool Sai — A local helper for Paint Tool Sai data folders, config and export files, and photo albums on Windows and macOS."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='paint_tool_sai_desktop',
        description='A local helper for Paint Tool Sai data folders, config and export files, and photo albums on Windows and macOS.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Paint Tool Sai')
    print('Keep the Paint Tool Sai data folder tidy before an update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# tweak (2026-11-03)
# minor adjust (2026-11-03)
# refactor bit (2026-11-05)
# polish (2026-11-06)
