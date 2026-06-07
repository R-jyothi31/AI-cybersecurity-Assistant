from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_file
)

from agents.planner import run_agent
from rag.retrieval import retrieve_context

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "file" not in request.files:
        return jsonify({
            "error": "No file uploaded"
        })

    file = request.files["file"]

    log_text = file.read().decode(
        "utf-8",
        errors="ignore"
    )

    result = run_agent(log_text)

    return jsonify(result)


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data["question"]

    answer = retrieve_context(question)

    return jsonify({
        "answer": answer
    })


@app.route("/download_report")
def download_report():

    return send_file(
        "reports/security_report.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )