import streamlit as st
from openai import OpenAI


st.set_page_config(
    page_title="Cold Mail Generator",
    page_icon="📧",
    layout="centered"
)

# --- HEADER ---
st.title("📧 Cold Mail Generator")
st.markdown(
    """
    Generate professional, personalized cold emails in seconds using AI. 
    Ideal for job applications, networking, and sales outreach.
    """
)

# --- SIDEBAR SETTINGS ---
with st.sidebar:
    st.header("⚙️ Settings")
    
    
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
        st.success("✅ API Key loaded from Secrets")
    except (FileNotFoundError, KeyError):
        api_key = st.text_input("Enter OpenRouter API Key", type="password")
        st.caption("Get your key at [openrouter.ai/keys](https://openrouter.ai/keys)")

    st.divider()

    # Model Selection
    model_option = st.selectbox(
        "Choose AI Model",
        options=[
            "google/gemini-2.0-flash-exp:free",
            "meta-llama/llama-3-8b-instruct:free",
            "mistralai/mistral-7b-instruct:free"
        ],
        index=0
    )

    # Advanced Parameters
    tone = st.selectbox(
        "Email Tone",
        ["Professional", "Casual", "Persuasive", "Urgent", "Friendly"]
    )
    
    temperature = st.slider(
        "Creativity Level",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        help="Higher values make the email more creative; lower values make it more focused."
    )

    st.markdown("---")
    st.markdown("Built by [Harshitha A](#)")


# --- MAIN FORM ---
with st.form("email_form"):
    col1, col2 = st.columns(2)
    with col1:
        recipient_name = st.text_input("Recipient Name", placeholder="e.g., Jane Doe")
        company_name = st.text_input("Company Name", placeholder="e.g., Tech Corp")
    with col2:
        my_name = st.text_input("Your Name", placeholder="e.g., John Smith")
        my_role = st.text_input("Your Role/Product", placeholder="e.g., Data Analyst")
        
    value_proposition = st.text_area(
        "Key Message / Value Proposition", 
        placeholder="e.g., I have built a predictive model that can increase your sales by 20%...",
        height=150
    )
    
    submit_button = st.form_submit_button("Generate Email 🚀")

# --- GENERATION LOGIC ---
if submit_button:
    if not api_key:
        st.error("❌ Please provide an API Key in the sidebar to proceed.")
    elif not value_proposition:
        st.warning("⚠️ Please enter a value proposition.")
    else:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

        prompt = f"""
        Write a cold email with the following details:
        
        Sender: {my_name} ({my_role})
        Recipient: {recipient_name} at {company_name}
        Tone: {tone}
        Key Message: {value_proposition}
        
        Structure:
        1. Subject Line (Catchy)
        2. Personalized Greeting
        3. The "Hook" (Why I'm writing)
        4. Value Proposition (How I can help)
        5. Call to Action (Next steps)
        6. Sign-off
        
        Keep it concise (under 200 words).
        """

        try:
            with st.spinner("🤖 AI is drafting your email..."):
                completion = client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": "https://cold-email-gen.streamlit.app",
                        "X-Title": "Cold Email Generator",
                    },
                    model=model_option,
                    messages=[
                        {"role": "system", "content": f"You are an expert copywriter specializing in {tone.lower()} cold outreach."},
                        {"role": "user", "content": prompt},
                    ],
                    max_tokens=500,
                    temperature=temperature
                )
                
                email_content = completion.choices[0].message.content

            st.subheader("📝 Generated Email")
            
            # Display in code block for easy copying
            st.code(email_content, language="markdown")
            
            # Download Button
            st.download_button(
                label="📥 Download Email (.txt)",
                data=email_content,
                file_name="cold_email.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")