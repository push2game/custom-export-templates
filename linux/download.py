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

import requests
import subprocess

BUILDROOT_REPOSITORY = "godotengine/buildroot"
BUILDROOT_FILENAME = "x86_64-godot-linux-gnu_sdk-buildroot.tar.bz2"


def get_latest_tag_buildroot():
    response = requests.get(
        f"https://api.github.com/repos/{BUILDROOT_REPOSITORY}/releases/latest"
    )
    response_json = response.json()
    return response_json["tag_name"]


def download_buildroot(tag):
    download_url = f"https://github.com/{BUILDROOT_REPOSITORY}/releases/download/{tag}/{BUILDROOT_FILENAME}"

    file_response = requests.get(download_url)
    file_response.raise_for_status()

    with open(f"workspace/{BUILDROOT_FILENAME}", "wb") as f:
        f.write(file_response.content)

    subprocess.run(
        f"tar -xjf workspace/{BUILDROOT_FILENAME} -C workspace/buildroot/", check=True
    )


def download_linux_impl():
    tag = get_latest_tag_buildroot()
    download_buildroot(tag)
