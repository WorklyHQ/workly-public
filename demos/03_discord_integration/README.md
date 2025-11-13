# 💬 Discord Integration Demo

Demonstrates how Workly integrates with Discord to create an AI-powered bot.

## 📋 Overview

This demo shows:
- Basic Discord bot setup
- AI-powered responses using local LLM
- Command handling
- Message processing

## 🛠️ Requirements

- Python 3.11+
- Discord Bot Token (create at https://discord.com/developers)
- A GGUF model file (optional, will work without)

## 📦 Installation

### Option 1 : Installation Rapide

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure le bot :
   - Copy `config_example.json` to `config.json`
   - Ajoute ton Discord bot token
   - (Optional) Ajoute le chemin vers ton modèle GGUF

3. Lance le bot :
```bash
python bot.py
```

### Option 2 : Guide Complet Pas-à-Pas

**👉 Si c'est ta première fois avec un bot Discord, suis ce guide :**

📖 **[SETUP_DISCORD_BOT.md](SETUP_DISCORD_BOT.md)** — Guide détaillé de A à Z

Ce guide t'explique :
- Comment créer une application Discord
- Comment obtenir ton token
- ⚠️ **Comment activer Message Content Intent** (CRITIQUE !)
- Comment inviter le bot sur ton serveur
- Comment résoudre les problèmes courants

### Option 3 : Script de Diagnostic

**👉 Si ton bot ne fonctionne pas, lance le diagnostic :**

```bash
python diagnose.py
```

Ce script vérifie :
- ✅ Fichier `config.json` valide
- ✅ Token Discord configuré
- ✅ Dépendances installées
- ✅ Modèle AI (optionnel)
- ⚠️ Rappel pour activer Message Content Intent

## 🚀 Usage

Run the bot:
```bash
python bot.py
```

### ⚠️ IMPORTANT: How to Use Commands

**Le bot utilise le préfixe `!workly ` (avec un espace après !)**

Tu DOIS taper `!workly` suivi d'un **espace**, puis la commande.

### ✅ Example Commands in Discord

```
You: !workly hello
Bot: Hello! 👋 I'm Workly, your AI assistant!

You: !workly ask what's 2+2?
Bot: 2 + 2 equals 4.

You: !workly joke
Bot: Why did the programmer quit his job? Because he didn't get arrays!

You: !workly help
Bot: Shows available commands with embed
```

### ❌ Common Mistakes

```
❌ hello                    # Won't work - missing prefix
❌ !hello                   # Won't work - missing "workly"
❌ !workly:hello            # Won't work - use space, not colon
❌ !worklyhello             # Won't work - missing space after "workly"
✅ !workly hello            # CORRECT ✨
```

## ⚙️ Configuration

Edit `config.json`:
```json
{
  "discord_token": "YOUR_BOT_TOKEN_HERE",
  "command_prefix": "!workly",
  "model_path": "model.gguf",
  "max_tokens": 256,
  "use_ai": true
}
```

Options:
- `discord_token`: Your Discord bot token
- `command_prefix`: Command prefix (e.g., `!workly`, `!w`)
- `model_path`: Path to GGUF model (optional)
- `max_tokens`: Maximum response length
- `use_ai`: Enable AI responses (false = simple responses)

## 🔧 Technical Details

### Bot Architecture

```
Discord Message
      ↓
  Bot Receives
      ↓
  Parse Command
      ↓
   AI Processing (optional)
      ↓
   Send Response
```

### Command System

Basic command structure:
```python
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello! 👋')
```

AI-powered responses:
```python
@bot.command(name='ask')
async def ask(ctx, *, question):
    response = generate_ai_response(question)
    await ctx.send(response)
```

## 📊 Features

### Without AI (Simple Mode)
- ✅ Predefined responses
- ✅ Command handling
- ✅ Fast response time
- ✅ Low resource usage

### With AI (Full Mode)
- ✅ Dynamic responses
- ✅ Context awareness
- ✅ Natural conversations
- ✅ Personality customization

## 🎯 Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `!workly hello` | Greet the bot | `!workly hello` |
| `!workly ask <question>` | Ask a question | `!workly ask what's Python?` |
| `!workly joke` | Get a joke | `!workly joke` |
| `!help` | Show help | `!help` |
| `!ping` | Check bot latency | `!ping` |

## 🐛 Troubleshooting

### Bot connects but doesn't respond

**✅ Vérifications :**

1. **Command prefix** — Assure-toi d'utiliser `!workly ` (avec espace)
   ```
   ✅ !workly hello
   ❌ !hello
   ❌ hello
   ```

2. **Bot permissions** — Le bot a besoin de ces permissions dans Discord :
   - `Send Messages`
   - `Read Message History`
   - `Use External Emojis` (optionnel)

3. **Developer Portal Intents** — Active **"Message Content Intent"** :
   - Va sur https://discord.com/developers/applications
   - Sélectionne ton bot
   - Onglet "Bot"
   - Section "Privileged Gateway Intents"
   - Active **"MESSAGE CONTENT INTENT"** ✅
   - Sauvegarde les changements

4. **Bot role position** — Le rôle du bot doit être plus haut que les rôles qu'il modère (si applicable)

### Common Errors

**"❌ Discord token not configured!"**
→ Tu dois ajouter ton token dans `config.json`

**"❌ Error: discord.py not installed"**
→ Exécute : `pip install discord.py`

**"401: Unauthorized"**
→ Token invalide. Vérifie ton token dans le Developer Portal et copie-le exactement.

**"403: Missing Permissions"**
→ Le bot n'a pas les permissions nécessaires sur le serveur Discord.

**Bot online mais ne répond jamais**
→ Vérifie que "MESSAGE CONTENT INTENT" est activé dans le Developer Portal.

### Testing Checklist

```
□ Bot token configuré dans config.json
□ discord.py installé (pip install discord.py)
□ Message Content Intent activé dans Developer Portal
□ Bot invité sur le serveur avec bonnes permissions
□ Bot apparaît "en ligne" dans Discord
□ Test avec : !workly hello
```

## 📝 Notes

This is a **simplified demo**. The full Workly Desktop Discord integration includes:

### Advanced Features
- 🧠 **Long-term memory** — Remembers previous conversations
- 🎭 **Personality modes** — Different bot personalities
- 🔄 **Context switching** — Handles multiple conversations
- 📊 **Analytics** — Usage statistics and insights
- 🛡️ **Moderation** — Auto-moderation features
- 🎨 **Embeds** — Rich message formatting
- 📎 **Attachments** — Image and file handling
- 🔔 **Event handling** — React to server events

### Enterprise Features (Workly Pro)
- 📈 Server analytics
- 🎯 Custom commands per server
- 🔒 Role-based permissions
- 📝 Custom responses database
- 🌐 Multi-language support

## 🔗 Resources

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/docs)
- [Discord Bot setup Help](./SETUP_DISCORD_BOT.md)

---

**Part of [Workly Public Edition](../../README.md)**
