from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def  home():
    print("kontol")
    return "flask is running"


import os


if __name__== "__main__" :
    port = int(os.environ.get("port", 5000))
    app.run(host="0.0.0.0", port=port)


# triger redeploy
