from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        img = request.files["input_image"]
        if img.filename == "":
            return "Please Upload an image!"
        else:
            img.save("image.jpeg")
            analyze_image()
            return "Image saved!"

def analyze_image():
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Gemini vs gpt which is better?", stream=True)
    for chunk in response:
        print(chunk.text)


if __name__ == "__main__":
    app.run(debug=True)