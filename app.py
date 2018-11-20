from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("1nd3x.html")

@app.route("/4b0ut")
def about():
    return render_template("4b0ut.html")

@app.route("/c0nt4ct")
def contact():
    return render_template("c0nt4ct.html")

@app.route("/n3w5")
def news():
    return render_template("n3w5.html")

if __name__ == "__main__":
    app.run(debug=True)
