# Resume-Job Match Analyzer

## Student Name
Claire Cavanaugh

## App Description
The Resume-Job Match Analyzer is a Streamlit web app that shows users how well their resume matches a specific job posting. Users paste in their resume and a job description, and the app finds the most important keywords in the posting, checks which ones appear in the resume, and gives a match score. It then lists the matched and missing keywords and shows a chart of the top terms, so users know exactly what to add or tailor before they apply.

## Intended Users
This app is intended for college students and recent graduates applying to internships and entry-level jobs, especially those sending many applications who want a fast way to tailor their resume to each posting and get past keyword-based applicant tracking systems.

## Current Features (Implemented)
- Two text boxes to paste a resume and a job description
- A slider to choose how many top job keywords to check (5–30)
- A checkbox to filter out common job-posting filler words
- Keyword extraction that finds the most frequent meaningful terms in the job posting
- A match score (percentage) with a progress bar and a color-coded rating
- Side-by-side lists of matched and missing keywords
- A bar chart and table of the top keywords, showing whether each is in the resume

## Planned Features (Final Version)
- Upload a resume as a PDF or TXT file instead of pasting text
- Recognize multi-word skills (e.g., "project management", "data analysis")
- Tips for where to add each missing keyword in the resume
- Save and compare match scores across multiple job postings
- Download a summary report of the results

## How to Run Locally
```
pip install -r requirements.txt
streamlit run app.py
```
