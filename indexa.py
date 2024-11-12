from flask import Flask, render_template, request, Response
import subprocess
from flask_cors import CORS  # Import CORS


app = Flask(__name__)

CORS(app)


@app.route("/", methods=["GET"])
def index():
    # return Response("hello")
    return render_template("../next.html")


@app.route("/admin", methods=["GET"])
def admin():
    # return Response("hello")
    print("admin")
    return render_template(
        "C:\\Users\\Dell\\Desktop\\serious final\\frontend\\templates\\admin.html"
    )


@app.route("/run_scripta", methods=["GET", "POST"])
def run_scripta():
    print("Running script")
    # Run your Python script here
    subprocess.Popen(["python", "python files\\teacher_assign.py"])
    # print("reached here")
    # return "Script executed successfully"


@app.route("/admin/run_scriptq", methods=["GET", "POST"])
def run_scriptq():
    print("Running script")
    # Run your Python script here
    subprocess.Popen(["python", "python files\\admin.py"])
    # print("reached here")
    # return "Script executed successfully"


@app.route("/admin/run_scriptw", methods=["GET", "POST"])
def run_scriptw():
    print("Running script")
    # Run your Python script here
    subprocess.Popen(["python", "python files\\training.py"])
    # print("reached here")
    # return "Script executed successfully"


@app.route("/run_scriptb", methods=["GET", "POST"])
def run_scriptb():
    # Run your Python script here
    subprocess.Popen(["python", "python files\\teacher_marks.py"])
    print("reached here")
    return "Script executed successfully"


@app.route("/run_scriptc", methods=["GET", "POST"])
def run_scriptc():
    # Run your Python script here
    subprocess.Popen(["python", "python files\\face_recogn.py"])
    print("reached here")
    return "Script executed successfully"


@app.route("/run_scriptd", methods=["GET", "POST"])
def run_scriptd():
    # Run your Python script here
    subprocess.Popen(["python", "python files\\teacher_attendance.py"])
    print("reached here")
    return "Script executed successfully"


if __name__ == "__main__":
    app.run(debug=True)
