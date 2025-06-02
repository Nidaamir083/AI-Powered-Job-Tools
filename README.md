# AI-Powered-Job-Tools
# AI-Powered Job Tools

A Streamlit application that generates tailored "About Me" sections and cover letters based on job descriptions using OpenAI's GPT-3.5.

## Features

- **About Me Generator**: Creates professional personal summaries tailored to specific job descriptions
- **Cover Letter Generator**: Produces customized cover letters matching your skills to job requirements
- **Personalization**: Incorporates your experience, skills, and achievements
- **Downloadable Results**: Save generated content as text files

## Deployment

1. **Streamlit Cloud** (Recommended):
   - Fork this repository
   - Go to [Streamlit Cloud](https://share.streamlit.io/)
   - Click "New app" and connect your GitHub account
   - Select your forked repository and main branch
   - Set `OPENAI_API_KEY` as a secret in your app settings
   - Click "Deploy"

2. **Local Installation**:
   ```bash
   git clone https://github.com/your-username/ai-job-tools.git
   cd ai-job-tools
   pip install -r requirements.txt
   streamlit run app.py
