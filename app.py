from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_message"]

    # Use OpenAI's GPT-3.5 model to generate a response
    response = openai.Completion.create(
        engine="davinci",  # GPT-3.5 engine
        prompt=user_message,
        max_tokens=50  # Control the response length
    )

    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(debug=True)
