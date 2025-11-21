#!/usr/bin/env python3
"""
LLM_QA_CLI.py
Simple CLI that accepts a natural-language question, applies basic preprocessing,
constructs a prompt, and calls an LLM API (Google Gemini by default).

Usage:
  python LLM_QA_CLI.py

Set environment variable `GEMINI_API_KEY` before running if you want real LLM responses.
Get your free API key at: https://makersuite.google.com/app/apikey
"""
import os
import re
import sys
import json

try:
    import google.generativeai as genai
except Exception:
    genai = None


def preprocess(text: str) -> str:
    """Lowercase, remove punctuation, simple tokenization normalization."""
    text = text.lower()
    # remove punctuation (keep spaces and alphanumerics)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    # collapse whitespace
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
        return "[MISSING_LIB] The `google-generativeai` package is not installed. Install it from requirements.txt."

    try:
        genai.configure(api_key=api_key)
        model_instance = genai.GenerativeModel(model)
        response = model_instance.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[API_ERROR] {e}"


def main():
    if len(sys.argv) > 1:
        # support passing question as command-line argument
        question = " ".join(sys.argv[1:])
    else:
        try:
            question = input("Enter your natural-language question: ")
        except KeyboardInterrupt:
            print("\nCancelled.")
            sys.exit(0)

    processed = preprocess(question)
    prompt = construct_prompt(processed)

    print("\n--- Processed Question ---")
    print(processed)
    print("\n--- Sending to LLM (Google Gemini) ---")

    answer = call_gemini(prompt)

    print("\n--- Final Answer ---")
    print(answer)


if __name__ == "__main__":
    main()
