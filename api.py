from flask import Flask, request, jsonify
from src.predict import predict_admission

app = Flask(__name__)

# Required input fields
REQUIRED_FIELDS = [
    "gre",
    "toefl",
    "university_rating",
    "sop",
    "lor",
    "cgpa",
    "research"
]


# ==========================================================
# Home Route
# ==========================================================

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Graduate Admission Prediction API!",
        "status": "API is running successfully."
    })


# ==========================================================
# Prediction Route
# ==========================================================

@app.route("/predict", methods=["POST"])
def predict():

    # Check if request is JSON
    if not request.is_json:
        return jsonify({
            "error": "Request body must be in JSON format."
        }), 400

    data = request.get_json()

    # Check for missing fields
    missing_fields = [
        field for field in REQUIRED_FIELDS
        if field not in data
    ]

    if missing_fields:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing_fields)}"
        }), 400

    try:
        # Convert input values to appropriate data types
        gre_score = float(data["gre"])
        toefl_score = float(data["toefl"])
        university_rating = float(data["university_rating"])
        sop = float(data["sop"])
        lor = float(data["lor"])
        cgpa = float(data["cgpa"])
        research = int(data["research"])

        # Validate research value
        if research not in [0, 1]:
            return jsonify({
                "error": "Research must be either 0 or 1."
            }), 400

        # Make prediction
        prediction = predict_admission(
            gre_score=gre_score,
            toefl_score=toefl_score,
            university_rating=university_rating,
            sop=sop,
            lor=lor,
            cgpa=cgpa,
            research=research
        )

        return jsonify({
            "chance_of_admit": round(float(prediction), 4)
        }), 200

    except ValueError:
        return jsonify({
            "error": "Invalid input. Numeric values are expected."
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500


# ==========================================================
# Run Flask App
# ==========================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)