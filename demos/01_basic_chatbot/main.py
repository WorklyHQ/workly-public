"""
Simple AI Chatbot Demo - Workly Public Edition

Demonstrates basic conversation capabilities using llama-cpp-python.
This is a simplified version for educational purposes.

Author: WorklyHQ
License: See LICENSE file
"""

import json
import os
from pathlib import Path

try:
    from llama_cpp import Llama
except ImportError:
    print("❌ Error: llama-cpp-python not installed")
    print("📦 Install with: pip install llama-cpp-python")
    exit(1)


def load_config():
    """Load configuration from config.json"""
    config_path = Path(__file__).parent / "config.json"

    if config_path.exists():
        with open(config_path, "r") as f:
            return json.load(f)

    # Default configuration
    return {
        "model_path": "model.gguf",
        "max_tokens": 256,
        "temperature": 0.7,
        "n_ctx": 2048,
        "n_threads": 4,
    }


def load_model(config):
    """Load the LLM model"""
    model_path = config["model_path"]

    if not os.path.exists(model_path):
        print(f"❌ Model not found: {model_path}")
        print("📥 Please download a GGUF model and update config.json")
        print("\nExample models:")
        print("- Llama 3.2 1B: https://huggingface.co/models?search=llama-3.2-1b-gguf")
        print("- Mistral 7B: https://huggingface.co/models?search=mistral-7b-gguf")
        return None

    print(f"📦 Loading model: {model_path}")

    try:
        llm = Llama(
            model_path=model_path,
            n_ctx=config["n_ctx"],
            n_threads=config["n_threads"],
            verbose=False,
        )
        print("✅ Model loaded successfully!\n")
        return llm

    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None


def generate_response(llm, user_input, config):
    """Generate AI response"""
    prompt = f"User: {user_input}\nAssistant:"

    try:
        response = llm(
            prompt,
            max_tokens=config["max_tokens"],
            temperature=config["temperature"],
            stop=["User:", "\n\n"],
            echo=False,
        )

        return response["choices"][0]["text"].strip()

    except Exception as e:
        return f"Error generating response: {e}"


def main():
    """Main chatbot loop"""
    print("=" * 60)
    print("🤖 Workly Chatbot Demo")
    print("=" * 60)
    print("\nThis is a simplified demo of Workly's AI capabilities.")
    print("Type 'quit' to exit\n")

    # Load configuration
    config = load_config()

    # Load model
    llm = load_model(config)
    if llm is None:
        return

    # Chat loop
    print("🎉 Ready! Start chatting:\n")

    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()

            if not user_input:
                continue

            # Check for quit command
            if user_input.lower() in ["quit", "exit", "bye"]:
                print("\n👋 Goodbye!")
                break

            # Generate response
            print("Workly: ", end="", flush=True)
            response = generate_response(llm, user_input, config)
            print(response + "\n")

        except KeyboardInterrupt:
            print("\n\n👋 Interrupted by user. Goodbye!")
            break

        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()
