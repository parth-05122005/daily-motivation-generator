import os
import logging
import google.generativeai as genai
import gradio as gr
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

genai.configure(api_key=api_key)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

# Helper function to build prompt
def build_prompt(mood):
    return (
        f"You are a motivational coach. Give a short, uplifting, and specific motivational quote "
        f"for someone who is currently {mood}. Keep it under 25 words."
    )

# Main function
def generate_motivation(mood):
    if not mood.strip():
        return "⚠️ Please enter a mood or situation to receive motivation."

    prompt = build_prompt(mood)

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error generating content: {e}")
        return "❌ Something went wrong while generating your quote. Please try again."

# Gradio UI
iface = gr.Interface(
    fn=generate_motivation,
    inputs=gr.Textbox(
        lines=2,
        placeholder="e.g., feeling anxious, tired, or unmotivated",
        label="How are you feeling?"
    ),
    outputs=gr.Textbox(label="💡 Your Motivational Quote"),
    title="🌟 Daily Motivation Generator",
    description="Enter your mood or mental state, and receive a motivational quote tailored to your situation!",
    examples=[
        ["feeling anxious"],
        ["tired and stressed"],
        ["lost confidence"],
        ["unmotivated after failure"]
    ],
)

# Launch the app
iface.launch(debug=True)
