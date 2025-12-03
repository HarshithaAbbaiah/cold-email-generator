# 📧 AI Cold Email Generator

A professional AI-powered tool designed to automate the process of writing personalized cold emails for job applications, sales outreach, and networking. Built with Python and Streamlit, this application leverages Large Language Models (LLMs) via the OpenRouter API to generate high-quality, context-aware drafts.

# 🚀 Features

**Multi-Model Support:** Choose between powerful free models like Google Gemini 2.0 Flash, Llama 3, and Mistral 7B.

T**one Customization:** Select the perfect tone for your recipient (Professional, Casual, Urgent, etc.).

**Creativity Control:** Adjust the "Temperature" slider to control how creative or focused the AI should be.

**Instant Download:** Generate and download your email as a .txt file with one click.

**Secure API Handling:** Input your API key securely via the UI or Streamlit Secrets.

# 🛠️ Tech Stack

**Frontend:** Streamlit (Python web framework)

**AI Logic:** OpenAI Client (connected to OpenRouter)

**Language:** Python 3.x

# ⚙️ Installation & Setup

## Follow these steps to run the project locally on your machine.

### 1. Clone the Repository

git clone [https://github.com/YOUR_USERNAME/cold-email-generator.git](https://github.com/YOUR_USERNAME/cold-email-generator.git)
cd cold-email-generator


### 2. Install Dependencies

Make sure you have Python installed. Then run:

pip install -r requirements.txt


### 3. Run the App

streamlit run app.py


The app will open automatically in your browser at http://localhost:8501.

**🔑 API Key Configuration**

To use the AI features, you need a free API Key from OpenRouter.

**Go to OpenRouter**.ai/keys and create a key.

**Option A (Temporary):** Paste the key directly into the sidebar of the app when running.

**Option B (Permanent/Cloud):**

Locally: Create a file .streamlit/secrets.toml and add:

OPENROUTER_API_KEY = "sk-or-v1-..."


On Streamlit Cloud: Go to App Settings -> Secrets and paste the same line.

# 📂 Project Structure

├─ app.py                # Main application logic

├─ requirements.txt      # List of dependencies

├─ README.md             # Project documentation

└─ .streamlit/           # (Optional) Local secrets configuration


# 👤 Author

**Harshitha A**

AI, ML & GenAI Enthusiast Committed to Continuous Learning

Always eager to learn and explore new technologies in AI and Machine Learning.
