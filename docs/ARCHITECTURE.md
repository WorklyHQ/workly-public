# 🏗️ Workly Desktop — Architecture

Technical architecture and system design overview.

## 📋 System Overview

Workly Desktop is a **hybrid application** combining:
- **Python** — Application logic, AI, GUI
- **Unity** — 3D rendering, VRM avatars
- **IPC** — Inter-process communication

```
┌─────────────────────────────────────────────────┐
│                  Workly Desktop                  │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌─────────────────┐      ┌─────────────────┐  │
│  │   Python Core   │◄────►│  Unity Renderer │  │
│  │                 │ TCP  │                 │  │
│  │  • AI Engine    │ JSON │  • VRM Avatar   │  │
│  │  • GUI (Qt)     │      │  • Expressions  │  │
│  │  • Memory       │      │  • Animations   │  │
│  │  • Discord      │      │  • Rendering    │  │
│  └─────────────────┘      └─────────────────┘  │
│           │                                      │
│  ┌────────▼────────────────────────────────┐   │
│  │        SQLite Database                   │   │
│  │  • Conversations • Config • Sessions     │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

## 🔧 Component Architecture

### 1. Python Core (`src/`)

#### AI Engine (`src/ai/`)
```
ai/
├── chat_engine.py      ← Main conversation engine
├── llm_manager.py      ← Model loading & inference
├── context_manager.py  ← Context window management
└── memory_interface.py ← Memory system integration
```

**Responsibilities:**
- Load and manage LLM models (GGUF)
- Generate AI responses
- Manage conversation context
- Interface with memory system

**Key Classes:**
- `ChatEngine` — Main conversation coordinator
- `LLMManager` — Model loading & inference
- `ContextManager` — Context window & token management

#### GUI Layer (`src/gui/`)
```
gui/
├── main_window.py      ← Main application window
├── settings_dialog.py  ← Settings interface
├── chat_widget.py      ← Chat display
└── expression_panel.py ← Expression controls
```

**Responsibilities:**
- User interface (PySide6/Qt)
- Settings management
- User input handling
- Status display

#### IPC Bridge (`src/ipc/`)
```
ipc/
├── python_bridge.py    ← Python-side IPC
├── protocol.py         ← Message protocol
└── message_queue.py    ← Thread-safe queue
```

**Responsibilities:**
- TCP socket communication
- JSON message serialization
- Thread-safe message passing
- Connection management

#### Memory System (`src/utils/`)
```
utils/
├── database.py         ← SQLite interface
├── config_manager.py   ← Configuration
└── logger.py           ← Logging system
```

### 2. Unity Renderer (`unity/`)

#### Core Scripts
```
unity/Assets/Scripts/
├── PythonBridge.cs             ← Unity-side IPC
├── VRMLoader.cs                ← VRM model loading
├── VRMBlendshapeController.cs  ← Expression control
└── AutoBlinkSystem.cs          ← Blink automation
```

**Responsibilities:**
- 3D rendering (URP)
- VRM model loading (UniVRM)
- Expression control
- Animation system

**Key Components:**
- `PythonBridge` — IPC communication
- `VRMLoader` — VRM file loading
- `VRMBlendshapeController` — Facial expressions
- `AutoBlinkSystem` — Eye blinking

### 3. Data Layer

#### SQLite Database
```sql
-- Conversations table
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    role TEXT,
    message TEXT,
    session_id TEXT,
    metadata TEXT
);

-- Configuration table
CREATE TABLE config (
    key TEXT PRIMARY KEY,
    value TEXT
);

-- Sessions table
CREATE TABLE sessions (
    id TEXT PRIMARY KEY,
    started_at TEXT,
    ended_at TEXT,
    message_count INTEGER
);
```

## 🔄 Data Flow

### 1. User Input → AI Response

```
User types message
       ↓
Python GUI receives input
       ↓
ChatEngine processes
       ↓
ContextManager retrieves history
       ↓
LLMManager generates response
       ↓
Save to database
       ↓
Display in GUI
       ↓
(Optional) Send to Unity for expression
```

### 2. Expression Control

```
Python: Trigger expression
       ↓
IPC: Send JSON message
       {
         "type": "set_expression",
         "expression": "Joy",
         "weight": 1.0,
         "duration": 2.0
       }
       ↓
Unity: PythonBridge receives
       ↓
Unity: VRMBlendshapeController processes
       ↓
Unity: Animate blendshape
```

### 3. VRM Loading

```
User selects VRM file
       ↓
Python: Send load command
       ↓
Unity: VRMLoader.LoadVRM()
       ↓
Unity: Parse VRM metadata
       ↓
Unity: Load mesh, materials, bones
       ↓
Unity: Setup blendshapes
       ↓
Unity: Send "loaded" confirmation
       ↓
Python: Update GUI status
```

## 🧵 Threading Model

### Python Threading
```
Main Thread (GUI)
  ├─ Qt Event Loop
  └─ User Interface

IPC Thread
  ├─ Socket Listen
  └─ Message Queue

AI Thread
  ├─ LLM Inference
  └─ Response Generation

Background Thread
  ├─ Database Operations
  └─ File I/O
```

### Unity Threading
```
Main Thread (Unity)
  ├─ Rendering
  ├─ Animation
  └─ Update Loop

IPC Thread
  ├─ Socket Listen
  └─ Message Receive

Queue Processing (Main Thread)
  ├─ Dequeue messages
  └─ Execute commands
```

**Critical:** Unity API calls MUST happen on main thread!

## 🔌 IPC Protocol

### Message Format (JSON)
```json
{
  "type": "command_name",
  "data": {
    "param1": "value1",
    "param2": "value2"
  },
  "timestamp": "2025-11-13T14:30:00",
  "id": "unique_message_id"
}
```

### Available Commands

#### Python → Unity
```json
// Load VRM model
{"type": "load_vrm", "data": {"path": "C:/path/to/model.vrm"}}

// Set expression
{"type": "set_expression", "data": {"expression": "Joy", "weight": 1.0}}

// Set window properties
{"type": "set_window", "data": {"always_on_top": true, "transparent": true}}
```

#### Unity → Python
```json
// VRM loaded confirmation
{"type": "vrm_loaded", "data": {"success": true, "blendshapes": ["Joy", "Angry"]}}

// Error message
{"type": "error", "data": {"message": "Failed to load VRM", "code": "ERR_VRM_001"}}

// Status update
{"type": "status", "data": {"fps": 60, "memory_mb": 512}}
```

## 🎨 Rendering Pipeline (Unity)

```
┌─────────────────────────────────────┐
│  Universal Render Pipeline (URP)    │
├─────────────────────────────────────┤
│                                      │
│  1. VRM Model                        │
│     └─ Mesh + Materials + Bones     │
│                                      │
│  2. Blendshape Animation             │
│     └─ Facial expressions            │
│                                      │
│  3. Lighting                         │
│     └─ Real-time lights              │
│                                      │
│  4. Post-Processing                  │
│     └─ Anti-aliasing, bloom          │
│                                      │
│  5. Transparent Background           │
│     └─ Alpha channel rendering       │
│                                      │
│  6. Output to Screen                 │
│     └─ 60 FPS target                 │
│                                      │
└─────────────────────────────────────┘
```

## 📊 Performance Optimizations

### Python Optimizations
- ✅ **Async I/O** — Non-blocking operations
- ✅ **Thread pooling** — Reuse threads
- ✅ **Lazy loading** — Load on demand
- ✅ **Caching** — Cache frequent queries
- ✅ **Batch operations** — Group database writes

### Unity Optimizations
- ✅ **Object pooling** — Reuse GameObjects
- ✅ **Occlusion culling** — Don't render hidden objects
- ✅ **LOD system** — Level of detail (planned)
- ✅ **Async loading** — Load resources asynchronously
- ✅ **GPU instancing** — Efficient rendering

### AI Optimizations
- ✅ **Quantized models** — Q4/Q5/Q8 GGUF
- ✅ **GPU acceleration** — CUDA support
- ✅ **Batch inference** — Process multiple inputs
- ✅ **Context caching** — Reuse KV cache
- ✅ **Early stopping** — Stop on completion tokens

## 🔒 Security Considerations

### Local Processing
- ✅ All AI inference is **100% local**
- ✅ No data sent to external servers
- ✅ Conversations stored in **local SQLite**
- ✅ No telemetry or analytics

### Process Isolation
- ✅ Python and Unity run in **separate processes**
- ✅ IPC uses **localhost only** (127.0.0.1)
- ✅ No external network access required
- ✅ Database encryption available (planned)

### File Access
- ✅ VRM files validated before loading
- ✅ Config files JSON-validated
- ✅ User data in standard app directories
- ✅ No privileged operations required

## 📁 Directory Structure

```
workly-desktop/
├── main.py                 ← Entry point
├── requirements.txt        ← Python dependencies
├── config.json            ← User configuration
├── src/                   ← Python source
│   ├── ai/               ← AI engine
│   ├── gui/              ← GUI components
│   ├── ipc/              ← IPC bridge
│   └── utils/            ← Utilities
├── unity/                 ← Unity project
│   ├── Assets/
│   │   ├── Scripts/      ← C# scripts
│   │   ├── Models/       ← VRM models
│   │   └── Scenes/       ← Unity scenes
│   └── Packages/         ← Unity packages (UniVRM)
├── data/                  ← User data
│   ├── database.db       ← SQLite database
│   ├── models/           ← GGUF models
│   └── avatars/          ← VRM files
└── logs/                  ← Log files
```

## 🔗 Technology Stack

### Python Stack
| Component | Technology | Purpose |
|-----------|-----------|---------|
| GUI | PySide6 (Qt 6) | User interface |
| AI | llama-cpp-python | LLM inference |
| Database | SQLite3 | Data storage |
| Networking | socket | IPC communication |
| Async | asyncio, threading | Concurrency |

### Unity Stack
| Component | Technology | Purpose |
|-----------|-----------|---------|
| Engine | Unity 2022.3 LTS | 3D rendering |
| Pipeline | URP | Rendering pipeline |
| VRM | UniVRM | VRM support |
| Scripting | C# .NET | Game logic |

## 📚 Design Patterns

### Used Patterns
- **Singleton** — ChatEngine, ConfigManager
- **Observer** — Event system (GUI updates)
- **Factory** — Message creation
- **Command** — IPC commands
- **Repository** — Database access
- **Bridge** — Python ↔ Unity IPC

## 🔮 Future Architecture

### Planned Improvements
- 🔜 **Plugin system** — Extensible architecture
- 🔜 **Microservices** — Separate AI, TTS services
- 🔜 **Event bus** — Decoupled communication
- 🔜 **Vector database** — Semantic search
- 🔜 **Cloud sync** — Optional backup (Workly Pro)

---

**[← Back to Documentation](README.md)** | **[View Roadmap →](ROADMAP.md)**
