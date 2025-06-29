import google.generativeai as genai
import gradio as gr


genai.configure(api_key="AIzaSyDWo3Ujtj_dczqfoi0Fm3s-GQpXrMiisdw")


model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

def generate_motivation(mood):
    if not mood.strip():
        return "Please enter a mood or situation for motivation."

    prompt = f"Give a short, uplifting motivational quote for someone who is {mood}."

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"


iface = gr.Interface(
    fn=generate_motivation,
    inputs=gr.Textbox(lines=2, placeholder="e.g., feeling anxious, tired, or unmotivated"),
    outputs="text",
    title="🌟 Daily Motivation Generator",
    description="Enter how you feel, and receive a motivational quote tailored to your situation!"
)

iface.launch()

