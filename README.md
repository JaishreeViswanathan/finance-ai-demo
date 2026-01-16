# 💰 Personal Finance AI Dashboard

**AI-powered personal finance prototype** that transforms raw spending data into **actionable insights**. 
This project demonstrates how AI can be leveraged to improve financial awareness, guide decision-making, and prototype innovative solutions quickly.

---

## 🔹 Key Features

- **CSV Upload:** Easily import expense data from any source.  
- **Spending Summary:** Quickly see total expenses and breakdown by category.  
- **Subscription Management:** Identify recurring subscriptions and highlight high-cost items.  
- **AI Financial Insights:** Personalized, concise recommendations based on real spending data.  
- **Interactive AI Chat:** Ask targeted questions, such as “How can I reduce my monthly spending?” and receive practical guidance.  
- **Demo-Proof:** Fallback mock AI ensures uninterrupted experience even without API access.

---

## 📈 How It Works

1. Upload a CSV with headers: `Date`, `Description`, `Category`, `Amount`.  
2. The app displays:
   - Raw transactions  
   - Total spending and category breakdown  
   - Subscription summary  
3. Click **Get AI Advice** for **personalized tips** based on top spending categories and subscriptions.  
4. Use the **chat box** to ask follow-up questions for actionable guidance.  

---

## ⚙️ Technology Overview

- **Streamlit** – Rapid, interactive web app interface  
- **Pandas** – Data analysis and aggregation  
- **OpenAI GPT** – AI-powered insights and interactive chat  
- **Python 3.14** – Backend language  

---

## 💡 Why This Project Matters to Executives

- Demonstrates how **AI can convert raw financial data into actionable insights**, supporting better business or personal decision-making.  
- Shows the ability to **prototype solutions quickly** without full-scale production, reducing time and cost for testing concepts.  
- Highlights how **data-driven recommendations** can increase efficiency, control costs, and enhance financial discipline.  
- Provides a **tangible example of AI-enabled product thinking** that executives can evaluate for innovation potential.

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/JaishreeViswanathan/finance-ai-demo.git
cd finance-ai-demo

# Install dependencies
python3 -m pip install streamlit pandas openai

# Run the app
streamlit run app.py

