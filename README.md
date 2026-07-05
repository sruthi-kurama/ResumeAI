# ResumeAI

ResumeAI is an AI-powered ATS Resume Builder developed using **Flask**, **Google Gemini AI**, **HTML**, **Tailwind CSS**, and **xhtml2pdf**. The application helps users create professional, ATS-friendly resumes by transforming their input into recruiter-quality content using AI. It also provides a live resume preview and allows users to download their resumes as PDF files.

---

## Features

- 🤖 AI-powered resume generation using Google Gemini AI
- 📄 ATS-friendly resume writing and formatting
- ✨ Professional rewriting of summaries, experience, education, and skills
- 👀 Live resume preview while generating resumes
- ⬇️ One-click PDF download
- 🎨 Modern, responsive, and user-friendly interface
- 📋 Multiple resume template section (ready for future expansion)
- ❓ FAQ and How It Works sections for improved user experience

---

## Technologies Used

- Python
- Flask
- Google Gemini API
- HTML5
- Tailwind CSS
- Jinja2 Templates
- xhtml2pdf
- Git & GitHub

---

## Project Structure

```text
ResumeAI/
│── app.py
│── prompts.py
│── requirements.txt
│── README.md
│── .gitignore
│── templates/
│     ├── index.html
│     └── pdf_template.html
│── static/
│     ├── style.css
│     └── script.js
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sruthi-kurama/ResumeAI.git
```

2. Navigate into the project:

```bash
cd ResumeAI
```

3. Create and activate a virtual environment.

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file and add your Gemini API key:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

6. Run the application:

```bash
python app.py
```

7. Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Future Enhancements

- Multiple professional resume templates
- Live editing without page refresh
- User authentication and saved resumes
- Resume score and ATS compatibility checker
- Cover letter generation
- LinkedIn profile integration

---

## Author

**Sruthi Kurama**

BBA Student | AI & Business Analytics Enthusiast

---

## License

This project is developed for educational and portfolio purposes.