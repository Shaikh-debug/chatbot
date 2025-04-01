import streamlit as st
import cohere
import os

# ====== GOOFY STYLING ======
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

# ====== COHERE SETUP ======
cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    st.error("Cohere API key not found! Please configure your environment variables.")
    st.stop()

co = cohere.Client(cohere_api_key)

# ====== TITLE & INPUT ======
st.title("🤪💩🔥 TERRIBLE STUDY ADVICE GENERATOR 9000 🔥💩🤪")
st.subheader("Warning: Following these tips may cause your GPA to evaporate 🫠")

user_input = st.text_input(
    "TYPE YOUR ACADEMIC PROBLEM HERE (or don't, I'm a bot, not a cop):",
    placeholder="e.g., 'How to pass exams while sleeping 20 hours a day?'"
)

# ====== SIDEBAR ======
with st.sidebar:
    st.header("⚠️ DISCLAIMER ⚠️")
    st.write("This bot was created by:")
    st.write("- A sleep-deprived student")
    st.write("- 3 cups of expired coffee")
    st.write("- A dare gone wrong")
    if st.checkbox("I accept that this advice will ruin my life"):
        st.error("Good. Proceed at your own risk. 🚑")

# ====== BOT RESPONSE ======
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
            max_tokens=100
        )
        
        # Display response in a ridiculous format
        st.markdown(
            f"""
            <div style="
                background-color: #FFEE00;
                padding: 10px;
                border: 3px dotted #FF00FF;
                border-radius: 0px 25px 0px 25px;
                margin: 10px 0;
            ">
            <p style="color: #FF0000; font-size: 18px;">🤖💬 <b>BOT'S HORRIBLE IDEA:</b></p>
            <p style="color: #8B00FF; font-size: 20px;">{response.generations[0].text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Add ridiculous GIF
        st.image("https://media.giphy.com/media/3o7TKUMdihx0FfQ3iE/giphy.gif", 
                caption="You trying to follow this advice:")
        
    except Exception as e:
        st.error(f"Oops! The bot malfunctioned: {str(e)}")
        st.image("https://media.giphy.com/media/l0HU7JI1u1On8q6A8/giphy.gif",
                caption="The bot right now:")
