"""
Discord Bot Diagnostic Tool

Helps diagnose common Discord bot issues.
Run this before launching the bot to check your configuration.
"""

import json
import os
from pathlib import Path


def print_header(title):
    """Print section header"""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


def print_status(check, passed, message=""):
    """Print check status"""
    icon = "✅" if passed else "❌"
    status = "PASS" if passed else "FAIL"
    print(f"{icon} [{status}] {check}")
    if message:
        print(f"   → {message}")


def check_config_file():
    """Check if config.json exists and is valid"""
    print_header("1️⃣  Configuration File Check")

    config_path = Path(__file__).parent / "config.json"

    if not config_path.exists():
        print_status(
            "config.json exists",
            False,
            "File not found! Copy config_example.json to config.json",
        )
        return None

    print_status("config.json exists", True)

    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        print_status("config.json is valid JSON", True)
        return config
    except json.JSONDecodeError as e:
        print_status("config.json is valid JSON", False, f"Parse error: {e}")
        return None


def check_discord_token(config):
    """Check Discord token configuration"""
    print_header("2️⃣  Discord Token Check")

    if not config:
        print_status("Token configuration", False, "config.json not loaded")
        return False

    token = config.get("discord_token", "")

    if not token:
        print_status("Token present", False, "discord_token field is empty")
        return False

    print_status("Token present", True)

    if token == "YOUR_BOT_TOKEN_HERE":
        print_status(
            "Token configured",
            False,
            "Still using placeholder value! Add your real token.",
        )
        return False

    print_status("Token configured", True)

    # Basic token format check
    if len(token) < 50:
        print_status(
            "Token format",
            False,
            "Token seems too short. Discord tokens are usually 59+ chars.",
        )
        return False

    print_status("Token format", True, "Token length looks valid")

    return True


def check_dependencies():
    """Check if required packages are installed"""
    print_header("3️⃣  Dependencies Check")

    # Check discord.py
    try:
        import discord

        print_status("discord.py installed", True, f"Version: {discord.__version__}")
    except ImportError:
        print_status(
            "discord.py installed", False, "Install with: pip install discord.py"
        )
        return False

    # Check llama-cpp-python (optional)
    try:
        import llama_cpp

        print_status("llama-cpp-python installed", True, "AI mode available")
    except ImportError:
        print_status(
            "llama-cpp-python installed", False, "Not required, but needed for AI mode"
        )

    return True


def check_model_file(config):
    """Check AI model file (optional)"""
    print_header("4️⃣  AI Model Check (Optional)")

    if not config:
        print_status("Model configuration", False, "config.json not loaded")
        return

    use_ai = config.get("use_ai", False)
    model_path = config.get("model_path", "")

    if not use_ai:
        print_status(
            "AI mode enabled",
            False,
            "AI disabled in config (use_ai: false). Bot will use simple responses.",
        )
        return

    print_status("AI mode enabled", True)

    if not model_path:
        print_status(
            "Model path configured", False, "model_path is empty in config.json"
        )
        return

    print_status("Model path configured", True, f"Path: {model_path}")

    if os.path.exists(model_path):
        size_mb = os.path.getsize(model_path) / (1024 * 1024)
        print_status("Model file exists", True, f"Size: {size_mb:.1f} MB")
    else:
        print_status("Model file exists", False, f"File not found: {model_path}")


def check_intents():
    """Remind about Discord Developer Portal intents"""
    print_header("5️⃣  Discord Developer Portal Configuration")

    print("\n⚠️  IMPORTANT: You MUST enable intents in Discord Developer Portal!")
    print("\n📋 Steps to enable intents:")
    print("   1. Go to: https://discord.com/developers/applications")
    print("   2. Select your bot application")
    print("   3. Go to 'Bot' tab")
    print("   4. Scroll to 'Privileged Gateway Intents'")
    print("   5. Enable: MESSAGE CONTENT INTENT ✅")
    print("   6. Click 'Save Changes'")
    print("   7. Restart your bot if it was running")

    print("\n❌ If you forget this, the bot will NOT read messages!")


def print_summary():
    """Print summary and next steps"""
    print_header("✨ Diagnostic Complete")

    print("\n📋 Next Steps:")
    print("   1. Fix any ❌ FAIL checks above")
    print("   2. Enable MESSAGE CONTENT INTENT in Developer Portal")
    print("   3. Run: python bot.py")
    print("   4. In Discord, try: !workly hello")
    print("\n📖 For more help, see: SETUP_DISCORD_BOT.md")


def run_diagnostics(silent=False):
    """Run all diagnostic checks and return True if critical checks pass"""
    if not silent:
        print("\n" + "=" * 60)
        print("  🤖 Discord Bot Diagnostic Tool")
        print("  Checking your configuration...")
        print("=" * 60)

    config = check_config_file()
    token_ok = check_discord_token(config)
    deps_ok = check_dependencies()
    check_model_file(config)

    if not silent:
        check_intents()
        print_summary()
        print("\n" + "=" * 60)

    # Return True only if critical checks pass
    return config is not None and token_ok and deps_ok


def main():
    """Run diagnostic in standalone mode"""
    run_diagnostics(silent=False)


if __name__ == "__main__":
    main()
