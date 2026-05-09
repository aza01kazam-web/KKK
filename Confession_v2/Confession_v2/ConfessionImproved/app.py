from pathlib import Path

from flask import Flask, send_from_directory


BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)


@app.get("/")
def home() -> object:
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/<path:filename>")
def static_files(filename: str) -> object:
    return send_from_directory(BASE_DIR, filename)


if __name__ == "__main__":
    app.run(debug=True)
