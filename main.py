from flask import Flask, render_template, request, send_file
import google.generativeai as genai
import os
import PIL.Image

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
            return send_file("game.pgn", as_attachment=True)

def analyze_image():
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    image = PIL.Image.open("image.jpeg")
    response = model.generate_content(["The given image consists of general handwritten chess notations, can you write the standard .pgn chess notations for these handwritten notations understood by a .pgn viewer, which I can directly upload and analyze my game, be sure to follow the standard .pgn format", image], stream=True)
    response.resolve()
    f = open("game.pgn","w")
    for chunk in response:
        f.write(chunk.text)
    f.close()


if __name__ == "__main__":
    app.run(debug=True)