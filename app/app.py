from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def main_app():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.png', mimetype='favicon.png')
# npx tailwindcss -i ./static/input.css -o ./static/output.css --watch