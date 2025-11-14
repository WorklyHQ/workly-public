# Workly — Public Edition

<div align="center">

<img src="assets/logo/workly_logo.png" alt="Workly Logo" width="200">

**Your AI-Powered Virtual Assistant with VRM Avatar**

[![License](https://img.shields.io/badge/License-Proprietary-orange.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&logoColor=white)](https://discord.gg/3Cpyxg29B4)
[![Version](https://img.shields.io/badge/Version-0.8.0--alpha-green.svg)](CHANGELOG.md)

• [📚 Documentation](https://github.com/WorklyHQ/workly-docs) • [💬 Discord](https://discord.gg/3Cpyxg29B4) • [🧪 Demos](demos/README.md)

![Demo GIF](screenshots/main_interface.png)

</div>

---

## 🌟 About Workly

**Workly Desktop** is an advanced AI-powered virtual assistant that lives on your Windows desktop. Featuring a fully customizable **VRM 3D avatar**, Workly combines cutting-edge AI technology with emotional intelligence and personality to create a truly interactive companion.

This repository showcases the **public edition** of Workly Desktop — a demonstration of the technologies, architecture, and capabilities that power the full commercial version available on Steam.

> ⚠️ **Note:** This is a showcase repository. The full source code is proprietary. The demos here are simplified examples for educational purposes.

---

## ✨ Key Features

### 🤖 Advanced AI Capabilities
- **Local LLM Integration** — Runs Llama 3.2, Mistral, Zephyr models locally
- **Conversation Memory** — SQLite-based long-term memory system
- **Context Awareness** — Remembers previous conversations and preferences
- **Customizable Personality** — Adjust tone, style, and behavior

### 🎭 VRM Avatar System
- **VRM Model Support** — Load custom VRM avatars (VRoid, VSeeFace compatible)
- **Facial Expressions** — Dynamic blendshape-based emotions (Joy, Anger, Sorrow, Fun, etc.)
- **Smooth Animations** — Transition between expressions with configurable timing
- **Auto-Blink System** — Realistic eye blinking with randomized intervals

### 🎤 Audio & Voice (Coming Soon)
- **Text-to-Speech** — Natural voice synthesis
- **Lip Sync** — Automatic mouth movement synced to speech
- **Audio Processing** — Real-time audio analysis and response

### 🔗 Discord Integration
- **Bot Commands** — Control Workly from Discord
- **Server Management** — Automated moderation and responses
- **Custom Commands** — Create your own bot interactions

### 🖥️ Desktop Integration
- **Always-on-Top** — Avatar stays visible while you work
- **Transparent Window** — Seamless desktop integration
- **Click-Through Mode** — Interact with desktop through the avatar
- **Multi-Monitor Support** — Works across multiple displays

---

## 🛠️ Tech Stack

### Frontend & Rendering
- **Unity 2022.3 LTS** — 3D rendering engine
- **UniVRM** — VRM model loading and manipulation
- **Universal Render Pipeline (URP)** — Modern rendering pipeline

### Backend & Logic
- **Python 3.11+** — Core application logic
- **PySide6 (Qt)** — GUI framework
- **llama-cpp-python** — Local LLM inference
- **SQLite** — Database for memory and configuration

### Communication
- **TCP Sockets** — IPC between Python and Unity
- **JSON Protocol** — Structured message format
- **Threading** — Async processing for responsiveness

### AI & NLP
- **Llama 3.2** — Primary language model
- **Mistral 7B** — Alternative model option
- **Zephyr 7B** — Specialized assistant model

---

## 📦 Demos

This repository contains **4 working demos** that showcase different aspects of Workly:

### 1. [Basic AI Chatbot](demos/01_basic_chatbot/)
Simple console-based chatbot using llama-cpp-python.
```bash
cd demos/01_basic_chatbot
pip install -r requirements.txt
python main.py
```

### 2. [VRM Avatar Loading](demos/02_vrm_avatar/)
Example of loading and displaying VRM metadata.
```bash
cd demos/02_vrm_avatar
python load_vrm.py
```

### 3. [Discord Integration](demos/03_discord_integration/)
Basic Discord bot with AI responses.
```bash
cd demos/03_discord_integration
pip install -r requirements.txt
python bot.py
```

### 4. [Memory System](demos/04_memory_system/)
SQLite-based conversation memory demonstration.
```bash
cd demos/04_memory_system
python memory_demo.py
```

> 📖 **Full documentation** for each demo is available in their respective folders.

---

## 📸 Screenshots

<div align="center">

| Main Interface | VRM Avatar | Chat Example |
|:--------------:|:----------:|:------------:|
| ![Interface](screenshots/main_interface.png) | ![Avatar](screenshots/vrm_avatar.png) | ![Chat](screenshots/chat_example.png) |

| Discord Bot | Expression System | Settings Panel |
|:-----------:|:-----------------:|:--------------:|
| ![Discord](screenshots/discord_bot.png) | ![Expressions](screenshots/expressions.png) | ![Settings](screenshots/settings.png) |

</div>

---

## 🗺️ Roadmap

### ✅ Phase 1 — Core Foundation (Completed)
- [x] Python + Unity architecture
- [x] VRM model loading
- [x] Basic IPC communication
- [x] GUI interface

### ✅ Phase 2 — Avatar Intelligence (Completed)
- [x] Facial expression system
- [x] Animation transitions
- [x] Auto-blink system
- [x] Blendshape control

### 🚧 Phase 3 — Audio Integration (In Progress)
- [ ] Text-to-Speech (TTS)
- [ ] Lip sync animation
- [ ] Audio input processing
- [ ] Voice activity detection

### 🔜 Phase 4 — Advanced Features (Planned)
- [ ] Multi-language support
- [ ] Plugin system
- [ ] Custom avatar creator
- [ ] Cloud synchronization

### 🔜 Phase 5 — Commercial Release (Planned)
- [ ] Steam integration
- [ ] Achievement system
- [ ] Community features
- [ ] Premium models

> 📋 For detailed roadmap, see [ROADMAP.md](docs/ROADMAP.md)

---

## 📚 Documentation

- [📖 Features Overview](docs/FEATURES.md) — Complete feature list
- [🏗️ Architecture](docs/ARCHITECTURE.md) — Technical architecture details
- [❓ FAQ](docs/FAQ.md) — Frequently asked questions
- [🔌 API Reference](docs/API.md) — IPC protocol documentation
- [🗺️ Roadmap](docs/ROADMAP.md) — Future development plans

---

## 🤝 Contributing

While the core Workly Desktop code is proprietary, we welcome contributions to:

- 📝 Documentation improvements
- 🐛 Bug reports and feedback
- 💡 Feature suggestions
- 🌍 Translations
- 🎨 Community assets (VRM models, configs)

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

---

## 💬 Community

Join our growing community:

- 💬 [Discord Server](https://discord.gg/YOUR_DISCORD) — Chat, support, and updates
- 🐦 [Twitter/X](https://twitter.com/YOUR_TWITTER) — News and announcements
- 📧 [Email](mailto:contact@workly.app) — Business inquiries
- 🎮 [Steam Community](https://steamcommunity.com) — Reviews and discussions

---

## 📄 License

**Workly Desktop** is proprietary software.

Copyright (c) 2025 **WorklyHQ**. All rights reserved.

The demo code in this repository is provided for **educational and showcase purposes only**. You may:
- ✅ View and study the code
- ✅ Run demos locally for learning
- ✅ Reference in educational content

You may **NOT**:
- ❌ Use for commercial purposes
- ❌ Redistribute or sell
- ❌ Create derivative commercial products
- ❌ Copy into proprietary projects

For licensing inquiries, contact: **contact@workly.app**

See [LICENSE](LICENSE) for full terms.

---

## 🚀 Get Workly Desktop

Ready to experience the full version?

<div align="center">

### [🎮 **Get Workly on Steam** 🎮](https://store.steampowered.com)

**Available now for Windows 10/11**

![Steam Badge](https://img.shields.io/badge/Steam-Available-blue.svg?style=for-the-badge&logo=steam)

</div>

---

## 🙏 Credits & Acknowledgments

**Workly Desktop** is built on amazing open-source projects and community resources:

### Core Technologies
- **[UniVRM](https://github.com/vrm-c/UniVRM)** — VRM support in Unity
- **[llama.cpp](https://github.com/ggerganov/llama.cpp)** — Optimized LLM inference
- **[PySide6](https://doc.qt.io/qtforpython/)** — Python GUI framework
- **[Unity](https://unity.com/)** — 3D rendering engine

### Demo Assets
- **[AcidicDoll](https://acidicdollz.booth.pm/)** — "Mura Mura" VRM model (demo example)
  - License: Personal use only, no redistribution, attribution required
  - Download: [BOOTH](https://acidicdollz.booth.pm/items/4613390)

### Inspiration
- **[Desktop Mate (Steam)](https://store.steampowered.com/app/3301060/Desktop_Mate/)** — Original concept inspiration

---

## 🙏 Support

If you like Workly, please consider:

- ⭐ **Starring this repository**
- 🎮 **Purchasing on Steam**
- 💬 **Joining our Discord**
- 🐦 **Following on Twitter**
- 📝 **Writing a Steam review**

---

<div align="center">

**Made with ❤️ by [WorklyHQ](https://github.com/WorklyHQ)**

[Website](https://workly.xyon.site.elsites.fr) • [Discord](https://discord.gg)


</div>
