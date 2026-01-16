import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit UI
st.set_page_config(page_title="AI Travel Planner for Students", page_icon="🌍")
st.title("🌍 AI Travel Planner for Students")
st.write(
    "Plan **budget-friendly**, **personalized trips** using AI. "
    "Perfect for students with limited budgets 🎓"
)

# User Inputs
destination = st.text_input("📍 Destination", placeholder="e.g. Jaipur, Goa, Delhi")
days = st.number_input("🗓️ Number of Days", min_value=1, max_value=30, value=3)
budget = st.number_input("💰 Budget (INR)", min_value=1000, step=500, value=5000)
travel_style = st.selectbox(
    "🎒 Travel Style",
    ["Backpacking", "Sightseeing", "Food & Culture", "Relaxed", "Adventure"]
)

if st.button("✨ Generate Travel Plan"):
    if not destination:
        st.warning("Please enter a destination.")
    else:
        with st.spinner("Generating your personalized travel plan..."):
            prompt = f"""
            You are an AI travel planner specialized for students.

            Create a {days}-day budget-friendly travel itinerary for:
            Destination: {destination}
            Budget: ₹{budget}
            Travel Style: {travel_style}

            Include:
            - Daily plan
            - Cheap local transport options
            - Affordable food suggestions
            - Budget accommodation tips
            - Estimated daily cost
            - Student-friendly travel hacks

            Keep it practical and realistic.
            """

            response = model.generate_content(prompt)

            st.success("🎉 Your Travel Plan is Ready!")
            st.markdown(response.text)
