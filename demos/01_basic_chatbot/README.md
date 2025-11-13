# 🤖 Basic AI Chatbot Demo

A simple console-based chatbot demonstrating Workly's AI conversation capabilities using llama-cpp-python.

## 📋 Overview

This demo shows the basics of:
- Loading a local LLM model (GGUF format)
- Creating a simple chat loop
- Generating AI responses
- Managing conversation context

## 🛠️ Requirements

- Python 3.11+
- 8GB RAM minimum
- A GGUF model file (e.g., Llama 3.2, Mistral)

## 📦 Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download a model (optional, uses default if available):
```bash
# Example: Download Llama 3.2 1B
# Place your .gguf model file in this folder
```

## 🚀 Usage

Run the chatbot:
```bash
python main.py
```

Example conversation:
```
🤖 Workly Chatbot Demo
Type 'quit' to exit

You: Hello!
Workly: Hello! I'm Workly, your AI assistant. How can I help you today?

You: What's 2+2?
Workly: 2 + 2 equals 4.

You: quit
Goodbye! 👋
```

## ⚙️ Configuration

Edit `config.json` to customize:
- Model path
- Max tokens per response
- Temperature (creativity)
- Context window size

```json
{
  "model_path": "model.gguf",
  "max_tokens": 256,
  "temperature": 0.7,
  "n_ctx": 2048
}
```

## 🔧 Technical Details

This demo uses:
- **llama-cpp-python**: Python bindings for llama.cpp
- **GGUF format**: Quantized model format for efficient inference
- **Simple prompt template**: Basic user/assistant format

### Model Loading
```python
from llama_cpp import Llama

llm = Llama(
    model_path="model.gguf",
    n_ctx=2048,
    n_threads=4
)
```

### Text Generation
```python
response = llm(
    prompt=f"User: {user_input}\nAssistant:",
    max_tokens=256,
    stop=["User:", "\n"],
    temperature=0.7
)
```

## 📊 Performance

Typical performance on consumer hardware:
- **CPU (i7-12700)**: ~10-15 tokens/sec
- **GPU (RTX 3060)**: ~40-60 tokens/sec
- **Memory usage**: 4-6GB for 7B models

## 🎯 Next Steps

To build on this demo:
1. Add conversation history tracking
2. Implement system prompts
3. Add streaming responses
4. Integrate with GUI
5. Add memory/context management

## 📝 Notes

- This is a simplified version for educational purposes
- The full Workly Desktop has advanced features like:
  - Long-term memory
  - Personality customization
  - Multi-turn context management
  - GPU acceleration
  - Streaming responses

## 🔗 Related

- [Memory System Demo](../04_memory_system/) — See how Workly remembers conversations
- [Full Documentation](../../docs/API.md) — Complete API reference

---

**Part of [Workly Public Edition](../../README.md)**
