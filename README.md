# 💰 Personal Finance AI Dashboard

**AI-powered personal finance prototype** built with Streamlit that helps users track spending, summarize expenses, and receive actionable AI financial insights.  

This project demonstrates **prototyping, AI integration, and executive-ready dashboard design**

---

## 🔹 Features

- **CSV Upload:** Upload your expense data in a simple CSV file.
- **Spending Summary:** See total expenses and breakdown by category.
- **Subscriptions Tracking:** Identify and summarize recurring subscriptions.
- **AI Financial Insights:** Personalized, concise tips based on your actual spending data.
- **Interactive AI Chat:** Ask questions like “How can I save $200/month?” and get actionable advice.
- **Demo-Proof:** Works even if API limits are reached, with fallback mock AI tips.
- **Clean, Readable Design:** Styled tables, colored boxes, and clear visual hierarchy for easy understanding.

---

## 📈 How It Works

1. Upload a CSV with these headers: `Date`, `Description`, `Category`, `Amount`.
2. The app displays:
   - Raw transactions
   - Total spending
   - Spending by category
   - Subscription summary
3. Click **Get AI Advice** to see **personalized tips** based on your top spending categories and subscriptions.
4. Ask follow-up questions in the **chat box** for additional guidance.

---

## ⚙️ Tech Stack

- **Streamlit** – Web app framework for Python
- **Pandas** – Data analysis
- **OpenAI GPT** – AI insights & interactive chat
- **Python 3.14** – Backend language

---

##  Why This Project Matters

- Demonstrates **AI prototyping** without needing a full production backend
- Shows ability to **analyze real-world data** and provide actionable recommendations
- Perfect for **resume or portfolio** to highlight AI, Python, and product thinking skills

---

##  Run Locally

```bash
# Clone the repo
git clone https://github.com/JaishreeViswanathan/finance-ai-demo.git
cd finance-ai-demo

# Install dependencies
python3 -m pip install streamlit pandas openai

# Run the app
streamlit run app.py
