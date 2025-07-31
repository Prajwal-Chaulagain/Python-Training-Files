import re
import streamlit as st
from datetime import datetime

class RuleBasedChatBot:
    def __init__(self):
        self.rules = {
            r'hi|hello|hey': "Hello! How can I assist you today?",
            r'how are you': "I'm just a bot, but I'm doing great! How can I help you?",
            r'what is your name': "I am a rule-based chatbot, created by a Python enthusiast.",
            r'quit|exit': "Goodbye! Have a nice day!",
            r'help': "You can ask me about my name, how I am doing, or just say 'hi' to start a conversation!",
            r'what time is it': self.get_current_time,
            r'what is your purpose': "I am here to answer simple questions using pre-programmed rules.",
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for pattern, response in self.rules.items():
            if re.search(pattern, user_input):
                return response() if callable(response) else response
        return "I'm sorry, I didn't understand that. Can you ask something else?"

    def get_current_time(self):
        return "The current time is " + datetime.now().strftime('%H:%M:%S')

# Streamlit UI Setup
st.set_page_config(page_title="ChatBot", page_icon="🤖", layout="centered")
st.title("🤖 Rule-Based ChatBot")

st.write("Talk to the chatbot by typing below!")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

bot = RuleBasedChatBot()

# User input
user_input = st.text_input("You:", "", key="user_input")
if user_input:
    response = bot.get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for speaker, text in st.session_state.chat_history:
    with st.chat_message(speaker):
        st.write(text)
