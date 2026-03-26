from flask import Flask, render_template, request
import os

from app.captioner import generate_caption
from app.self_corrector import refine_caption
from app.scorer import choose_best
from app.hashtag import generate_hashtags

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def run_pipeline(image_path):
    c1 = generate_caption(image_path)
    c2 = refine_caption(image_path)
    best = choose_best(c1, c2)
    hashtags = generate_hashtags(best)

    return c1, c2, best, hashtags


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    file = request.files["image"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    c1, c2, best, hashtags = run_pipeline(filepath)

    return f"""
    <h3>Caption 1:</h3> {c1}
    """


if __name__ == "__main__":
    app.run(debug=True)