# 🔌 Workly Desktop — API Reference

IPC Protocol and API Specifications

## 📋 Overview

Workly uses **TCP sockets** with **JSON messages** for communication between the Python core and Unity renderer.

```
Python (127.0.0.1:5555) ←─── TCP/JSON ───→ Unity (Client)
```

## 🔗 Connection

### Server (Python)
```python
import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen(1)

conn, addr = server.accept()
```

### Client (Unity C#)
```csharp
using System.Net.Sockets;

TcpClient client = new TcpClient("127.0.0.1", 5555);
NetworkStream stream = client.GetStream();
```

## 📨 Message Format

### Basic Structure
```json
{
  "type": "command_name",
  "data": {
    "param1": "value1",
    "param2": "value2"
  },
  "timestamp": "2025-11-13T14:30:00.000Z",
  "id": "msg_123456"
}
```

### Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | ✅ Yes | Command type |
| `data` | object | ✅ Yes | Command parameters |
| `timestamp` | string | ⚠️ Optional | ISO 8601 timestamp |
| `id` | string | ⚠️ Optional | Unique message ID |

## 🔄 Commands Reference

---

## Python → Unity Commands

### 1. Load VRM Model

Load a VRM avatar file.

**Command:**
```json
{
  "type": "load_vrm",
  "data": {
    "path": "C:/path/to/model.vrm"
  }
}
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `path` | string | ✅ | Absolute path to VRM file |

**Response:**
```json
{
  "type": "vrm_loaded",
  "data": {
    "success": true,
    "model_name": "Mura Mura",
    "blendshapes": ["Joy", "Angry", "Sorrow", "Fun"],
    "bone_count": 55
  }
}
```

**Error Response:**
```json
{
  "type": "error",
  "data": {
    "command": "load_vrm",
    "message": "File not found",
    "code": "ERR_VRM_001"
  }
}
```

---

### 2. Set Expression

Change facial expression with transition.

**Command:**
```json
{
  "type": "set_expression",
  "data": {
    "expression": "Joy",
    "weight": 1.0,
    "duration": 2.0
  }
}
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `expression` | string | ✅ | Expression name (Joy, Angry, Sorrow, Fun, etc.) |
| `weight` | float | ⚠️ | Expression intensity (0.0-1.0), default: 1.0 |
| `duration` | float | ⚠️ | Transition duration in seconds, default: 1.0 |

**Available Expressions:**
- `Neutral` — Default neutral face
- `Joy` — Happy/smiling
- `Angry` — Angry/frustrated
- `Sorrow` — Sad/crying
- `Fun` — Playful/excited
- `Surprised` — Shocked/amazed
- `Relaxed` — Calm/peaceful

**Response:**
```json
{
  "type": "expression_set",
  "data": {
    "expression": "Joy",
    "weight": 1.0
  }
}
```

---

### 3. Reset Expression

Reset to neutral expression.

**Command:**
```json
{
  "type": "reset_expression",
  "data": {
    "duration": 1.0
  }
}
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `duration` | float | ⚠️ | Transition duration, default: 1.0 |

---

### 4. Set Window Properties

Configure Unity window behavior.

**Command:**
```json
{
  "type": "set_window",
  "data": {
    "always_on_top": true,
    "transparent": true,
    "click_through": false,
    "size": {"width": 800, "height": 600},
    "position": {"x": 100, "y": 100}
  }
}
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `always_on_top` | boolean | ⚠️ | Keep window on top |
| `transparent` | boolean | ⚠️ | Transparent background |
| `click_through` | boolean | ⚠️ | Allow clicks to pass through |
| `size` | object | ⚠️ | Window size {width, height} |
| `position` | object | ⚠️ | Window position {x, y} |

---

### 5. Set Auto-Blink

Configure automatic blinking.

**Command:**
```json
{
  "type": "set_auto_blink",
  "data": {
    "enabled": true,
    "min_interval": 2.0,
    "max_interval": 6.0,
    "blink_duration": 0.15
  }
}
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `enabled` | boolean | ✅ | Enable/disable auto-blink |
| `min_interval` | float | ⚠️ | Min seconds between blinks, default: 2.0 |
| `max_interval` | float | ⚠️ | Max seconds between blinks, default: 6.0 |
| `blink_duration` | float | ⚠️ | Blink duration in seconds, default: 0.15 |

---

### 6. Manual Blink

Trigger a blink manually.

**Command:**
```json
{
  "type": "blink",
  "data": {
    "duration": 0.15
  }
}
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `duration` | float | ⚠️ | Blink duration, default: 0.15 |

---

### 7. Shut Down Unity

Gracefully shut down Unity.

**Command:**
```json
{
  "type": "shutdown",
  "data": {}
}
```

**Response:**
```json
{
  "type": "shutdown_confirm",
  "data": {
    "message": "Unity shutting down"
  }
}
```

---

## Unity → Python Commands

### 1. Ready Signal

Unity sends when initialized and ready.

**Message:**
```json
{
  "type": "ready",
  "data": {
    "unity_version": "2022.3.15f1",
    "vrm_support": true
  }
}
```

---

### 2. VRM Loaded Confirmation

Sent after VRM successfully loads.

**Message:**
```json
{
  "type": "vrm_loaded",
  "data": {
    "success": true,
    "model_name": "Mura Mura",
    "blendshapes": ["Joy", "Angry", "Sorrow"],
    "bone_count": 55
  }
}
```

---

### 3. Expression Changed

Sent when expression changes.

**Message:**
```json
{
  "type": "expression_changed",
  "data": {
    "expression": "Joy",
    "weight": 1.0
  }
}
```

---

### 4. Status Update

Periodic status updates.

**Message:**
```json
{
  "type": "status",
  "data": {
    "fps": 60,
    "memory_mb": 512,
    "uptime_seconds": 3600
  }
}
```

---

### 5. Error Message

Sent when errors occur.

**Message:**
```json
{
  "type": "error",
  "data": {
    "command": "load_vrm",
    "message": "File not found",
    "code": "ERR_VRM_001",
    "severity": "error"
  }
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| `ERR_VRM_001` | VRM file not found |
| `ERR_VRM_002` | Invalid VRM format |
| `ERR_VRM_003` | VRM loading failed |
| `ERR_EXP_001` | Invalid expression name |
| `ERR_EXP_002` | Expression transition failed |
| `ERR_WIN_001` | Window operation failed |
| `ERR_CONN_001` | Connection lost |

---

## 🧵 Threading Considerations

### Python Side
```python
import threading
import queue

# Message queue for thread-safe communication
message_queue = queue.Queue()

def ipc_listener_thread():
    """Background thread for receiving messages"""
    while running:
        data = conn.recv(4096)
        message = json.loads(data.decode())
        message_queue.put(message)

def main_loop():
    """Main thread processes messages"""
    while True:
        if not message_queue.empty():
            message = message_queue.get()
            handle_message(message)
```

### Unity Side (C#)
```csharp
using System.Threading;
using System.Collections.Concurrent;

// Thread-safe queue
private ConcurrentQueue<string> messageQueue = new ConcurrentQueue<string>();

// Background thread for receiving
void ListenerThread() {
    while (running) {
        byte[] buffer = new byte[4096];
        int bytes = stream.Read(buffer, 0, buffer.Length);
        string message = Encoding.UTF8.GetString(buffer, 0, bytes);
        messageQueue.Enqueue(message);
    }
}

// Unity Update() on main thread
void Update() {
    if (messageQueue.TryDequeue(out string message)) {
        ProcessMessage(message);
    }
}
```

**⚠️ CRITICAL:** Unity API calls MUST happen on the main thread!

---

## 📚 Code Examples

### Python: Send Expression Command
```python
import socket
import json

def send_expression(expression, weight=1.0, duration=1.0):
    message = {
        "type": "set_expression",
        "data": {
            "expression": expression,
            "weight": weight,
            "duration": duration
        }
    }

    json_data = json.dumps(message)
    conn.sendall(json_data.encode())

# Usage
send_expression("Joy", weight=1.0, duration=2.0)
```

### Unity: Receive and Process
```csharp
using UnityEngine;
using Newtonsoft.Json.Linq;

void ProcessMessage(string jsonMessage) {
    JObject message = JObject.Parse(jsonMessage);
    string type = message["type"].ToString();

    switch (type) {
        case "set_expression":
            string expr = message["data"]["expression"].ToString();
            float weight = (float)message["data"]["weight"];
            float duration = (float)message["data"]["duration"];
            SetExpression(expr, weight, duration);
            break;

        case "load_vrm":
            string path = message["data"]["path"].ToString();
            LoadVRM(path);
            break;
    }
}
```

---

## 🔒 Security

### Port Security
- Server binds to `127.0.0.1` (localhost only)
- No external network access
- Firewall not required

### Message Validation
```python
def validate_message(message):
    """Validate incoming message"""
    required_fields = ["type", "data"]

    # Check required fields
    for field in required_fields:
        if field not in message:
            raise ValueError(f"Missing field: {field}")

    # Validate type
    if not isinstance(message["type"], str):
        raise ValueError("Invalid type field")

    # Validate data
    if not isinstance(message["data"], dict):
        raise ValueError("Invalid data field")

    return True
```

---

## 🐛 Error Handling

### Python Side
```python
def send_message(message):
    try:
        json_data = json.dumps(message)
        conn.sendall(json_data.encode())
    except BrokenPipeError:
        print("Connection lost")
        reconnect()
    except Exception as e:
        print(f"Send error: {e}")
```

### Unity Side
```csharp
try {
    JObject message = JObject.Parse(jsonMessage);
    ProcessMessage(message);
}
catch (JsonException e) {
    Debug.LogError($"JSON parse error: {e.Message}");
}
catch (Exception e) {
    Debug.LogError($"Processing error: {e.Message}");
}
```

---

## 📊 Performance Tips

1. **Batch messages** when possible
2. **Use asynchronous I/O** for large transfers
3. **Limit message size** to <10KB for fast processing
4. **Throttle status updates** to 1-2 per second
5. **Use message queues** for thread safety

---

## 🔮 Future API Extensions

Planned additions:
- 🔜 Audio playback commands
- 🔜 Lip sync data streaming
- 🔜 Animation clip triggers
- 🔜 Custom shader parameters
- 🔜 Plugin API endpoints

---

**Last updated:** November 13, 2025

**[← Back to Documentation](README.md)** | **[View Features →](FEATURES.md)**
