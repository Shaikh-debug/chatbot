import streamlit as st
import cohere
import os

st.markdown("""
<style>
    .stApp { 
        background-color: #FFFACD;  /* Lemon Chiffon */
        font-family: "Comic Sans MS", cursive;
    }
    .stTextInput>div>div>input {
        background-color: #FFD1DC !important; /* Pastel Pink */
        color: #FF00FF !important; /* Magenta */
    }
    .stButton>button {
        background-color: #00FFFF !important; /* Cyan */
        color: #FF4500 !important; /* OrangeRed */
        border: 2px dashed #800080 !important; /* Purple */
    }
</style>
""", unsafe_allow_html=True)

# Securely set up Cohere API using environment variables
cohere_api_key = os.getenv("COHERE_API_KEY")  # Set this in your environment/Streamlit secrets
if not cohere_api_key:
    st.error("Cohere API key not found! Please configure your environment variables.")
    st.stop()

co = cohere.Client(cohere_api_key)

st.title("Bad Study Advice Chatbot 🤖")
st.write("Ask for study advice... but beware, it's all terrible!")

user_input = st.text_input("TYPE YOUR ACADEMIC PROBLEM HERE (or don't, I'm a bot, not a cop)")

if user_input:
    st.balloons()  # 🎉
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
        with st.sidebar:
    st.header("⚠️ DISCLAIMER ⚠️")
    st.write("This bot was created by:")
    st.write("- A sleep-deprived student")
    st.write("- 3 cups of expired coffee")
    st.write("- A dare gone wrong")
    if st.checkbox("I accept that this advice will ruin my life"):
        st.error("Good. Proceed at your own risk. 🚑")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW0yY2F6Z2R0bXZqY2V6dHd4Z2R6eGJ6dGJmN2RycWZ1bGJzbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKUMdihx0FfQ3iE/giphy.gif", 
         caption="You trying to follow this advice:")
        st.write("🤖 **Bad Advice Bot:**", response.generations[0].text)
    except Exception as e:
        st.error(f"Oops! The bot malfunctioned: {str(e)}")
