import streamlit as st
import pandas as pd
import openai  # For LLM integration (OpenRouter API compatible)

# ---------- Categorization ----------
def categorize(description):
    desc = description.lower()
    if any(x in desc for x in ["swiggy", "zomato", "uber eats", "starbucks", "domino", "breakfast"]):
        return "Food"
    elif any(x in desc for x in ["amazon", "flipkart", "myntra", "big bazaar", "reliance"]):
        return "Shopping"
    elif any(x in desc for x in ["salary", "payment", "freelance"]):
        return "Salary"
    elif "bookmyshow" in desc:
        return "Entertainment"
    elif "tata sky" in desc:
        return "Recharge"
    elif "uber" in desc:
        return "Transport"
    else:
        return "Others"

# ---------- Streamlit App ----------
st.set_page_config(page_title="UPI CSV Spending Analyzer", layout="wide")
st.title("📊 UPI CSV Spending Analyzer + AI Financial Tips")

uploaded_file = st.file_uploader("Upload your UPI Transaction CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Expect CSV with at least: Date, Amount, Description
    expected_columns = ["Date", "Amount", "Description"]
    if all(col in df.columns for col in expected_columns):
        df["Category"] = df["Description"].apply(categorize)
        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors='coerce')
        df.dropna(subset=["Date"], inplace=True)
        df["Month"] = df["Date"].dt.strftime("%b-%Y")

        monthly_spending = df.groupby("Month")["Amount"].sum()
        category_spending = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

        st.success(" Transactions Processed & Categorized!")

        st.subheader("🗂️ Full Transaction Table")
        st.dataframe(df, use_container_width=True)

        st.subheader("📅 Monthly Spending Overview")
        st.bar_chart(monthly_spending)

        st.subheader("🏷️ Spending by Category")
        st.bar_chart(category_spending)

        # ---------- LLM Prompt ----------
        monthly_spending_str = "\n".join(
            [f"{month}: ₹{amount:,.2f}" for month, amount in monthly_spending.items()]
        )
        category_spending_str = "\n".join(
            [f"{category}: ₹{amount:,.2f}" for category, amount in category_spending.items()]
        )
        prompt = f"""
        You are a financial advisor. Based on the following monthly and category-wise spending in Indian Rupees (₹), provide 3 personalized financial tips.

        Monthly Spending:
        {monthly_spending_str}

        Category-wise Spending:
        {category_spending_str}
        """

        st.subheader("🤖 Personalized Financial Advice")

        if st.button("Generate Financial Tips (AI)"):
            with st.spinner("Connecting to LLM for financial guidance..."):
                client = openai.OpenAI(
                 
                    api_key="sk-or-v1-api_key=\"your api key update ",  # Your API Key here
                    base_url="https://openrouter.ai/api/v1"
                )
                try:
                    response = client.chat.completions.create(
                        model="openrouter/auto",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error("❌ Failed to get response from LLM")
                    st.exception(e)
    else:
        st.error(f"⚠️ CSV must have columns: {expected_columns}")
