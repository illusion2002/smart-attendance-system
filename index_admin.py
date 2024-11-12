from flask import Flask, render_template, request, Response
import subprocess
from flask_cors import CORS  # Import CORS


app = Flask(__name__)

CORS(app)


@app.route("/", methods=["GET"])
def index():
    # return Response("hello")
    return render_template("../admin.html")


@app.route("/run_scripta", methods=["GET", "POST"])
def run_scripta():
    print("Running script")
    # Run your Python script here
    subprocess.Popen(["python", "python files\\teacher_assign.py"])
    print("reached here")
    return "Script executed successfully"


@app.route("/run_scriptb", methods=["GET", "POST"])
def run_scriptb():
    # Run your Python script here
    subprocess.Popen(["python", "python files\\teacher_marks.py"])
    print("reached here")
    return "Script executed successfully"


if __name__ == "__main__":
    app.run(debug=True)
