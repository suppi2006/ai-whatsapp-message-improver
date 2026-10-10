# AI WhatsApp Message Improver 💬

An AI-powered web application that helps users improve their WhatsApp messages by making them clearer, more professional, and better suited to the intended tone.

## Features

- Improve WhatsApp messages using AI.
- Generate clearer and more polished text.
- Make messages more professional and readable.
- Simple web interface for entering messages and viewing results.

## Technologies Used

- Python
- Flask
- HTML and CSS
- Google Gemini API

## Project Structure

```text
AI-WhatsApp-Message-Improver/
├── app.py
├── requirements.txt
├── .gitignore
├── templates/
│   └── index.html
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd AI-WhatsApp-Message-Improver
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project folder and add your Gemini API key using the environment variable name expected by `app.py`.

**Important:** Never upload your `.env` file or API key to GitHub.

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

`http://127.0.0.1:5000/`

## Purpose

This project was developed to practise Python, Flask, web development, and integration with a generative AI API.

## Author

Developed as a Python and AI learning project.
