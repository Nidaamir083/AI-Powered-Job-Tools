import streamlit as st
import openai
import os
from datetime import datetime

# Set up OpenAI API
openai.api_key = st.secrets["OPENAI_API_KEY"]

# App title and config
st.set_page_config(page_title="AI-Powered Job Tools", page_icon="💼")
st.title("AI-Powered Job Tools")
st.markdown("Generate tailored **About Me** sections and **cover letters** for your job applications")

# Initialize session state
if 'about_me' not in st.session_state:
    st.session_state.about_me = ""
if 'cover_letter' not in st.session_state:
    st.session_state.cover_letter = ""

# Sidebar for user inputs
with st.sidebar:
    st.header("Your Information")
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    linkedin = st.text_input("LinkedIn Profile")
    portfolio = st.text_input("Portfolio/Website")
    years_experience = st.slider("Years of Experience", 0, 30, 3)
    skills = st.text_area("Your Skills (comma separated)", "Python, Data Analysis, SQL, Machine Learning")
    achievements = st.text_area("Key Achievements (bullet points work best)", 
                              "- Increased sales by 30% through data-driven marketing\n- Led team of 5 analysts\n- Built predictive model with 95% accuracy")

# Tab layout
tab1, tab2 = st.tabs(["About Me Generator", "Cover Letter Generator"])

# About Me Generator Tab
with tab1:
    st.subheader("Tailored About Me Section")
    job_description = st.text_area("Paste the job description here", height=200, key="about_me_jd")
    
    if st.button("Generate About Me Section"):
        if not job_description:
            st.warning("Please enter a job description")
        else:
            with st.spinner("Generating your tailored About Me section..."):
                prompt = f"""
                Create a professional 'About Me' section for a job application using these details:
                - Candidate Name: {name}
                - Years of Experience: {years_experience}
                - Skills: {skills}
                - Achievements: {achievements}
                - Target Job Description: {job_description}

                The section should:
                1. Be 3-4 concise paragraphs (150-200 words total)
                2. Highlight relevant skills and experiences
                3. Show quantifiable achievements
                4. Match the tone of the job description
                5. Use professional but approachable language
                6. Include a call to action at the end
                """
                
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a professional career coach helping candidates create compelling personal summaries."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=400
                )
                
                st.session_state.about_me = response.choices[0].message.content
                
            st.success("Generated About Me Section")
            st.text_area("Generated Content", st.session_state.about_me, height=300)
            
            # Download button
            st.download_button(
                label="Download About Me Section",
                data=st.session_state.about_me,
                file_name=f"about_me_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain"
            )

# Cover Letter Generator Tab
with tab2:
    st.subheader("AI-Powered Cover Letter")
    job_description = st.text_area("Paste the job description here", height=200, key="cover_letter_jd")
    hiring_manager = st.text_input("Hiring Manager Name (optional)")
    company = st.text_input("Company Name")
    job_title = st.text_input("Job Title")
    
    if st.button("Generate Cover Letter"):
        if not job_description or not company or not job_title:
            st.warning("Please fill in required fields: job description, company name, and job title")
        else:
            with st.spinner("Generating your personalized cover letter..."):
                prompt = f"""
                Write a professional cover letter using these details:
                - Candidate Name: {name}
                - Contact Info: {email} | {phone} | {linkedin}
                - Years of Experience: {years_experience}
                - Skills: {skills}
                - Achievements: {achievements}
                - Target Company: {company}
                - Job Title: {job_title}
                - Hiring Manager: {hiring_manager if hiring_manager else 'Hiring Manager'}
                - Job Description: {job_description}

                The cover letter should:
                1. Be 3-4 paragraphs (300-400 words total)
                2. Start with a strong opening paragraph showing enthusiasm
                3. Highlight 2-3 most relevant skills with examples
                4. Include 1-2 quantifiable achievements
                5. Show knowledge of the company
                6. End with a call to action
                7. Use professional but not overly formal tone
                """
                
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a professional resume writer creating compelling cover letters."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=600
                )
                
                st.session_state.cover_letter = response.choices[0].message.content
                
                # Format with proper letter structure
                formatted_letter = f"""
                {datetime.now().strftime('%B %d, %Y')}

                {hiring_manager if hiring_manager else 'Hiring Manager'}
                {company}
                
                Dear {'Mr./Ms. ' + hiring_manager.split()[0] if hiring_manager else 'Hiring Manager'},

                {st.session_state.cover_letter}

                Sincerely,
                {name}
                """
                
            st.success("Generated Cover Letter")
            st.text_area("Generated Content", formatted_letter, height=400)
            
            # Download button
            st.download_button(
                label="Download Cover Letter",
                data=formatted_letter,
                file_name=f"cover_letter_{company.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain"
            )

# How to use section
with st.expander("How to get the best results"):
    st.markdown("""
    **For best results:**
    
    1. **Complete all fields** in the sidebar with your information
    2. **Copy the full job description** from the posting
    3. **Include specific achievements** with numbers/impact
    4. **Review and edit** the generated content to personalize it
    5. **Save multiple versions** for different job types
    
    The AI will match your skills to the job requirements, but you should always:
    - Verify accuracy of facts and numbers
    - Adjust tone if needed
    - Add personal touches
    """)

# Footer
st.markdown("---")
st.markdown("💡 *Tip: For more personalized results, edit the generated content with specific examples from your experience.*")
