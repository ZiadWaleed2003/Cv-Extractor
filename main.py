from app.agents.cv_parser import CvParser
from app.agents.scrutinizer import Scrutinizer
from app.extractors.process_cv import process_cv
from app.utils import read_requirements_file
from app.utils import read_cv_json
import os
import sys


def main():
  

    # --- File paths ---
    cv_path = os.path.join('input', 'resume', 'text_based_version.pdf')  # or 'Resume_scanned_version.pdf'
    requirements_path = os.path.join('input', 'requirements', 'req.txt')
    output_json_path = os.path.join('results', 'parsed_cv.json')

    # --- Step 1: Extract text from CV ---
    print(f"Extracting text from CV: {cv_path}")
    cv_text = process_cv(cv_path)
    if not cv_text.strip():
        print("Failed to extract text from CV.")
        sys.exit(1)

    # --- Step 2: Parse CV text to structured data ---
    print("Parsing CV text with LLM...")
    parser = CvParser()
    try:
        parser.save_cv_to_json(cv_text, output_json_path)
    except Exception as e:
        print(f"Error parsing and saving CV: {e}")
        sys.exit(1)

    # --- Step 3: Read requirements ---
    print(f"Reading job requirements from: {requirements_path}")
    try:
        requirements = read_requirements_file(requirements_path)
    except Exception as e:
        print(f"Error reading requirements: {e}")
        sys.exit(1)

    # --- Step 4: Scrutinize candidate ---
    print("Loading parsed CV JSON...")
    cv_json = read_cv_json(output_json_path)

    print("Running Scrutinizer (LLM assessment)...")
    scrutinizer = Scrutinizer()
    try:
        assessment = scrutinizer.judge_candidate(requirements, cv_json)
        print("\n===== Candidate Assessment =====\n")
        print(assessment)
    except Exception as e:
        print(f"Error during scrutiny: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 