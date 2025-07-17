from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = f"""
    لطفاً بر اساس اطلاعات زیر یک برنامه تمرینی و غذایی حرفه‌ای برای ورزشکار طراحی کن:
    سن: {data['age']}
    جنسیت: {data['gender']}
    هدف: {data['goal']}
    سطح: {data['level']}
    تعداد روزهای تمرین در هفته: {data['days']}
    محل تمرین: {data['location']}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    plan = response.choices[0].message.content
    return jsonify({"plan": plan})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
