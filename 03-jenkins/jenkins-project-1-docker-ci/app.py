from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Jenkins CI Project</title>
        </head>
        <body>
            <h1>Jenkins CI Pipeline</h1>
            <h2>Flask Application Running Successfully!</h2>
            <p>This application is built and tested through Jenkins.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
