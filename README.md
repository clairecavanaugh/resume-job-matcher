# Resume-Job Match Analyzer

## Student Name
Claire Cavanaugh

## App Description
This app will help users see how well their resume matches a specific job posting before they apply. Users will paste in (or upload) their resume and a job description, and the app will compare the two to find the important keywords and skills the job asks for. It will then show a match score, list which keywords the resume already covers, and highlight the ones that are missing so the user knows exactly what to strengthen or tailor.

## Intended Users
This app is intended for college students and recent graduates applying to internships and entry-level jobs, especially those sending many applications who want a fast way to tailor their resume to each posting and get past keyword-based applicant tracking systems.

## Planned Features
- Text boxes to paste a resume and a job description (with optional PDF/TXT resume upload)
- Keyword extraction that pulls the most important skills and terms from the job posting
- A match score showing what percentage of key terms appear in the resume
- Side-by-side lists of matched and missing keywords
- A chart of the top keywords in the job posting and whether each is covered

## How to Run Locally
```
pip install -r requirements.txt
streamlit run app.py
```
