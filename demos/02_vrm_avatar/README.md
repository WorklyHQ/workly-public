# 🎭 VRM Avatar Loading Demo

Demonstrates how Workly loads and processes VRM (Virtual Reality Model) files.

## 📋 Overview

This demo shows:
- VRM metadata extraction
- Blendshape (expression) information
- Model information display
- Basic VRM file structure

## 🛠️ Requirements

- Python 3.11+
- No external dependencies (uses standard library)

> **Note:** This is a simplified demo. The full Workly Desktop uses Unity with UniVRM for actual 3D rendering.

## 📦 Installation

No installation required! This demo uses only Python standard library.

## 🚀 Usage

### Interactive Mode (Recommended)

Run the demo without arguments to get an interactive menu:
```bash
python load_vrm.py
```

You'll see:
```
📂 VRM File Selection:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Enter custom path
  2. Use sample data (no file)

Choose option (1-2):
```

**Option 1 - Load Real VRM File:**
- Choose option `1`
- Paste or type the path to your VRM file
- The demo will parse the actual VRM metadata

**Option 2 - Use Sample Data:**
- Choose option `2`
- Uses pre-defined sample data (no file needed)
- Good for testing the demo without a VRM file

### Command Line Mode

Load a VRM file directly:
```bash
python load_vrm.py "C:\path\to\your\model.vrm"
```

Or with relative path:
```bash
python load_vrm.py ../../workly-desktop/assets/Mura\ Mura\ -\ Model.vrm
```

> **Tip:** You can drag-and-drop a VRM file into the terminal to auto-paste its path!

### Example Output (Real VRM File)

When loading the Mura Mura model:
```
🎭 Workly VRM Avatar Demo
════════════════════════════════════════════════════════════

📂 VRM File Selection:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Enter custom path
  2. Use sample data (no file)

Choose option (1-2): 1

Enter VRM file path: C:\Dev\workly_project\workly-desktop\assets\Mura Mura - Model.vrm

📦 Loading VRM from: C:\Dev\workly_project\workly-desktop\assets\Mura Mura - Model.vrm

📂 Found VRM file: Mura Mura - Model.vrm (15242.9 KB)
   glTF version: 2
   File size: 15608680 bytes
✅ Successfully parsed VRM metadata!

✅ VRM Model Loaded!

📋 Model Information:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Name:    Mura Mura
  Version: 0.0
  Author:  AcidicDoll
  Title:   Mura Mura

🎭 Available Expressions:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. 😐 Neutral
  2. 🎭 A
  3. 🎭 I
  4. 🎭 U
  5. 🎭 E
  6. 🎭 O
  7. 😑 Blink
  8. 🎭 Blink_L
  9. 🎭 Blink_R
  10. 😠 Angry
  11. 😆 Fun
  12. 😊 Joy
  13. 😢 Sorrow
  14. 🎭 Surprised

📜 Usage License:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Commercial Use:  Disallow
  Violent Content: Allow
  Sexual Content:  Allow
  License Type:    Redistribution_Prohibited

🔧 Technical Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Blendshapes:  14 shapes
  Bones:        19 bones

  Bone Hierarchy Sample:
    - Hips
    - Spine
    - Chest
    - Neck
    - Head
    - LeftShoulder
    - LeftUpperArm
    - LeftLowerArm
    - LeftHand
    - RightShoulder
    ... and 9 more

🎬 Expression Animation Demo:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  😐 Setting expression: Neutral (weight: 0.0)
  😊 Setting expression: Joy (weight: 1.0)
  😠 Setting expression: Angry (weight: 1.0)
  😢 Setting expression: Sorrow (weight: 1.0)
  😆 Setting expression: Fun (weight: 1.0)
  😐 Setting expression: Neutral (weight: 0.0)

✅ Expression animation complete!
```

## ⚙️ What This Demo Does

### Real VRM Parsing (Hybrid Approach)

This demo can **actually parse real VRM files**:

1. **Reads glTF Binary Format**: Parses the VRM file structure (glTF 2.0)
2. **Extracts Real Metadata**: Gets actual model name, author, version from the file
3. **Lists Real Blendshapes**: Shows the actual expressions available in your model
4. **Displays License Info**: Shows commercial usage rights and restrictions
5. **Falls Back Gracefully**: Uses sample data if file not found or parsing fails

### Technical Capabilities

✅ **What it CAN do:**
- Parse VRM/glTF binary header
- Extract JSON metadata from VRM files
- Read VRM extension data (meta, blendShapes)
- Display model information and license
- Show available expressions

❌ **What it CANNOT do** (requires Unity + UniVRM):
- Render 3D models
- Display textures
- Animate the avatar
- Real-time expression changes
- Physics simulation

## 🔧 Technical Details

### VRM File Format

VRM is based on **glTF 2.0** with additional extensions:
- **Format**: Binary glTF (.glb) with VRM extension
- **Structure**:
  - Header (12 bytes): Magic "glTF", version, length
  - JSON chunk: Scene graph, nodes, materials, **VRM metadata**
  - Binary chunks: Geometry, textures, buffers
- **VRM Extension**: Custom data for humanoid avatars

Components in VRM files:
- **Mesh data**: 3D geometry (vertices, triangles)
- **Materials**: Textures and shaders (MToon shader)
- **Bones**: Skeleton for animation (humanoid rig)
- **Blendshapes**: Facial expressions (morphs)
- **Metadata**: Author, license, usage rights
- **Spring Bones**: Hair/cloth physics
- **Look At**: Eye tracking parameters

### Blendshape System

Blendshapes control facial expressions:
- Each blendshape is a weight from 0.0 to 1.0
- Multiple blendshapes can be active simultaneously
- Smooth transitions create natural expressions

Common blendshapes in VRM:
- `Joy` — Happy expression
- `Angry` — Angry expression
- `Sorrow` — Sad expression
- `Fun` — Playful expression
- `Blink`, `Blink_L`, `Blink_R` — Eye blinking

### How the Demo Parses VRM Files

The demo implements a basic VRM parser:

```python
def parse_real_vrm(vrm_path):
    with open(vrm_path, 'rb') as f:
        # 1. Read glTF header
        magic = f.read(4)  # Should be b'glTF'
        version = int.from_bytes(f.read(4), 'little')  # glTF version 2
        length = int.from_bytes(f.read(4), 'little')   # Total file size

        # 2. Read JSON chunk header
        chunk_length = int.from_bytes(f.read(4), 'little')
        chunk_type = f.read(4)  # Should be b'JSON'

        # 3. Parse JSON data
        json_data = f.read(chunk_length).decode('utf-8')
        gltf_data = json.loads(json_data)

        # 4. Extract VRM extension
        vrm_extension = gltf_data['extensions']['VRM']
        meta = vrm_extension['meta']
        blendshapes = vrm_extension['blendShapeMaster']['blendShapeGroups']

        return {
            'name': meta['title'],
            'author': meta['author'],
            'blendshapes': [bs['name'] for bs in blendshapes],
            # ... more data
        }
```

### Unity Integration (Full Workly Desktop)

In the full Workly Desktop:
```csharp
// Unity C# code (not included in demo)
using UniVRM10;

// Load VRM
var vrm = Vrm10.LoadFromPath(vrmPath);

// Set expression
var expressionProxy = vrm.GetComponent<VRM10Expression>();
expressionProxy.SetExpression("Joy", 1.0f);
```

## 📊 VRM Models

Compatible VRM sources:
- **VRoid Studio**: https://vroid.com/studio
- **VRoid Hub**: https://hub.vroid.com
- **Booth**: https://booth.pm (search for VRM)
- **Custom models**: Any VRM 0.0 or VRM 1.0 compliant

## 🎯 Next Steps

To build on this demo:
1. Add actual VRM parsing (requires glTF library)
2. Extract texture information
3. Display bone hierarchy
4. Show animation clips
5. Implement thumbnail generation

## 🎯 Key Differences: Demo vs Full Workly

| Feature | This Demo | Full Workly Desktop |
|---------|-----------|---------------------|
| **File Parsing** | ✅ Yes (basic JSON extraction) | ✅ Yes (full glTF parsing) |
| **Metadata Display** | ✅ Yes (name, author, license) | ✅ Yes (complete info) |
| **Blendshape List** | ✅ Yes (from file) | ✅ Yes (from file) |
| **3D Rendering** | ❌ No | ✅ Yes (Unity + URP) |
| **Expression Animation** | ❌ No (simulated only) | ✅ Yes (real-time) |
| **Texture Display** | ❌ No | ✅ Yes (full materials) |
| **Physics** | ❌ No | ✅ Yes (SpringBone) |
| **Desktop Integration** | ❌ No | ✅ Yes (transparent window) |
| **Eye Tracking** | ❌ No | ✅ Yes (LookAt system) |

## 📦 Model License Notice

**Demo Example Model:**

This demo references the **"Mura Mura"** VRM model by [AcidicDoll](https://acidicdollz.booth.pm/items/4613390) as an example. This model is **NOT included** in this repository.

**License Terms:**
- ✅ **Credit**: AcidicDoll
- ✅ **Modification**: Allowed
- ✅ **Personal use**: Free
- ❌ **Redistribution**: Prohibited
- ❌ **Commercial use**: Prohibited
- ❌ **Resale**: Prohibited

**Download**: [BOOTH](https://acidicdollz.booth.pm/items/4613390) | [Ko-fi](https://ko-fi.com/s/06bbeaeef1)

**For Workly Desktop:** You can use **any VRM model** you have rights to use.

---

## 📝 Notes

- This demo can **parse real VRM files** but only extracts metadata (no 3D rendering)
- Full 3D rendering requires Unity + UniVRM (used in Workly Desktop)
- The full Workly Desktop supports **VRM 0.0 and VRM 1.0** formats
- Real-time rendering uses **Unity's Universal Render Pipeline (URP)**
- This is a **standalone Python demo** — no Unity or dependencies needed!

## 🔗 Related

- [VRM Specification](https://github.com/vrm-c/vrm-specification)
- [UniVRM (Unity)](https://github.com/vrm-c/UniVRM)
- [Full Documentation](../../docs/ARCHITECTURE.md)

---

**Part of [Workly Public Edition](../../README.md)**
