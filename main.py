import streamlit as st
from groq import Groq
import os

# Page configuration
st.set_page_config(
    page_title="Coding Agent",
    page_icon="💻",
    layout="wide"
)

# Initialize Groq client
def initialize_groq():
    api_key = os.getenv("GROQ_API_KEY") or st.session_state.get("groq_api_key")
    if api_key:
        return Groq(api_key=api_key)
    return None

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = ""

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    
    # API Key input
    api_key_input = st.text_input(
        "Groq API Key",
        type="password",
        value=st.session_state.groq_api_key,
        help="Get your API key from https://console.groq.com"
    )
    
    if api_key_input:
        st.session_state.groq_api_key = api_key_input
    
    # Model selection
    model = st.selectbox(
        "Select Model",
        [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "openai/gpt-oss-120b",
            "meta-llama/llama-4-maverick-17b-128e-instruct"
        ],
        help="Choose the AI model for your assistant"
    )
    
    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Higher values make output more random"
    )
    
    # Max tokens
    max_tokens = st.slider(
        "Max Tokens",
        min_value=256,
        max_value=8192,
        value=2048,
        step=256,
        help="Maximum length of the response"
    )
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    
    

# Main chat interface
st.title("💻 Coding Agent")
st.markdown("Ask me anything about coding, debugging, or software development!")

# Check if API key is set
client = initialize_groq()

if not client:
    st.warning("⚠️ Please enter your Groq API key in the sidebar to start chatting.")
else:
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a coding question..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # Create system message for coding assistant
                system_message = {
                    "role": "system",
                    "content": 
                    """
                    You are an expert coding assistant. Help users with:
                                - Writing clean, efficient code
                                - Debugging and troubleshooting
                                - Explaining programming concepts
                                - Code reviews and best practices
                                - Algorithm design and optimization

                        Always provide clear explanations and well-formatted code examples with proper syntax highlighting.
                        When providing code, use markdown code blocks with language specification (e.g., ```python).
                    """
                }
                
                # Prepare messages for API
                messages = [system_message] + st.session_state.messages
                
                # Stream response from Groq
                stream = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stream=True
                )
                
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
            except Exception as e:
                error_message = f"❌ Error: {str(e)}"
                message_placeholder.error(error_message)
                full_response = error_message
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})