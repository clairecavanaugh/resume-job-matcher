import re
from collections import Counter

import pandas as pd
import streamlit as st

# Common words that don't tell us anything about a job's skills.
STOP_WORDS = {
    "a", "about", "above", "after", "all", "also", "an", "and", "any", "are",
    "as", "at", "be", "been", "being", "both", "but", "by", "can", "could",
    "do", "does", "each", "for", "from", "has", "have", "how", "if", "in",
    "into", "is", "it", "its", "may", "more", "most", "must", "not", "of",
    "on", "or", "other", "our", "out", "over", "own", "per", "should", "so",
    "such", "than", "that", "the", "their", "them", "then", "there", "these",
    "they", "this", "those", "through", "to", "under", "up", "us", "via",
    "was", "we", "were", "what", "when", "where", "which", "while", "who",
    "will", "with", "within", "would", "you", "your",
}

# Words that show up in almost every job posting but aren't real skills.
JOB_FILLER_WORDS = {
    "ability", "able", "candidate", "candidates", "company", "experience",
    "including", "job", "join", "looking", "opportunity", "position",
    "preferred", "required", "seek", "seeking", "requirements", "responsibilities", "role",
    "skills", "strong", "team", "work", "working", "year", "years",
}


def get_words(text):
    """Turn text into a list of lowercase words (keeps terms like c++ or excel)."""
    return re.findall(r"[a-z][a-z0-9+#.\-]*[a-z0-9+#]|[a-z]", text.lower())


def get_top_keywords(job_text, how_many, ignore_filler):
    """Find the most frequent meaningful words in the job posting."""
    words_to_skip = STOP_WORDS | JOB_FILLER_WORDS if ignore_filler else STOP_WORDS
    words = [w for w in get_words(job_text) if w not in words_to_skip and len(w) > 2]
    return Counter(words).most_common(how_many)


# ---------- Page setup ----------
st.set_page_config(page_title="Resume-Job Match Analyzer", page_icon="📄")

st.title("Resume-Job Match Analyzer")
st.write(
    "See how well your resume matches a job posting. Paste both below, and the app "
    "will pull out the posting's most important keywords, give you a match score, "
    "and show which keywords your resume is missing."
)

# ---------- Inputs ----------
col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area(
        "1. Paste your resume",
        height=250,
        placeholder="Copy and paste the text of your resume here...",
    )

with col2:
    job_text = st.text_area(
        "2. Paste the job description",
        height=250,
        placeholder="Copy and paste the job posting here...",
    )

st.subheader("Settings")
num_keywords = st.slider(
    "How many top keywords from the job posting should be checked?",
    min_value=5,
    max_value=30,
    value=15,
)
ignore_filler = st.checkbox(
    "Ignore common job-posting words (like 'team', 'experience', 'role')",
    value=True,
)

# ---------- Results ----------
st.divider()

if not resume_text.strip() or not job_text.strip():
    st.info("👆 Paste your resume and a job description above to see your results.")
else:
    top_keywords = get_top_keywords(job_text, num_keywords, ignore_filler)
    resume_words = set(get_words(resume_text))

    matched = [word for word, count in top_keywords if word in resume_words]
    missing = [word for word, count in top_keywords if word not in resume_words]

    if not top_keywords:
        st.warning("No keywords were found in the job description. Try pasting more text.")
    else:
        score = round(len(matched) / len(top_keywords) * 100)

        st.subheader("Your Match Score")
        st.metric("Keyword match", f"{score}%", help="Share of the top job keywords found in your resume")
        st.progress(score / 100)

        if score >= 75:
            st.success("Strong match! Your resume covers most of the key terms.")
        elif score >= 50:
            st.warning("Decent match. Adding a few missing keywords could help.")
        else:
            st.error("Low match. Consider tailoring your resume to this posting.")

        left, right = st.columns(2)
        with left:
            st.markdown(f"**✅ Keywords you have ({len(matched)})**")
            st.write(", ".join(matched) if matched else "None yet")
        with right:
            st.markdown(f"**❌ Keywords you're missing ({len(missing)})**")
            st.write(", ".join(missing) if missing else "None. Nice work!")

        st.subheader("Top Keywords in the Job Posting")
        chart_data = pd.DataFrame(top_keywords, columns=["Keyword", "Times mentioned"])
        chart_data["In your resume?"] = chart_data["Keyword"].apply(
            lambda word: "Yes" if word in resume_words else "No"
        )
        st.bar_chart(
            chart_data,
            x="Keyword",
            y="Times mentioned",
            color="In your resume?",
            horizontal=True,
        )
        st.dataframe(chart_data, hide_index=True, width="stretch")
