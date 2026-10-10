from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai
import os


# Load environment variables
load_dotenv()


# Create Flask application
app = Flask(__name__)


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Please add it to your .env file."
    )


# Create Gemini client
client = genai.Client(api_key=api_key)


@app.route("/", methods=["GET", "POST"])
def home():

    improved_message = None
    error = None

    # Check whether user submitted the form
    if request.method == "POST":

        # Get message from form
        message = request.form.get("message", "").strip()

        # Get selected style
        style = request.form.get("style", "Professional").strip()

        # Check message
        if not message:

            error = "Please enter a WhatsApp message."

        else:

            # Create AI prompt
            prompt = f"""
You are an AI WhatsApp Message Improver.

The user has entered this WhatsApp message:

"{message}"

The selected writing style is:

{style}

Improve the message according to these rules:

1. Correct grammar and spelling.
2. Make the message clear and easy to understand.
3. Keep the original meaning exactly.
4. Do not add information that was not present in the original message.
5. Make it suitable for WhatsApp.
6. Return only the improved message.
7. Do not explain what you changed.

Style instructions:

Professional:
Make the message polite, clear and professional.

Friendly:
Make the message warm, polite and friendly.

Formal:
Make the message formal and respectful.

Short and Simple:
Keep the message short, clear and easy to understand.

Now provide the improved message.
"""

            try:

                # Models to try
                models = [
                    "gemini-3.8-flash",
                    "gemini-3.7-flash",
                    "gemini-3.6-flash",
                    "gemini-2.5-flash"
                ]

                response = None
                last_error = None

                # Try models one by one
                for model in models:

                    try:

                        print(f"Trying model: {model}")

                        response = client.models.generate_content(
                            model=model,
                            contents=prompt
                        )

                        if response.text:
                            print(f"Success using: {model}")
                            break

                    except Exception as e:

                        print(f"Model {model} failed: {e}")
                        last_error = e


                # Check response
                if response is None or not response.text:
                    raise Exception(last_error)


                # Store improved message
                improved_message = response.text.strip()


            except Exception as e:

                print("Gemini Error:", e)

                error = (
                    "Unable to improve the message right now. "
                    "Please try again."
                )


    return render_template(
        "index.html",
        improved_message=improved_message,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)