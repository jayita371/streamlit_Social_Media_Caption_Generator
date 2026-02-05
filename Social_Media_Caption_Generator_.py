import os
import streamlit as st
import google.generativeai as genai
#from dotenv import load_dotenv
# Direct API key

#load_dotenv()
api_key_new = st.secrets.get("GOOGLE_API_KEY")
genai.configure(api_key="AIzaSyBBBM-GOfKv3AeRdiW3PYexO8aXmgvqEyA")

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------
# Streamlit UI
# -------------------------
st.title("📱 Social Media Caption Generator")

description = st.text_area("Enter product/service description")

tone = st.selectbox(
    "Select tone",
    ["Witty", "Professional", "Casual", "Inspirational", "Friendly", "Luxury"]
)

# -------------------------
# Button
# -------------------------
if st.button("Generate Captions"):

    if description:

        prompt = f"""
Write 3 social media captions under 30 words, tone: {tone}, about:
{description}
"""

        response = model.generate_content(prompt)

        st.subheader("✨ Generated Captions")
        st.write(response.text)

    else:
        st.warning("Please enter product/service description")
