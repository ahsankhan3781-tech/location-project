from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json()

    print("\n--- Location received ---")
    print("Latitude:", data.get("latitude"))
    print("Longitude:", data.get("longitude"))
    print("Accuracy:", data.get("accuracy"), "meters")
    print("-------------------------\n")

    return jsonify({
        "message": "Location successfully shared."
    })

if __name__ == "__main__":
    app.run()