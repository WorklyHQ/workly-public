# ❓ Workly Desktop — FAQ

Frequently Asked Questions

## 📦 General Questions

### What is Workly Desktop?

**Workly Desktop** is an AI-powered virtual assistant that lives on your Windows desktop. It features a customizable 3D VRM avatar that can express emotions, have natural conversations, and assist you with various tasks. All AI processing happens locally on your computer—no cloud required.

### Is Workly free?

The full version of **Workly Desktop** is a **paid commercial product** available on Steam. This public repository contains demo code and documentation for educational and showcase purposes only.

### What makes Workly different from other AI assistants?

- ✅ **100% Local** — All AI runs on your computer, no data sent to cloud
- ✅ **VRM Avatar** — Visible 3D character with expressions and animations
- ✅ **Desktop Integration** — Always visible while you work
- ✅ **Customizable** — Use your own VRM models and AI models
- ✅ **Privacy-First** — Your conversations stay on your machine

---

## 💻 System & Compatibility

### What are the system requirements?

**Minimum:**
- Windows 10 64-bit
- Intel Core i5 or equivalent
- 8GB RAM
- DirectX 11 compatible GPU
- 5GB free storage

**Recommended:**
- Windows 11 64-bit
- Intel Core i7 / AMD Ryzen 7
- 16GB RAM
- NVIDIA GTX 1060 or better (for GPU acceleration)
- 10GB SSD storage

### Does it work on Mac or Linux?

Currently, **Workly Desktop is Windows-only**. Mac and Linux support would require rebuilding the Unity components for those platforms, which is being considered for future releases based on demand.

### Can I run it without a GPU?

**Yes!** Workly can run on CPU-only systems. However, AI response times will be slower compared to GPU-accelerated systems. We recommend:
- **CPU-only**: Use small models (1B-3B parameters)
- **With GPU**: Can use larger models (7B-13B parameters)

### How much disk space does it need?

- **Application**: ~1GB
- **AI Models**: 2-10GB (depends on model size)
- **VRM Models**: 10-100MB each
- **Database**: Grows over time (typically <100MB)

**Total:** Plan for 5-15GB depending on your setup.

---

## 🤖 AI & Models

### What AI models does Workly support?

Workly supports any **GGUF format** models, including:
- Llama 3.2 (1B, 3B)
- Mistral 7B
- Zephyr 7B
- Phi-3
- Custom fine-tuned models

### Where do I get AI models?

Download from [Hugging Face](https://huggingface.co/models?search=gguf):
- Search for "gguf" + model name
- Download the quantized version (Q4, Q5, or Q8)
- Place in `models/` folder

### Does Workly require an internet connection?

**No!** Once you've downloaded:
- The Workly application
- Your AI model (GGUF file)
- Your VRM avatar

...you can use Workly **completely offline**. Your conversations never leave your computer.

### How do I improve AI response quality?

1. **Use a larger model** — 7B models are smarter than 1B
2. **Adjust temperature** — Lower (0.3-0.5) = consistent, Higher (0.7-0.9) = creative
3. **Provide better prompts** — Be specific and clear
4. **Use more context** — Increase context window size

### Can I use ChatGPT / Claude instead of local models?

Not currently. Workly is designed for **local-only processing** to prioritize privacy. However, API integration with cloud providers is being considered as an **optional feature** in future updates.

---

## 🎭 VRM Avatars

### What is a VRM model?

**VRM** is a 3D avatar format designed for VR/VTuber applications. It's based on glTF and includes:
- 3D mesh and textures
- Bones and rigging
- Facial expressions (blendshapes)
- License and usage information

### Where can I get VRM models?

**Free sources:**
- [VRoid Hub](https://hub.vroid.com) — Thousands of free models
- [VRoid Studio](https://vroid.com/studio) — Create your own
- [Booth.pm](https://booth.pm) — Free and paid models

**Paid sources:**
- Commission artists on Twitter, Fiverr, etc.
- Premium models on Booth.pm
- Custom character creators

### Can I use my own VRM avatar?

**Yes!** Workly supports:
- ✅ VRM 0.0 format
- ✅ VRM 1.0 format
- ✅ Models from VRoid Studio
- ✅ Custom-made VRM models

Just load your `.vrm` file in the settings.

### My VRM model doesn't load. Why?

Common issues:
- ❌ **Not a VRM file** — Must be `.vrm` format, not `.fbx` or `.blend`
- ❌ **Corrupted file** — Try re-downloading
- ❌ **Too many polygons** — Very high-poly models may crash Unity
- ❌ **Missing textures** — VRM should be self-contained

**Solution:** Try a different VRM from VRoid Hub to test.

### Can I create expressions for custom VRM models?

**Yes**, but the VRM must have blendshapes defined. Models from VRoid Studio automatically include standard expressions (Joy, Angry, Sorrow, Fun, etc.). Custom models need proper blendshape setup in Blender or Unity.

---

## ⚙️ Configuration & Settings

### Where are settings stored?

Settings are stored in:
- **Config file**: `config.json` in the app directory
- **Database**: `data/database.db` for conversations
- **Logs**: `logs/` folder for debugging

### How do I reset to default settings?

1. Close Workly completely
2. Delete or rename `config.json`
3. Restart Workly — it will create a new default config

### Can I backup my conversations?

**Yes!** Your conversations are in `data/database.db`. You can:
- Copy the file for backup
- Use SQLite browser to export
- (Planned) In-app export feature

### Does Workly collect any data?

**NO.** Workly:
- ❌ Does not send data to servers
- ❌ Does not track usage
- ❌ Does not include telemetry
- ❌ Does not require accounts

Your privacy is guaranteed.

---

## 💬 Discord Integration

### How do I use Workly as a Discord bot?

1. Create a Discord bot at [Discord Developer Portal](https://discord.com/developers)
2. Copy the bot token
3. Configure in Workly settings
4. Invite bot to your server
5. Use commands like `!workly ask <question>`

See [Discord Demo](../demos/03_discord_integration/) for details.

### Can Workly respond in multiple Discord servers?

**Yes!** One Workly instance can serve multiple Discord servers simultaneously. Each server can have its own configuration (coming in future updates).

### Does Discord integration require Workly to be running?

**Yes.** Workly must be running on your computer for the Discord bot to work. It's not a cloud-hosted bot—it runs locally.

---

## 🐛 Troubleshooting

### Workly won't start / crashes immediately

**Try:**
1. Check `logs/` folder for error messages
2. Verify system requirements
3. Update graphics drivers
4. Run as administrator
5. Reinstall Workly

### Unity window is blank / black screen

**Causes:**
- Graphics driver issues
- Incompatible GPU
- Corrupted Unity build

**Solutions:**
- Update graphics drivers
- Try running in windowed mode
- Check DirectX compatibility
- Reinstall application

### AI responses are very slow

**Normal if:**
- Running on CPU only (expected: 1-5 tokens/sec)
- Using large models (7B+) without GPU

**Speed up:**
- Use smaller quantized models (Q4)
- Enable GPU acceleration (CUDA)
- Use smaller model (1B-3B parameters)
- Close other applications

### High CPU/GPU usage

**Expected behavior:**
- Unity rendering = GPU usage
- AI inference = CPU/GPU usage

**Reduce usage:**
- Enable "Background throttling" in settings
- Lower FPS limit
- Use smaller models
- Minimize Unity window when not in use

### "Model not found" error

**Causes:**
- Model path incorrect in config
- Model file missing or renamed
- Unsupported model format

**Solutions:**
- Verify model path in `config.json`
- Ensure file ends with `.gguf`
- Re-download model if corrupted
- Use absolute file path

---

## 🔒 Privacy & Security

### Is my data safe?

**Yes.** Everything runs locally:
- AI models on your computer
- Database on your hard drive
- No data sent to external servers
- No cloud dependency

### Can others see my conversations?

**No**, unless:
- They have physical access to your computer
- They access your `database.db` file

Keep your computer secure with:
- User account password
- Disk encryption (BitLocker)
- Regular backups

### Can Workly access my files?

Workly only accesses:
- ✅ Its own application folder
- ✅ User-selected VRM files
- ✅ User-selected model files
- ✅ Standard app data directories

It does **NOT**:
- ❌ Scan your hard drive
- ❌ Access browser history
- ❌ Read other apps' data
- ❌ Require administrator rights (normally)

---

## 💰 Pricing & Licensing

### How much does Workly cost?

**Workly Desktop** will be available on Steam with the following pricing (subject to change):
- **Standard Edition**: $19.99 (one-time purchase)
- **Pro Edition**: $4.99/month or $49.99/year (subscription)

### What's included in Standard vs Pro?

**Standard Edition:**
- ✅ Full desktop application
- ✅ Unlimited local AI
- ✅ VRM avatar support
- ✅ Discord integration
- ✅ Local memory system

**Pro Edition** (additional features):
- ✅ Everything in Standard
- ✅ Cloud backup (optional, encrypted)
- ✅ Priority support
- ✅ Early access to new features
- ✅ Premium AI models
- ✅ Advanced analytics

### Is there a free trial?

A **free demo version** with limited features will be available on Steam. The full version offers a **14-day refund policy** through Steam.

### Can I use Workly commercially?

**Standard license:** Personal use only
**Commercial license:** Contact sales@workly.app for pricing

---

## 🚀 Updates & Support

### How do I update Workly?

- **Steam version:** Updates automatically through Steam
- **Standalone version:** Download latest from website

### Where do I get support?

- 💬 **Discord**: https://discord.gg/YOUR_DISCORD (fastest)
- 📧 **Email**: support@workly.app
- 🐛 **Bug reports**: GitHub issues
- 📚 **Documentation**: This repository

### How do I report bugs?

1. Check [existing issues](https://github.com/WorklyHQ/workly-public/issues)
2. If new bug, create issue with:
   - Description of problem
   - Steps to reproduce
   - System information
   - Log files (from `logs/` folder)

### Can I request features?

**Yes!** We love feature requests:
1. Check [existing discussions](https://github.com/WorklyHQ/workly-public/discussions)
2. Create new discussion if not exists
3. Explain your use case
4. Community can vote on requests

---

## 📚 Development

### Can I contribute to Workly?

The core Workly Desktop is **proprietary**, but you can contribute:
- 📝 Documentation improvements
- 🐛 Bug reports
- 💡 Feature suggestions
- 🌍 Translations
- 🎨 Community assets (VRM models, configs)

### Is the source code available?

**No.** Workly Desktop is **proprietary commercial software**. This repository contains:
- ✅ Demo code (simplified examples)
- ✅ Documentation
- ✅ API specifications
- ❌ Full source code (not included)

### Can I build plugins for Workly?

A **plugin system** is planned for future releases (Phase 4). It will allow:
- Custom commands
- UI extensions
- Integration with other apps
- Community-created features

---

## 🤔 Other Questions

### Does Workly support multiple languages?

Currently **English only**. Multi-language support is planned for Phase 4:
- UI translations
- Multi-language AI models
- Auto language detection

### Can I use Workly for VTubing?

**Not officially**, but it's on the roadmap! "VTuber mode" is a highly-requested feature that would add:
- OBS virtual camera integration
- Face/body tracking
- Real-time mouth movement
- Screen recording

### Will there be a mobile version?

A **mobile companion app** is being considered for 2026+. It would allow:
- View conversations on phone
- Basic chat interface
- Remote control of desktop app
- Sync (optional, cloud-based)

### Question not answered here?

- 💬 Ask in our [Discord](https://discord.gg/YOUR_DISCORD)
- 📧 Email: support@workly.app
- 🔍 Search [GitHub Discussions](https://github.com/WorklyHQ/workly-public/discussions)

---

**Last updated:** November 13, 2025

**[← Back to Documentation](README.md)** | **[View API →](API.md)**
