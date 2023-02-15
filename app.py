
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/formPrueba")
def formprueba():
    return render_template("formprueba.html")

if __name__ == "__main__":
    app.run(debug=True)