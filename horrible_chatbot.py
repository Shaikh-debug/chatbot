import streamlit as st
import cohere
import os

# Securely set up Cohere API using environment variables
cohere_api_key = os.getenv("COHERE_API_KEY")  # Set this in your environment/Streamlit secrets
if not cohere_api_key:
    st.error("Cohere API key not found! Please configure your environment variables.")
    st.stop()

co = cohere.Client(cohere_api_key)

st.title("Bad Study Advice Chatbot 🤖")
st.write("Ask for study advice... but beware, it's all terrible!")

user_input = st.text_input("Ask me anything about studying:")

if user_input:
    try:
        response = co.generate(
            model='command',
            prompt=f"""Give the absolute worst and funniest study advice ever for: {user_input}. 
            Make it sound confident but completely useless. Be creative with terrible suggestions.
            Examples:
            - "Write notes in lemon juice for secret invisible ink studying"
            - "Watch YouTube videos at 3x speed to become a genius instantly"
            - "Replace sleep with energy drinks for maximum productivity"
            - "Only study during lunar eclipses for cosmic knowledge absorption"
            """,
            max_tokens=100  # Increased for more complete responses
        )
        st.write("🤖 **Bad Advice Bot:**", response.generations[0].text)
    except Exception as e:
        st.error(f"Oops! The bot malfunctioned: {str(e)}")