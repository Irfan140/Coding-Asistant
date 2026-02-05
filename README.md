# 💻 AI Coding Assistant

An intelligent coding assistant powered by Groq's fast LLM inference and built with Streamlit. Get instant help with coding questions, debugging, code reviews, and algorithm optimization.

## ✨ Features

- **Multiple AI Models**: Choose from various
- **Real-time Streaming**: Get responses instantly with streaming output
- **Adjustable Parameters**: Control temperature and max tokens for customized responses
- **Clean Interface**: User-friendly chat interface with message history
- **Code-Optimized**: Specialized system prompts for coding assistance

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- A Groq API key (get one free at [console.groq.com](https://console.groq.com))

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Coding_Asistence
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Or using uv:

```bash
uv pip install -r requirements.txt
```

### Configuration

You can provide your Groq API key in the following way:

**In the App**: Enter your API key in the sidebar when running the application

### Running the Application

```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`

## 📖 Usage

1. **Enter API Key**: Add your Groq API key in the sidebar
2. **Select Model**: Choose from available models based on your needs:

- `llama-3.3-70b-versatile` - Latest and most capable
- `llama-3.1-8b-instant` - Fast responses, good for simple queries
- `openai/gpt-oss-120b` - Highly capable general purpose with reasoning/tools
- `meta-llama/llama-4-maverick-17b-128e-instruct` - Efficient MoE for complex code

3. **Adjust Settings**: Fine-tune temperature and max tokens as needed
4. **Start Chatting**: Ask coding questions and get instant help!

## 💡 What You Can Ask

- **Code Generation**: "Write a Python function to sort a list"
- **Debugging Help**: "Why is my loop not working?"
- **Explanations**: "Explain async/await in JavaScript"
- **Code Reviews**: "Review this code for best practices"
- **Algorithm Help**: "What's the best sorting algorithm for my use case?"
- **Optimization**: "How can I make this code more efficient?"

## 🛠️ Configuration Options

### Temperature (0.0 - 2.0)

- **Lower values (0.0-0.7)**: More focused and deterministic responses
- **Higher values (0.8-2.0)**: More creative and varied outputs

### Max Tokens (256 - 8192)

- Controls the maximum length of the AI's response
- Higher values allow for longer, more detailed answers

## 📦 Dependencies

- **streamlit**: Web application framework
- **groq**: Groq API client for LLM inference


## 📝 License

This project is open source and available under the MIT License.