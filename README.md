# AI Resume Screening System

A simple AI-inspired resume screening tool that helps recruiters shortlist candidates by comparing resumes with a job description.

## Problem
HR teams receive many resumes and need a quick way to identify candidates that best match a job role.

## Solution
This system automatically analyzes resumes and compares them with a Machine Learning Engineer job description to generate candidate rankings.

## How It Works
1. Input resumes (PDF files) and a job description.
2. Extract text from resumes using `pdfplumber`.
3. Compare resume content with required ML engineer skills.
4. Calculate a match score (0–100).
5. Generate strengths, gaps, and a final recommendation.

## Output
The system produces a structured `output.csv` containing:
- Candidate name
- Match score
- Key strengths
- Skill gaps
- Final recommendation (Strong Fit / Moderate Fit / Not Fit)

## Tech Stack
- Python
- pdfplumber
- pandas

## How to Run
```bash
pip install pdfplumber pandas
python resume_screening.py
