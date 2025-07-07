# CV Extractor & Scrutinizer

A Python application for extracting, parsing, and assessing candidate CVs (PDF) against job requirements using advanced text extraction (including OCR for scanned PDFs) and Large Language Models (LLMs). Includes both a command-line interface and a Streamlit-based web GUI.

---

## Features

- **PDF CV Extraction:** Supports both text-based and scanned (image-based) PDFs using OCR (Tesseract).
- **Structured Parsing:** Uses an LLM (NVIDIA NIM Qwen3-235B) to convert raw CV text into structured JSON (see schema below).
- **Job Requirements Matching:** Compares parsed CVs to job requirements and generates a detailed, evidence-based assessment (score, recommendation, strengths, weaknesses).
- **Streamlit Web App:** User-friendly interface for uploading CVs and requirements, running assessments, and viewing results.
- **Command-Line Interface:** For batch or automated processing.

---

## Requirements

- Python 3.8+
- See `requirements.txt` for dependencies:
  - pdfplumber
  - pytesseract
  - pillow
  - openai
  - python-dotenv
  - PyMuPDF
  - streamlit
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (for scanned PDFs)

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ZiadWaleed2003/Cv-Extractor.git
   cd Cv-Extractor
   ```
2. **Create an Enviroment**
   create a local env using conda or any tool that you like just to prevent dependency issues 
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Install Tesseract OCR:**
   - Windows: Download from [here](https://github.com/tesseract-ocr/tesseract)
   - Linux: `sudo apt-get install tesseract-ocr`
   - Mac: `brew install tesseract`
4. **Set up environment variables:**
   - Create a `.env` file in the project root:
     ```env
     NVIDIA_API_KEY=your_nvidia_nim_api_key
     ```

---

## Usage

### 1. Command-Line (CLI)

Edit `main.py` to set your input file paths, or use the defaults:
- CV: `input/resume/uploaded_cv.pdf`
- Requirements: `input/requirements/uploaded_req.txt`

Run:
```bash
python main.py
```

The assessment will be printed to the console and the parsed CV will be saved to `results/parsed_cv.json`.

### 2. Streamlit Web App

```bash
streamlit run gui.py
```
- Upload a candidate CV (PDF) and job requirements (TXT).
- Click **Run Assessment** to view the results in the browser.

---

## Input/Output Examples

### Example Job Requirements (`input/requirements/uploaded_req.txt`):
```
Job Title: Machine Learning Intern
Location: [Remote/On-site/City, Country]
... (see file for full example)
```

### Example CV (`input/resume/uploaded_cv.pdf`):
- Use your own or the provided sample.

### Example Output (`results/parsed_cv.json`):
```json
{
  "name": "Ziad Waleed",
  "contact_info": { "email": "ziadwaleedmohamed2003@gmail.com", ... },
  "experience": [ { "company": "AICE XPERT", ... } ],
  ...
}
```

---

## Parsed CV Schema

The output JSON follows this schema (see `app/agents/data_model.py` for details):
- `name`: Full name
- `contact_info`: Email, phone, LinkedIn, etc.
- `summary`: Professional summary
- `experience`: List of jobs (company, position, dates, description, achievements)
- `education`: List of degrees (institution, degree, field, dates, GPA, location)
- `skills`: List of skills
- `projects`: List of projects (name, description, technologies, dates, URL)
- `certifications`: List of certifications
- `languages`: List of languages
- `awards`: List of awards
- `volunteer_experience`: Optional
- `hobbies`: Optional

---

## Environment Variables

- `NVIDIA_API_KEY`: Your Nvidia NIM API key (required for LLM access)

---