from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config["UPLOAD_FOLDER"] = os.getcwd() + "\\uploads"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files["file"]
        if file:
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
        return render_template("index.html")

    if request.method == 'GET':
        return render_template("index.html")


def main():
    """主函数"""
    app.run("0.0.0.0", "2333")


if __name__ == "__main__":
    main()
