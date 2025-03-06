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

build_args_optional = [
    "module_mono_enabled=yes",
    "use_mingw=yes",
    "disable_3d=yes",
    "disable_advanced_gui=yes",
    "lto=full",
    "module_text_server_adv_enabled=no",
    "module_text_server_fb_enabled=yes",
    "module_basis_universal_enabled=no",
    "module_bmp_enabled=no",
    "module_camera_enabled=no",
    "module_csg_enabled=no",
    "module_dds_enabled=no",
    "module_enet_enabled=no",
    "module_gridmap_enabled=no",
    "module_hdr_enabled=no",
    "module_jsonrpc_enabled=no",
    "module_ktx_enabled=no",
    "module_mbedtls_enabled=no",
    "module_meshoptimizer_enabled=no",
    "module_minimp3_enabled=no",
    "module_mobile_vr_enabled=no",
    "module_msdfgen_enabled=no",
    "module_multiplayer_enabled=no",
    "module_noise_enabled=no",
    "module_navigation_enabled=no",
    "module_ogg_enabled=no",
    "module_openxr_enabled=no",
    "module_raycast_enabled=no",
    "module_regex_enabled=no",
    "module_squish_enabled=no",
    "module_svg_enabled=no",
    "module_tga_enabled=no",
    "module_theora_enabled=no",
    "module_tinyexr_enabled=no",
    "module_upnp_enabled=no",
    "module_vhacd_enabled=no",
    "module_vorbis_enabled=no",
    "module_webrtc_enabled=no",
    "module_websocket_enabled=no",
    "module_webxr_enabled=no",
    "module_zip_enabled=no",
]

build_args = {
    "debug": [
        "target=template_debug",
        "dev_mode=yes",
        "optimize=debug",
    ]
    + build_args_optional,
    "release": [
        "target=template_release",
        "production=yes",
        "optimize=speed_trace",
    ]
    + build_args_optional,
}


def handle_pck_encryption():
    if not os.path.exists("workspace/godot.gdkey"):
        return

    with open("workspace/godot.gdkey", "r") as file:
        gdkey_content = file.read()

        print(f"Find pck key is {gdkey_content}")

        os.environ["SCRIPT_AES256_ENCRYPTION_KEY"] = gdkey_content

        if platform.system() == "Windows":
            os.system(f"set SCRIPT_AES256_ENCRYPTION_KEY={gdkey_content}")
        elif platform.system() == "Linux":
            os.system(f'export SCRIPT_AES256_ENCRYPTION_KEY="{gdkey_content}"')


def build_godot(mode):
    handle_pck_encryption()

    args = " ".join(build_args.get(mode, []))

    scons_command = f"scons {args}"

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
