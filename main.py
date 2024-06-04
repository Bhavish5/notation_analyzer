from flask import Flask, render_template, request

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
            return "Image saved!"


if __name__ == "__main__":
    app.run(debug=True)