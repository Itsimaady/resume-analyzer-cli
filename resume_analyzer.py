import fitz  # PyMuPDF
import argparse
from termcolor import colored

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text.lower()

def load_skills(file_path="skills.txt"):
    with open(file_path, 'r') as f:
        return [line.strip().lower() for line in f.readlines()]

def analyze_skills(resume_text, skills_list):
    found_skills = []
    missing_skills = []
    for skill in skills_list:
        if skill in resume_text:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)
    return found_skills, missing_skills

def display_results(found, missing):
    print(colored("\n✅ Skills Found in Resume:", "green", attrs=["bold"]))
    for skill in found:
        print(f"  - {skill}")
    print(colored("\n❌ Skills Missing (Consider adding):", "red", attrs=["bold"]))
    for skill in missing:
        print(f"  - {skill}")

def main():
    parser = argparse.ArgumentParser(description="📄 Resume Analyzer CLI")
    parser.add_argument("pdf_file", help="Path to the resume PDF file")
    args = parser.parse_args()

    print(colored("\n📂 Analyzing Resume:", "cyan"), args.pdf_file)

    resume_text = extract_text_from_pdf(args.pdf_file)
    skills_list = load_skills()
    found, missing = analyze_skills(resume_text, skills_list)
    display_results(found, missing)

if __name__ == "__main__":
    main()
