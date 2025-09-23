from flask import Flask
import os  

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hola Mundo</h1>
    <h2>Eva Estefani Diaz Beltran - 22031466</h2>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)