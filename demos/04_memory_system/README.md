# 🧠 Memory System Demo

Demonstrates Workly's SQLite-based conversation memory system for maintaining context across sessions.

## 📋 Overview

This demo shows:
- SQLite database for conversation storage
- Message history tracking
- Context retrieval
- Memory search capabilities

## 🛠️ Requirements

- Python 3.11+
- No external dependencies (uses SQLite from standard library)

## 📦 Installation

No installation required! Uses Python standard library.

## 🚀 Usage

Run the demo:
```bash
python memory_demo.py
```

Example session:
```
🧠 Workly Memory System Demo
════════════════════════════════════════

📊 Database: workly_memory.db

Available commands:
  - Type a message to save it
  - 'search <keyword>' to search messages
  - 'history' to view recent messages
  - 'stats' to see database statistics
  - 'clear' to clear all messages
  - 'quit' to exit

You: Hello Workly!
✅ Message saved (ID: 1)

You: I like Python programming
✅ Message saved (ID: 2)

You: search Python
🔍 Found 1 message(s):
  [2025-11-13 14:30:15] I like Python programming

You: history
📜 Recent messages (last 5):
  1. [2025-11-13 14:30:10] Hello Workly!
  2. [2025-11-13 14:30:15] I like Python programming

You: stats
📊 Database Statistics:
  Total messages: 2
  Database size: 8.2 KB
```

## ⚙️ How It Works

### Database Schema

```sql
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    role TEXT NOT NULL,
    message TEXT NOT NULL,
    session_id TEXT,
    metadata TEXT
);

CREATE INDEX idx_timestamp ON conversations(timestamp);
CREATE INDEX idx_role ON conversations(role);
CREATE INDEX idx_session ON conversations(session_id);
```

### Message Storage

```python
def save_message(role, message, session_id=None):
    cursor.execute("""
        INSERT INTO conversations (timestamp, role, message, session_id)
        VALUES (?, ?, ?, ?)
    """, (datetime.now(), role, message, session_id))
```

### Context Retrieval

```python
def get_recent_context(limit=10):
    cursor.execute("""
        SELECT role, message, timestamp
        FROM conversations
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
```

## 🔧 Technical Details

### Memory Architecture

```
User Input
    ↓
SQLite Storage
    ↓
Context Window (last N messages)
    ↓
AI Processing
    ↓
Response + Store
```

### Features

1. **Persistent Storage**
   - Messages saved across sessions
   - SQLite database file
   - Fast read/write operations

2. **Search Capabilities**
   - Full-text search
   - Keyword filtering
   - Date range queries

3. **Session Management**
   - Group messages by session
   - Track conversation threads
   - Isolate contexts

4. **Metadata Support**
   - Store additional information
   - JSON format
   - Extensible structure

## 📊 Performance

Typical performance metrics:
- **Write**: ~1,000 messages/sec
- **Read**: ~10,000 messages/sec
- **Search**: ~100ms for 10,000 messages
- **Database size**: ~1KB per message

## 🎯 Advanced Features (Full Workly)

The full Workly Desktop includes:

### Memory Management
- 🔄 **Automatic summarization** — Condense old conversations
- 🎯 **Relevance scoring** — Rank messages by importance
- 🗂️ **Topic clustering** — Group related conversations
- 🕒 **Time-based decay** — Older messages have less weight
- 💾 **Vector embeddings** — Semantic search capabilities

### Context Strategies
- **Sliding window** — Last N messages
- **Summary + recent** — Old summary + recent details
- **Relevance-based** — Most relevant to current topic
- **Hierarchical** — Important events + recent context

### Data Management
- 📦 **Export/import** — Backup conversations
- 🔒 **Encryption** — Secure sensitive data
- 🗜️ **Compression** — Reduce database size
- 🔄 **Sync** — Cloud backup (Workly Pro)

## 📝 Example Use Cases

### 1. Personal Assistant
```python
# Remember user preferences
save_message("system", "User prefers dark mode")
save_message("system", "User's favorite language is Python")

# Retrieve preferences later
preferences = search_messages("prefers")
```

### 2. Learning Assistant
```python
# Track topics discussed
save_message("user", "Explain Python decorators")
save_message("assistant", "Decorators are...")

# Review learning history
history = get_messages_by_date(date)
```

### 3. Task Tracking
```python
# Store tasks
save_message("user", "TODO: Finish documentation")
save_message("user", "TODO: Test memory system")

# Query pending tasks
tasks = search_messages("TODO")
```

## 🔗 Integration with AI

In the full Workly Desktop:

```python
# Get context for AI
context = get_recent_context(limit=10)

# Build prompt with context
prompt = build_prompt_with_context(context, user_message)

# Generate response
response = llm(prompt)

# Save both to memory
save_message("user", user_message)
save_message("assistant", response)
```

## 📚 Resources

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Full Documentation](../../docs/ARCHITECTURE.md)
- [API Reference](../../docs/API.md)

---

**Part of [Workly Public Edition](../../README.md)**
