# 📚 Demos Overview

This folder contains **4 working demonstrations** of Workly Desktop's core features.

## 🎯 Available Demos

### 1️⃣ Basic AI Chatbot
**Location:** `01_basic_chatbot/`

A simple console-based chatbot demonstrating local LLM integration.

**Features:**
- llama-cpp-python integration
- Simple conversation loop
- Model loading and configuration
- Basic prompt engineering

**Difficulty:** 🟢 Beginner

[📖 Demo Documentation](01_basic_chatbot/README.md)

---

### 2️⃣ VRM Avatar Loading
**Location:** `02_vrm_avatar/`

Example of loading and parsing VRM model metadata.

**Features:**
- VRM file structure
- Metadata extraction
- Blendshape information
- Model validation

**Difficulty:** 🟢 Beginner

[📖 Demo Documentation](02_vrm_avatar/README.md)

---

### 3️⃣ Discord Integration
**Location:** `03_discord_integration/`

Basic Discord bot with AI-powered responses.

**Features:**
- Discord.py bot setup
- Command handling
- AI response generation
- Server integration

**Difficulty:** 🟡 Intermediate

[📖 Demo Documentation](03_discord_integration/README.md)

---

### 4️⃣ Memory System
**Location:** `04_memory_system/`

SQLite-based conversation memory demonstration.

**Features:**
- Database setup
- Conversation storage
- Context retrieval
- Memory management

**Difficulty:** 🟡 Intermediate

[📖 Demo Documentation](04_memory_system/README.md)

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+** installed
- **pip** package manager
- **Windows 10/11** (recommended, demos may work on other OS)
- **Basic command line knowledge**

### Running a Demo

1. **Navigate to demo folder:**
   ```bash
   cd demos/01_basic_chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the demo:**
   ```bash
   python main.py
   ```

4. **Follow on-screen instructions**

Each demo includes its own README with detailed setup and usage instructions.

---

## 📋 Demo Comparison

| Demo | Complexity | Dependencies | Runtime | Output |
|------|------------|--------------|---------|--------|
| **01 - Chatbot** | 🟢 Beginner | llama-cpp-python | ~5-10 min | Console text |
| **02 - VRM** | 🟢 Beginner | None (stdlib) | < 1 min | Console text |
| **03 - Discord** | 🟡 Intermediate | discord.py, llama-cpp | Continuous | Discord messages |
| **04 - Memory** | 🟡 Intermediate | None (stdlib) | ~1-2 min | Console + SQLite |

---

## 💡 Learning Path

### For Beginners
1. Start with **Demo 2 (VRM Loading)** - No dependencies, quick results
2. Try **Demo 1 (Chatbot)** - Learn about LLM integration
3. Experiment with **Demo 4 (Memory)** - Understand data persistence

### For Intermediate Users
1. Jump to **Demo 3 (Discord)** - Real-world integration
2. Combine concepts from multiple demos
3. Create your own variations

### For Advanced Users
- Modify demos to add features
- Combine demos into larger projects
- Contribute improvements back to the repo

---

## 🎓 What You'll Learn

### Demo 1 - Basic AI Chatbot
- Local LLM setup
- Model loading and configuration
- Prompt engineering basics
- Conversation loop implementation
- Error handling

### Demo 2 - VRM Avatar Loading
- VRM file format
- Metadata parsing
- Blendshape names and usage
- Model validation
- File I/O in Python

### Demo 3 - Discord Integration
- Discord bot creation
- Command handling
- Async programming in Python
- Integrating AI with platforms
- Bot deployment basics

### Demo 4 - Memory System
- SQLite database basics
- Conversation persistence
- Context management
- Data retrieval and search
- Memory optimization

---

## 🔧 Troubleshooting

### Common Issues

#### "Module not found" error
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

#### "Model file not found" (Demo 1, 3)
**Solution:** Download a model or update path in code
```python
model_path = "path/to/your/model.gguf"
```

#### "Permission denied" on database (Demo 4)
**Solution:** Run with appropriate permissions or change database location

#### Discord bot not responding (Demo 3)
**Solution:** Check bot token, ensure bot has proper permissions in server

### Getting Help

- 📖 Check demo-specific README
- 💬 Ask in [Discord](https://discord.gg)
- 🐛 [Report issue](https://github.com/WorklyHQ/workly-public/issues)
- 📧 Email: support@workly.app

---

## 🤝 Contributing

Want to improve the demos or add new ones?

### Improvement Ideas
- Add better error handling
- Improve code comments
- Add more examples
- Create variations
- Fix bugs

### New Demo Ideas
- Audio processing demo
- Expression control demo
- Unity communication demo
- Configuration management demo
- Performance monitoring demo

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

## ⚠️ Important Notes

### These are Demonstrations
- **Simplified code** for educational purposes
- **Not production-ready** - missing advanced features
- **Security considerations** not fully implemented
- **Error handling** is basic

### Full Workly Desktop
The commercial version on Steam includes:
- ✅ Advanced error handling
- ✅ Production-ready code
- ✅ Full Unity integration
- ✅ Advanced AI features
- ✅ Complete UI/UX
- ✅ Performance optimizations
- ✅ Ongoing support and updates

[🎮 Get Workly Desktop on Steam](https://store.steampowered.com)

---

## 📄 License

Demo code is provided under the proprietary license of this repository.

**You may:**
- ✅ Study and learn from the code
- ✅ Run locally for educational purposes
- ✅ Reference in educational content

**You may NOT:**
- ❌ Use commercially
- ❌ Redistribute
- ❌ Create commercial derivatives

See [LICENSE](../LICENSE) for full terms.

---

## 🔗 Related Resources

### Documentation
- [Main README](../README.md)
- [Features Overview](../docs/FEATURES.md)
- [Architecture](../docs/ARCHITECTURE.md)
- [API Reference](../docs/API.md)

### External
- [llama.cpp](https://github.com/ggerganov/llama.cpp) - LLM inference
- [VRM Specification](https://github.com/vrm-c/vrm-specification) - VRM format
- [Discord.py](https://discordpy.readthedocs.io/) - Discord bot library

---

**Happy learning!** 🎓✨

Enjoy exploring Workly's capabilities through these demos!
