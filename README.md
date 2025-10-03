# AI Assistant with Gemini Pro and Streamlit

This project creates an AI assistant using Google's Gemini Flash Lite API, accessible through a Streamlit web interface.

## Features
- 💬 Interactive chat interface with conversation history
- 🔒 Secure API key management via `.env` file
- 🧠 Powered by Google's Gemini Flash lite LLM
- 🧹 Clear chat history functionality

## Prerequisites
- Python 3.11+
- Google Gemini Pro API key (from https://ai.google.dev/)
- Streamlit for web interface

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-assistant.git
   cd ai-assistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Create `.env` file in project root with your API key:
   ```env
   API_KEY=your_actual_api_key_here
   ```
2. The `.gitignore` file already excludes `.env` from version control

## Usage
Start the Streamlit application:
```bash
streamlit run ai_assistant.py
```

## Project Structure
```
├── ai_assistant.py       # Main application code
├── .env                  # API key configuration (not version controlled)
├── .gitignore            # Specifies untracked files
├── requirements.txt      # Dependency list
└── README.md             # This documentation
```

## Implementation Details
- Uses Google's Generative AI SDK for Gemini Pro integration
- Streamlit for modern web interface
- Environment variables for secure credential management
- Session state for maintaining chat history

The application provides a clean, interactive interface for testing Gemini Pro's capabilities through natural language conversations.
