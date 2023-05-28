from flask import Flask ,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        user = request.form["nm"]
        return f"<h1>{user}</h1>"
    else:
        return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True, port='0.0.0.0')
