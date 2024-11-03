# config_store.py (Mock Configuration Server)
from flask import Flask, jsonify

app = Flask(__name__)
# Sample configurations per country-operator
configs = {
    "US-TMobile": {"rate_limit": 5, "timeout": 10},
    "IN-Airtel": {"rate_limit": 10, "timeout": 8},
    # More configurations...
}

@app.route('/<country_operator>', methods=['GET'])
def get_config(country_operator):
    return jsonify(configs.get(country_operator, {}))

if __name__ == "__main__":
    app.run(port=5000)
