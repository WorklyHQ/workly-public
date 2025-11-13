"""
VRM Avatar Loading Demo - Workly Public Edition

Demonstrates VRM metadata extraction and display.
This is a simplified educational example.

In the full Workly Desktop, VRM loading is handled by Unity + UniVRM.

Author: WorklyHQ
License: See LICENSE file
"""

import sys
import json
import zipfile
from pathlib import Path


# Simulated VRM data (in reality, this would be parsed from the .vrm file)
SAMPLE_VRM_DATA = {
    "name": "Mura Mura",
    "version": "0.0",
    "author": "VRoid Studio",
    "contact_information": "",
    "reference": "",
    "title": "Sample VRM Model",
    "allowed_user_name": "Everyone",
    "violent_usage": "Disallow",
    "sexual_usage": "Disallow",
    "commercial_usage": "Allow",
    "license_type": "Redistribution_Prohibited",
    "blendshapes": [
        "Neutral",
        "Joy",
        "Angry",
        "Sorrow",
        "Fun",
        "Blink",
        "Blink_L",
        "Blink_R",
    ],
    "bones": [
        "Hips",
        "Spine",
        "Chest",
        "Neck",
        "Head",
        "LeftShoulder",
        "LeftUpperArm",
        "LeftLowerArm",
        "LeftHand",
        "RightShoulder",
        "RightUpperArm",
        "RightLowerArm",
        "RightHand",
        "LeftUpperLeg",
        "LeftLowerLeg",
        "LeftFoot",
        "RightUpperLeg",
        "RightLowerLeg",
        "RightFoot",
    ],
}


def print_header():
    """Print demo header"""
    print("🎭 Workly VRM Avatar Demo")
    print("═" * 60)
    print()


def parse_real_vrm(vrm_path):
    """
    Try to parse a real VRM file

    VRM files are glTF 2.0 files with VRM extensions, stored as .glb (binary glTF)
    They are essentially ZIP archives containing:
    - JSON scene data
    - Binary buffers (geometry, textures)
    - VRM-specific metadata
    """
    try:
        vrm_file = Path(vrm_path)

        if not vrm_file.exists():
            print(f"⚠️  File not found: {vrm_path}")
            print(f"   Using sample data instead.")
            print()
            return None

        print(
            f"📂 Found VRM file: {vrm_file.name} ({vrm_file.stat().st_size / 1024:.1f} KB)"
        )

        # VRM files are glTF binary format
        # We'll do a simple extraction of the JSON data
        with open(vrm_path, "rb") as f:
            # Read glTF header (12 bytes)
            magic = f.read(4)
            if magic != b"glTF":
                print(f"⚠️  Not a valid glTF/VRM file (invalid magic header)")
                print(f"   Using sample data instead.")
                print()
                return None

            version = int.from_bytes(f.read(4), "little")
            length = int.from_bytes(f.read(4), "little")

            print(f"   glTF version: {version}")
            print(f"   File size: {length} bytes")

            # Read JSON chunk (next 8 bytes = chunk header)
            chunk_length = int.from_bytes(f.read(4), "little")
            chunk_type = f.read(4)

            if chunk_type != b"JSON":
                print(f"⚠️  Expected JSON chunk, got {chunk_type}")
                return None

            # Read JSON data
            json_data = f.read(chunk_length).decode("utf-8")
            gltf_data = json.loads(json_data)

            # Extract VRM metadata
            vrm_extension = gltf_data.get("extensions", {}).get("VRM", {})

            if not vrm_extension:
                print(f"⚠️  No VRM extension found in file")
                print(f"   Using sample data instead.")
                print()
                return None

            # Extract metadata
            meta = vrm_extension.get("meta", {})
            blendshape_master = vrm_extension.get("blendShapeMaster", {})

            # Get blendshape names
            blendshapes = []
            for group in blendshape_master.get("blendShapeGroups", []):
                blendshapes.append(group.get("name", "Unknown"))

            # Build VRM data structure
            vrm_data = {
                "name": meta.get("title", "Unknown"),
                "version": meta.get("version", "0.0"),
                "author": meta.get("author", "Unknown"),
                "contact_information": meta.get("contactInformation", ""),
                "reference": meta.get("reference", ""),
                "title": meta.get("title", "Unknown"),
                "allowed_user_name": meta.get("allowedUserName", "Unknown"),
                "violent_usage": meta.get("violentUssageName", "Unknown"),
                "sexual_usage": meta.get("sexualUssageName", "Unknown"),
                "commercial_usage": meta.get("commercialUssageName", "Unknown"),
                "license_type": meta.get("licenseName", "Unknown"),
                "blendshapes": (
                    blendshapes if blendshapes else SAMPLE_VRM_DATA["blendshapes"]
                ),
                "bones": SAMPLE_VRM_DATA[
                    "bones"
                ],  # Would need to parse nodes for real bone data
            }

            print(f"✅ Successfully parsed VRM metadata!")
            print()
            return vrm_data

    except Exception as e:
        print(f"⚠️  Error parsing VRM file: {e}")
        print(f"   Using sample data instead.")
        print()
        return None


def load_vrm_info(vrm_path):
    """
    Extract VRM metadata (hybrid approach)

    1. Try to parse real VRM file if it exists
    2. Fall back to sample data if parsing fails or file doesn't exist
    """
    print(f"📦 Loading VRM from: {vrm_path}")
    print()

    # Try to parse real VRM file
    vrm_data = parse_real_vrm(vrm_path)

    # Fall back to sample data if parsing failed
    if vrm_data is None:
        print("📋 Using sample VRM data for demonstration")
        print()
        import time

        time.sleep(0.3)
        vrm_data = SAMPLE_VRM_DATA

    return vrm_data


def display_model_info(vrm_data):
    """Display VRM model information"""
    print("✅ VRM Model Loaded!")
    print()
    print("📋 Model Information:")
    print("━" * 60)
    print(f"  Name:    {vrm_data['name']}")
    print(f"  Version: {vrm_data['version']}")
    print(f"  Author:  {vrm_data['author']}")
    print(f"  Title:   {vrm_data['title']}")
    print()


def display_blendshapes(vrm_data):
    """Display available blendshapes (facial expressions)"""
    print("🎭 Available Expressions:")
    print("━" * 60)

    for i, blendshape in enumerate(vrm_data["blendshapes"], 1):
        # Add emoji for common expressions
        emoji = {
            "Joy": "😊",
            "Angry": "😠",
            "Sorrow": "😢",
            "Fun": "😆",
            "Blink": "😑",
            "Neutral": "😐",
        }.get(blendshape, "🎭")

        print(f"  {i}. {emoji} {blendshape}")

    print()


def display_license_info(vrm_data):
    """Display VRM usage license"""
    print("📜 Usage License:")
    print("━" * 60)
    print(f"  Commercial Use:  {vrm_data['commercial_usage']}")
    print(f"  Violent Content: {vrm_data['violent_usage']}")
    print(f"  Sexual Content:  {vrm_data['sexual_usage']}")
    print(f"  License Type:    {vrm_data['license_type']}")
    print()


def display_technical_info(vrm_data):
    """Display technical details"""
    print("🔧 Technical Details:")
    print("━" * 60)
    print(f"  Blendshapes:  {len(vrm_data['blendshapes'])} shapes")
    print(f"  Bones:        {len(vrm_data['bones'])} bones")
    print()

    print("  Bone Hierarchy Sample:")
    for bone in vrm_data["bones"][:10]:
        print(f"    - {bone}")
    if len(vrm_data["bones"]) > 10:
        print(f"    ... and {len(vrm_data['bones']) - 10} more")
    print()


def simulate_expression_change():
    """Simulate changing expressions"""
    print("🎬 Expression Animation Demo:")
    print("━" * 60)

    expressions = [
        ("Neutral", "😐", 0.0),
        ("Joy", "😊", 1.0),
        ("Angry", "😠", 1.0),
        ("Sorrow", "😢", 1.0),
        ("Fun", "😆", 1.0),
        ("Neutral", "😐", 0.0),
    ]

    import time

    for expr_name, emoji, weight in expressions:
        print(f"  {emoji} Setting expression: {expr_name} (weight: {weight})")
        time.sleep(0.3)

    print()
    print("✅ Expression animation complete!")
    print()


def main():
    """Main function"""
    print_header()

    # Get VRM path from command line or use default
    if len(sys.argv) > 1:
        vrm_path = sys.argv[1]
    else:
        # Ask user for VRM path
        print("📂 VRM File Selection:")
        print("━" * 60)
        print("  1. Enter custom path")
        print("  2. Use sample data (no file)")
        print()

        choice = input("Choose option (1-2): ").strip()
        print()

        if choice == "2":
            # Sample data
            vrm_path = "sample_data"
        else:
            # Custom path (default)
            # Note: The default example uses "Mura Mura" model by AcidicDoll
            # This model is NOT included in this repo
            # Download from: https://acidicdollz.booth.pm/items/4613390
            # License: Free for personal use, no redistribution, attribution required
            vrm_path = input("Enter VRM file path: ").strip()
            # Remove quotes if user pasted a path with quotes
            vrm_path = vrm_path.strip('"').strip("'")

    # Load VRM info
    vrm_data = load_vrm_info(vrm_path)

    # Display information
    display_model_info(vrm_data)
    display_blendshapes(vrm_data)
    display_license_info(vrm_data)
    display_technical_info(vrm_data)

    # Simulate expression changes
    simulate_expression_change()

    # Final notes
    print("📝 Notes:")
    print("━" * 60)
    print("  This demo can parse real VRM files or use sample data.")
    print()
    print("  Usage:")
    print("    python load_vrm.py                    # Interactive menu")
    print("    python load_vrm.py path/to/model.vrm  # Direct load")
    print()
    print("  The full Workly Desktop uses Unity + UniVRM for:")
    print("    - Real-time 3D rendering")
    print("    - Smooth expression transitions")
    print("    - Advanced lighting and shading")
    print("    - Desktop window integration")
    print()
    print("🔗 Learn more: https://github.com/WorklyHQ/workly-public")
    print()


if __name__ == "__main__":
    main()
