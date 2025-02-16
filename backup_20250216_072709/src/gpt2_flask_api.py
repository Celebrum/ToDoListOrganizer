from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

@app.route('/generate_content', methods=['POST'])
def generate_content():
    data = request.get_json()
    prompt = data.get('prompt', '')

    # Generate content using GPT-2
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )

    content = response.choices[0].text.strip()
    return jsonify({'content': content})

if __name__ == '__main__':
    app.run(debug=True)
