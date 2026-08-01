#!/usr/bin/env python3
"""
===============================================================================
 Prototype (2009) - High Resolution & Widescreen Fix (v1.0)
===============================================================================
 Developed via Reverse Engineering by Antigravity AI & Luigi.

 This script safely patches `prototypeenginef.dll` in-place to unlock higher
 widescreen resolutions (1080p, 1200p+) and bypass modern hardware VRAM
 and resolution caps that limit the game to 1280x800 on modern GPUs.

 Usage:
   1. Close Prototype if running.
   2. Run: python PrototypeResolutionFix.py
   3. Launch Prototype and select your desired resolution in Options > Graphics.

 Legal & Clean: Modifies your local file directly without redistributing
 copyrighted binaries.
===============================================================================
"""

import os
import sys
import shutil

DLL_NAME = "prototypeenginef.dll"
BAK_NAME = "prototypeenginef.dll.bak"
GAME_EXE = "prototypef.exe"

PATCHES = [
    {
        "name": "Remove 1280x800 Hardcoded Safety Cap",
        "offset": 0x2E02B7,
        "original": b"\x7D\x17",
        "patched":  b"\xEB\x17",
        "description": "Bypasses hardcoded 1280x800 limit triggered on modern GPUs"
    },
    {
        "name": "VRAM Quality Menu Bypass",
        "offset": 0x4DFC3C,
        "original": b"\x7D\x06",
        "patched":  b"\xEB\x06",
        "description": "Prevents graphics options from resetting to low quality"
    },
    {
        "name": "Direct3D 9 Display Mode Validation Bypass",
        "offset": 0x616F20,
        "original": b"\x8B\x44\x24\x0C\x53",
        "patched":  b"\xB0\x01\xC2\x0C\x00",
        "description": "Forces EnumAdapterModes to accept higher display modes"
    }
]

COMMON_STEAM_PATHS = [
    r"C:\Program Files (x86)\Steam\steamapps\common\Prototype",
    r"C:\Program Files\Steam\steamapps\common\Prototype",
    r"D:\Steam\steamapps\common\Prototype",
    r"D:\SteamLibrary\steamapps\common\Prototype",
    r"E:\SteamLibrary\steamapps\common\Prototype",
]


def find_game_directory():
    """Locate the real Prototype game directory."""
    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd, GAME_EXE)):
        return cwd

    for path in COMMON_STEAM_PATHS:
        if os.path.exists(os.path.join(path, GAME_EXE)):
            return path

    return None


def main():
    print("=" * 70)
    print("   Prototype (2009) - High Resolution & Widescreen Fix (v1.0)")
    print("=" * 70)

    game_dir = find_game_directory()

    if game_dir is None:
        print("[ERROR] Could not find the Prototype installation folder.")
        print("Please place this script inside your Prototype game directory")
        print("(where prototypef.exe is located) and run it again.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    target_path = os.path.join(game_dir, DLL_NAME)
    bak_path = os.path.join(game_dir, BAK_NAME)

    print(f"[+] Game directory: {game_dir}")
    print(f"[+] Target file:    {target_path}")

    if not os.path.exists(target_path):
        print(f"[ERROR] '{DLL_NAME}' not found in game directory.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    # Backup
    if not os.path.exists(bak_path):
        print(f"[+] Creating original backup: {BAK_NAME}...")
        try:
            shutil.copyfile(target_path, bak_path)
            print("[+] Backup created successfully!")
        except Exception as e:
            print(f"[!] Error creating backup: {e}")
            sys.exit(1)
    else:
        print(f"[+] Backup already exists ({BAK_NAME}).")

    # Read
    try:
        with open(target_path, "rb") as f:
            data = bytearray(f.read())
    except PermissionError:
        print("[!] ERROR: Permission denied! Make sure Prototype is CLOSED.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    print("\n[+] Applying patches...")

    # Apply patches
    for patch in PATCHES:
        off = patch["offset"]
        orig = patch["original"]
        pat = patch["patched"]
        current = bytes(data[off:off + len(orig)])

        if current == pat:
            print(f"  - [{patch['name']}] -> ALREADY PATCHED at {hex(off)}")
        elif current == orig:
            data[off:off + len(pat)] = pat
            print(f"  - [{patch['name']}] -> SUCCESS at {hex(off)}")
        else:
            print(f"  - [WARNING] [{patch['name']}] Unexpected bytes at {hex(off)}: {current.hex()}")
            print(f"    Expected: {orig.hex()} | This DLL version may not be compatible.")

    # Save
    try:
        with open(target_path, "wb") as f:
            f.write(data)
        print("\n" + "=" * 70)
        print("  SUCCESS! prototypeenginef.dll has been patched.")
        print("  Launch Prototype and select your desired resolution in")
        print("  Options > Graphics!")
        print("=" * 70)
    except PermissionError:
        print("\n[!] ERROR: File locked. Close Prototype and try again.")
        sys.exit(1)

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
