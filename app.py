from flask import Flask, render_template, request
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

try:
    import google.generativeai as genai
except Exception:
    genai = None

app = Flask(__name__)


def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def construct_prompt(processed_question: str) -> str:
    return (
        "You are a helpful assistant. Answer the user's question concisely and accurately.\n\n"
        f"Question: {processed_question}\n\nAnswer:"
    )


def call_gemini(prompt: str, model: str = "gemini-pro") -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return (
            "[NO_API_KEY] Set the GEMINI_API_KEY environment variable to get a real response.\n"
            "Get your free API key at: https://makersuite.google.com/app/apikey\n"
            "Simulated answer: I can't call the API because the API key is not set."
        )

    if genai is None:
        return "[MISSING_LIB] The `google-generativeai` package is not installed."

    try:
        genai.configure(api_key=api_key)
        model_instance = genai.GenerativeModel(model)
        response = model_instance.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[API_ERROR] {e}"


@app.route("/", methods=["GET", "POST"])
def index():
    processed = ""
    prompt = ""
    response = ""
    answer = ""

    if request.method == "POST":
        question = request.form.get("question", "")
        processed = preprocess(question)
        prompt = construct_prompt(processed)
        response = call_gemini(prompt)
        answer = response

    return render_template("index.html", processed=processed, prompt=prompt, response=response, answer=answer)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
