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
import requests
import os

GODOT_ENGINE_REPOSITORY = "godotengine/godot"
GODOT_SWAPPY_REPOSITORY = "godotengine/godot-swappy"
GODOT_SWAPPY_FILE_NAME = "godot-swappy.zip"


def download_latest_swappy():
	response = requests.get(f'https://api.github.com/repos/{GODOT_SWAPPY_REPOSITORY}/releases/latest')
	data = response.json()

    download_url = None

	for asset in data.get('assets', []):
		if asset['name'].endswith('.zip'):
			download_url = asset['browser_download_url']
            break
    
    if download_url is None:
        print("No downloadable asset found for the latest release.")
        return
    
    file_response = requests.get(download_url)
    file_response.raise_for_status()

    with open(f'workspace/{GODOT_SWAPPY_FILE_NAME}', 'wb') as f:
        f.write(file_response.content)
    
    os.system(f'7z x workspace/{GODOT_SWAPPY_FILE_NAME} -oworkspace/godot/thirdparty/swappy-frame-pacing')


def download_godot(tag):
    clone_url = f"https://github.com/{GODOT_ENGINE_REPOSITORY}.git"

    os.system(f"git clone -b {tag} --depth 1 {clone_url} workspace/godot")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Godot Engine source code")
    parser.add_argument(
        "-t",
        "--tag",
        type=str,
        help="Tag of the Godot Engine version to download",
        required=True,
    )

    args = parser.parse_args()
    tag = args.tag

    download_godot(tag)
