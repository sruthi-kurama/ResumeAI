import os
import json

from flask import Flask, render_template, request, make_response
from dotenv import load_dotenv
from google import genai
from xhtml2pdf import pisa
from io import BytesIO

from prompts import RESUME_PROMPT

app = Flask(__name__)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Stores latest generated resume
latest_resume = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    global latest_resume

    fullname = request.form.get("fullname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    jobrole = request.form.get("jobrole")
    summary = request.form.get("summary")
    education = request.form.get("education")
    experience = request.form.get("experience")
    skills = request.form.get("skills")

    user_prompt = f"""
Name:
{fullname}

Target Role:
{jobrole}

Professional Summary:
{summary}

Education:
{education}

Experience:
{experience}

Skills:
{skills}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=RESUME_PROMPT + "\n\n" + user_prompt
        )

        response_text = response.text.strip()

        if response_text.startswith("```json"):
            response_text = response_text.replace(
                "```json", ""
            ).replace(
                "```", ""
            ).strip()

        ai_resume = json.loads(response_text)

    except Exception as e:

        print(e)

        ai_resume = {
            "summary": summary,
            "experience": experience,
            "education": education,
            "skills": [s.strip() for s in skills.split(",")] if skills else []
        }

    latest_resume = {
    "fullname": fullname,
    "email": email,
    "phone": phone,
    "jobrole": ai_resume["jobrole"],
    "summary": ai_resume["summary"],
    "experience": ai_resume["experience"],
    "education": ai_resume["education"],
    "skills": ai_resume["skills"]
}

    return render_template(
        "index.html",
        **latest_resume
    )


@app.route("/download-pdf")
def download_pdf():

    if not latest_resume:
        return "Generate a resume first."

    html = render_template(
        "pdf_template.html",
        **latest_resume
    )

    pdf = BytesIO()

    pisa.CreatePDF(
        src=html,
        dest=pdf
    )

    response = make_response(pdf.getvalue())

    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=ResumeAI_Resume.pdf"

    return response

if __name__ == "__main__":
    app.run(debug=True)