"""

MIT License

Copyright (c) 2025 Push To Game

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import argparse
import platform
import os

from config import build_args

def build_godot(mode):
    args = build_args.get(mode, [])

    scons_command = f"scons {' '.join(args)}"

    os.system(f"cd workspace/godot && {scons_command}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Build export templates from source code"
    )
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        choices=["debug", "release"],
        help="Debug or Release mode, value (``debug`` or ``release``)",
        required=True,
    )

    args = parser.parse_args()
    mode = args.mode

    build_godot(mode)
