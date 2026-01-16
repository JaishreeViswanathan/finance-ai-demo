import streamlit as st
import pandas as pd
from openai import OpenAI

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(page_title="Personal Finance AI Coach", layout="centered")
st.title("💰 Personal Finance AI Coach")
st.write(
    "Upload your spending CSV to see your data summarized and receive AI-powered financial guidance."
)

# -----------------------------
# OpenAI API Key Input
# -----------------------------
api_key = st.text_input(
    "Enter your OpenAI API Key (kept private, not saved)", type="password"
)
client = OpenAI(api_key=api_key) if api_key else None

# -----------------------------
# CSV Upload
# -----------------------------
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        df.columns = df.columns.str.strip()

        if "Amount" not in df.columns:
            st.error("CSV must contain an 'Amount' column.")
            st.stop()

        expenses = df[df["Amount"] < 0]
        total_spent = abs(expenses["Amount"].sum())
        spending_by_category = (
            expenses.groupby("Category")["Amount"]
            .sum()
            .abs()
            .reset_index()
            .rename(columns={"Amount": "Total"})
        )

        subscriptions = expenses[
            expenses["Category"].str.lower() == "subscriptions"
        ]
        if not subscriptions.empty:
            sub_summary = (
                subscriptions.groupby("Description")["Amount"]
                .sum()
                .abs()
                .reset_index()
                .rename(columns={"Amount": "Total"})
            )

        # -----------------------------
        # Raw Data Table
        # -----------------------------
        st.subheader("📄 Raw Data")
        st.dataframe(df, use_container_width=True)

        # -----------------------------
        # Spending Summary
        # -----------------------------
        st.subheader("💸 Spending Summary")
        st.markdown(
            f"""
<div style='background-color:#F0F4C3; padding:12px; border-radius:8px; color:#333'>
<strong>Total Spent:</strong> ${total_spent:.2f}
</div>
""",
            unsafe_allow_html=True
        )

        st.subheader("Spending by Category")
        st.dataframe(spending_by_category, use_container_width=True)

        if not subscriptions.empty:
            st.subheader("Subscriptions")
            for _, row in sub_summary.iterrows():
                st.markdown(
                    f"""
<div style='background-color:#E1F5FE; padding:8px; border-radius:8px; color:#000'>
<strong>{row['Description']}</strong>: ${row['Total']:.2f}
</div>
""",
                    unsafe_allow_html=True
                )
        else:
            st.write("No subscriptions found in your data.")

        # -----------------------------
        # Prepare Personalized User Profile
        # -----------------------------
        top_categories = spending_by_category.sort_values(by="Total", ascending=False).head(3)
        top_categories_text = "\n".join([f"{row['Category']}: ${row['Total']:.2f}" for _, row in top_categories.iterrows()])

        subscriptions_text = ""
        if not subscriptions.empty:
            subscriptions_summary = sub_summary.sort_values(by="Total", ascending=False)
            subscriptions_text = "\n".join([f"{row['Description']}: ${row['Total']:.2f}" for _, row in subscriptions_summary.iterrows()])

        user_profile = f"""
Total Spent: ${total_spent:.2f}

Top Categories:
{top_categories_text}

Subscriptions:
{subscriptions_text if subscriptions_text else 'None'}
"""

        # -----------------------------
        # AI Financial Insights
        # -----------------------------
        st.divider()
        st.subheader("💡 AI Financial Insights")

        if st.button("Get AI Advice", key="ai_advice"):
            ai_response = None

            # Try OpenAI
            if client:
                try:
                    prompt = f"""
You are a calm, supportive financial coach.

Here is the user's spending profile:

{user_profile}

Give 3 short, actionable tips specifically tailored to their top spending categories and subscriptions.
Each tip should be no more than 2 sentences.
Make the advice practical, concise, and easy to implement.
"""
                    completion = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "You are a calm, supportive financial coach."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=300
                    )
                    ai_response = completion.choices[0].message.content

                except Exception:
                    st.warning(
                        "AI quota or API issue detected. Showing mock AI insights instead."
                    )

            # Fallback mock AI
            if not ai_response:
                ai_response = """
• Review your top spending category and find 1–2 ways to reduce it.
• Consider pausing or canceling underused subscriptions.
• Set up automated savings based on your usual spending patterns.
"""

            st.markdown(
                f"""
<div style='background-color:#FFF9C4; padding:12px; border-radius:10px; color:#000'>
{ai_response.replace(chr(10), '<br>')}
</div>
""",
                unsafe_allow_html=True
            )

        # -----------------------------
        # Chat Section
        # -----------------------------
        st.divider()
        st.subheader("💬 Ask the AI a Question")
        user_question = st.text_input("Example: How can I save $200/month?", key="chat_input")

        if user_question:
            chat_reply = None

            if client:
                try:
                    chat_prompt = f"""
You are a calm, supportive financial coach.
Answer the user's question concisely and give 1-2 actionable tips, each in 1-2 sentences.

User question: {user_question}
"""
                    chat = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "You are a calm, supportive financial coach."},
                            {"role": "user", "content": chat_prompt}
                        ],
                        max_tokens=200
                    )
                    chat_reply = chat.choices[0].message.content

                except Exception:
                    st.warning("AI quota or API issue detected. Showing mock response instead.")

            if not chat_reply:
                chat_reply = (
                    "Start by identifying one recurring expense to reduce, "
                    "then redirect that money into savings automatically."
                )

            st.markdown(
                f"""
<div style='background-color:#E0F7FA; padding:12px; border-radius:10px; color:#000'>
{chat_reply.replace(chr(10), '<br>')}
</div>
""",
                unsafe_allow_html=True
            )

    except Exception as e:
        st.error(f"Error processing file: {e}")
