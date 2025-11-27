from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "5G DU Demo Running!"

@app.route('/status')
def status():
    # Simulated 5G DU status metrics
    return jsonify({
        "DU_ID": "DU001",
        "Cell_Status": "Active",
        "Connected_UEs": 5,
        "CPU_Usage": "15%",
        "Memory_Usage": "120MB"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
