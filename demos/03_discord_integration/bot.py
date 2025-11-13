"""
Discord Integration Demo - Workly Public Edition

Demonstrates basic Discord bot with optional AI responses.
This is a simplified version for educational purposes.

Author: WorklyHQ
License: See LICENSE file
"""

import json
import os
from pathlib import Path

try:
    import discord
    from discord.ext import commands
except ImportError:
    print("❌ Error: discord.py not installed")
    print("📦 Install with: pip install discord.py")
    exit(1)


def load_config():
    """Load bot configuration"""
    config_path = Path(__file__).parent / "config.json"

    if not config_path.exists():
        print("❌ config.json not found!")
        print(
            "📝 Please copy config_example.json to config.json and add your bot token"
        )
        exit(1)

    with open(config_path, "r") as f:
        config = json.load(f)

    if config.get("discord_token") == "YOUR_BOT_TOKEN_HERE":
        print("❌ Discord token not configured!")
        print("📝 Please add your bot token to config.json")
        print("🔗 Get a token: https://discord.com/developers/applications")
        exit(1)

    return config


def load_ai_model(config):
    """Load AI model if enabled"""
    if not config.get("use_ai", False):
        return None

    model_path = config.get("model_path")

    if not model_path or not os.path.exists(model_path):
        print("⚠️ AI model not found, using simple responses")
        return None

    try:
        from llama_cpp import Llama

        print(f"📦 Loading AI model: {model_path}")
        llm = Llama(model_path=model_path, n_ctx=2048, n_threads=4, verbose=False)
        print("✅ AI model loaded!")
        return llm

    except ImportError:
        print("⚠️ llama-cpp-python not installed, using simple responses")
        return None

    except Exception as e:
        print(f"⚠️ Error loading AI model: {e}")
        return None


def generate_ai_response(llm, question, config):
    """Generate AI-powered response"""
    if llm is None:
        return None

    try:
        prompt = f"User: {question}\nAssistant:"

        response = llm(
            prompt,
            max_tokens=config.get("max_tokens", 256),
            temperature=0.7,
            stop=["User:", "\n\n"],
            echo=False,
        )

        return response["choices"][0]["text"].strip()

    except Exception as e:
        print(f"❌ AI generation error: {e}")
        return None


def get_simple_response(question):
    """Get predefined response (fallback when AI is disabled)"""
    question_lower = question.lower()

    responses = {
        "hello": "Hello! 👋 I'm Workly, your AI assistant. How can I help you today?",
        "hi": "Hi there! 😊",
        "how are you": "I'm doing great! Thanks for asking. How can I help you?",
        "who are you": "I'm Workly, an AI-powered virtual assistant created by WorklyHQ!",
        "help": "You can ask me questions or chat with me! Try: !workly hello",
        "thanks": "You're welcome! 😊",
        "bye": "Goodbye! Come back anytime! 👋",
    }

    for keyword, response in responses.items():
        if keyword in question_lower:
            return response

    return "I'm a demo bot with limited responses. The full Workly has advanced AI! 🤖"


def main():
    """Main bot function"""
    print("=" * 60)
    print("🤖 Workly Discord Bot Demo")
    print("=" * 60)
    print()

    # Run diagnostics first
    print("🔍 Running pre-flight checks...\n")

    try:
        from diagnose import run_diagnostics

        if not run_diagnostics(silent=False):
            print("\n❌ Pre-flight checks FAILED!")
            print("📝 Please fix the issues above before starting the bot.")
            print("💡 Tip: Check SETUP_DISCORD_BOT.md for detailed instructions.\n")
            return

        print("\n✅ Pre-flight checks PASSED!")
        print("🚀 Starting bot...\n")

    except ImportError:
        print("⚠️  Warning: Could not run diagnostics (diagnose.py not found)")
        print("🚀 Starting bot anyway...\n")

    # Load configuration
    config = load_config()

    # Setup bot
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(
        command_prefix=config.get("command_prefix", "!workly "),
        intents=intents,
        help_command=None,
    )

    # Load AI model
    llm = load_ai_model(config)

    @bot.event
    async def on_ready():
        """Bot startup event"""
        print(f"✅ Bot connected as {bot.user}")
        print(f"📊 Serving {len(bot.guilds)} server(s)")
        print(f"🤖 AI Mode: {'Enabled' if llm else 'Simple responses'}")
        print("\n🎉 Bot is ready!\n")

    @bot.command(name="hello")
    async def hello(ctx):
        """Greet command"""
        await ctx.send("Hello! 👋 I'm Workly, your AI assistant!")

    @bot.command(name="ask")
    async def ask(ctx, *, question):
        """Ask a question"""
        async with ctx.typing():
            # Try AI response first
            if llm:
                response = generate_ai_response(llm, question, config)
                if response:
                    await ctx.send(response)
                    return

            # Fallback to simple response
            response = get_simple_response(question)
            await ctx.send(response)

    @bot.command(name="joke")
    async def joke(ctx):
        """Tell a joke"""
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the Python programmer go broke? Because he used up all his cache! 💰",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
        ]
        import random

        await ctx.send(random.choice(jokes))

    @bot.command(name="ping")
    async def ping(ctx):
        """Check bot latency"""
        latency = round(bot.latency * 1000)
        await ctx.send(f"🏓 Pong! Latency: {latency}ms")

    @bot.command(name="help")
    async def help_command(ctx):
        """Show help"""
        prefix = config.get("command_prefix", "!workly ")

        embed = discord.Embed(
            title="🤖 Workly Bot Commands",
            description="Here are the available commands:",
            color=discord.Color.blue(),
        )

        embed.add_field(name=f"{prefix}hello", value="Greet the bot", inline=False)
        embed.add_field(
            name=f"{prefix}ask <question>", value="Ask a question", inline=False
        )
        embed.add_field(name=f"{prefix}joke", value="Get a random joke", inline=False)
        embed.add_field(name=f"{prefix}ping", value="Check bot latency", inline=False)

        embed.set_footer(text="Workly Public Edition • WorklyHQ")

        await ctx.send(embed=embed)

    @bot.event
    async def on_command_error(ctx, error):
        """Handle command errors"""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(
                "❌ Command not found. Use `!help` to see available commands."
            )
        else:
            await ctx.send(f"❌ Error: {error}")
            print(f"Error: {error}")

    # Run bot
    print("⏸️  Press Ctrl+C to stop\n")

    try:
        bot.run(config["discord_token"])
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
