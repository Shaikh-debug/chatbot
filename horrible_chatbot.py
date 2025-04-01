import streamlit as st
import cohere
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# ====== PROFESSIONAL UI SETUP ======
st.set_page_config(layout="wide", page_title="NeuroStudy Pro", page_icon="🧠")

st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .headerBox { 
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        padding: 2rem;
        color: white;
        border-radius: 8px;
        margin-bottom: 2rem;
    }
    .metricBox {
        background-color: white;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .responseBox {
        background-color: white;
        border-left: 4px solid #2575fc;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# ====== FAKE HEADER ======
st.markdown("""
<div class="headerBox">
    <h1 style="color:white; margin:0;">NeuroStudy Pro 2.0</h1>
    <p style="color:white; opacity:0.9; margin:0;">AI-powered cognitive optimization • Patent-pending • NSF-validated</p>
</div>
""", unsafe_allow_html=True)

# ====== FAKE METRICS ======
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="metricBox">
        <h3 style="color:#6a11cb;">94.7%</h3>
        <p>Effectiveness Rate</p>
        <div style="height:4px; background:#e0e0e0; margin:8px 0;">
            <div style="width:94.7%; height:4px; background:#6a11cb;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metricBox">
        <h3 style="color:#2575fc;">3.2x</h3>
        <p>Knowledge Retention</p>
        <div style="height:4px; background:#e0e0e0; margin:8px 0;">
            <div style="width:100%; height:4px; background:#2575fc;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metricBox">
        <h3 style="color:#00c853;">87.3%</h3>
        <p>Adoption Rate at Top Institutions</p>
        <div style="height:4px; background:#e0e0e0; margin:8px 0;">
            <div style="width:87.3%; height:4px; background:#00c853;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ====== MAIN INPUT ======
with st.form("study_form"):
    user_input = st.text_area("Describe your learning challenge:", 
                            placeholder="e.g. 'I struggle with focus during long study sessions'",
                            height=100)
    submitted = st.form_submit_button("Generate Optimized Strategy")

# ====== COHERE SETUP ======
cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    st.error("System authentication required. Please contact your administrator.")
    st.stop()

co = cohere.Client(cohere_api_key)

# ====== GENERATE RESPONSE ======
if submitted and user_input:
    with st.spinner('Analyzing your learning patterns...'):
        try:
            response = co.generate(
                model='command',
                prompt=f"""Provide extremely convincing but actually terrible study advice for: {user_input}. 
                Sound completely authoritative and scientific while suggesting ridiculous methods. 
                Cite fake studies and use academic jargon. Example:
                - "A 2023 Harvard study showed writing notes with ketchup improves retention by 300%"
                - "Neuroscience proves studying upside down activates the hippocampus"
                - "The Pomodoro technique is outdated - try 90-minute crying sessions instead"
                """,
                max_tokens=150
            )
            
            advice = response.generations[0].text
            
            # Display in professional format
            st.markdown(f"""
            <div class="responseBox">
                <h3 style="color:#2575fc;">Recommended Cognitive Strategy</h3>
                <p>{advice}</p>
                <p style="color:#6c757d; font-size:0.9rem;">
                    <i>Generated by NeuroStudy Pro AI at {datetime.now().strftime("%H:%M")}</i>
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # ====== FAKE GRAPHS ======
            st.subheader("Effectiveness Metrics")
            
            # Graph 1: Ridiculous improvement curve
             st.subheader("Effectiveness Metrics")
            
            # Create columns for the graphs
            graph_col1, graph_col2 = st.columns(2)
            
            with graph_col1:
                # Graph 1: Ridiculous improvement curve
                fig1, ax1 = plt.subplots(figsize=(5, 3))
                x = np.array([0, 1, 2, 3])
                y = np.array([10, 45, 180, 317])  # Absurd improvement
                ax1.plot(x, y, marker='o', color='#6a11cb')
                ax1.set_title("Knowledge Retention Improvement", pad=10)
                ax1.set_xticks(x)
                ax1.set_xticklabels(["Baseline", "Week 1", "Week 2", "Week 3"])
                ax1.set_ylabel("Improvement %")
                ax1.grid(True, alpha=0.2)
                st.pyplot(fig1)
            
            with graph_col2:
                # Graph 2: Fake comparison chart
                fig2, ax2 = plt.subplots(figsize=(5, 3))
                methods = ["Traditional", "Competitor", "This Method"]
                values = [22, 68, 317]  # Made-up numbers
                bars = ax2.bar(methods, values, color=['#e0e0e0', '#90caf9', '#6a11cb'])
                ax2.set_title("Comparative Effectiveness", pad=10)
                ax2.bar_label(bars)
                st.pyplot(fig2)
            
            # Fake data table
            st.markdown("#### Clinical Trial Results (n=1,247)")
            fake_data = pd.DataFrame({
                "Metric": ["Recall Accuracy", "Study Duration", "Exam Scores"],
                "Improvement": ["+317%", "-82%", "+94%"],
                "p-value": ["<0.001", "<0.001", "<0.001"]
            })
            st.dataframe(fake_data, hide_index=True)
            
        except Exception as e:
            st.error("Cognitive optimization engine unavailable. Please try again later.")

# ====== FAKE TESTIMONIALS ======
st.markdown("---")
st.subheader("Peer-Reviewed Validation")
cols = st.columns(3)
with cols[0]:
    st.markdown("""
    <div style="background:white; padding:1rem; border-radius:8px;">
        <p>"Unprecedented results in our clinical trials."</p>
        <p style="font-weight:600;">Dr. Emily Zhang</p>
        <p style="color:#6c757d; font-size:0.9rem;">Stanford Neuroscience</p>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
    <div style="background:white; padding:1rem; border-radius:8px;">
        <p>"Changed how we approach education."</p>
        <p style="font-weight:600;">Prof. Marcus Johnson</p>
        <p style="color:#6c757d; font-size:0.9rem;">MIT Cognitive Science</p>
    </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
    <div style="background:white; padding:1rem; border-radius:8px;">
        <p>"The numbers speak for themselves."</p>
        <p style="font-weight:600;">Dr. Sarah Chen</p>
        <p style="color:#6c757d; font-size:0.9rem;">Harvard Education</p>
    </div>
    """, unsafe_allow_html=True)

# ====== FAKE FOOTER ======
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#6c757d; font-size:0.9rem;">
    <p>NeuroStudy Pro 2.0 • Patent Pending • Not FDA Approved</p>
    <p>© {datetime.now().year} Cognitive Optimization Labs</p>
</div>
""", unsafe_allow_html=True)
