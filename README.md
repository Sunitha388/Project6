# Project6
Personal UPI Usage and Financial Analyzer using LLMs


📊 Personal UPI Usage and Financial Analyzer using LLMs
A powerful personal finance analysis tool that helps you track, categorize, and analyze your UPI transactions with the assistance of Large Language Models (LLMs). This project combines financial data analytics with natural language processing to provide insightful summaries and visualizations of your spending habits.

🌟 Features
📂 Upload UPI Transaction Data (CSV or PDF)

🏷️ Automatic Transaction Categorization (Food, Shopping, Bills, etc.)

📅 Monthly Spending Summaries

📊 Visual Insights (Pie Charts, Bar Graphs, Trends)

🗂️ Top Merchants and Frequent Payees

🔎 Keyword Search and Filters

🤖 AI-powered Summarization of Financial Behavior using LLMs

💾 Download Processed Data

⚡ Interactive Streamlit Web Interface

🖥️ Demo
Coming Soon 🚀

🛠️ Tech Stack
# Technology	Purpose
# Python	Core programming language
# Streamlit	Building the interactive UI
# Pandas	Data manipulation & analysis
# Matplotlib / Seaborn	Visualizations
# PyMuPDF / pdfminer	PDF extraction
# OpenAI API / OpenRouter	LLM integration
# Regex	Keyword-based transaction parsing

📂 Project Structure
graphql
Copy
Edit
personal-upi-financial-analyzer/
├── app.py                # Main Streamlit app
├── utils.py              # Functions: data parsing, categorization
├── sample_data/          # Example UPI transaction files
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── LICENSE               # License information

🚀 Getting Started
1️⃣ Clone the Repository
bash
eg:
git clone https://github.com/your-username/personal-upi-financial-analyzer.git
cd personal-upi-financial-analyzer




2️⃣ Install Dependencies

pip install -openai,pymupdf

3️⃣ Run the App

streamlit run app.py

4️⃣ Upload your UPI transaction file and start analyzing!

📄 Example Data Format
Date	Amount	Description	Category
2025-05-12	₹500	UPI PAYMENT TO ZOMATO	Food
2025-05-13	₹1,200	UPI PAYMENT TO AMAZON	Shopping


⚙️ Customization Options
🖋️ Edit utils.py to customize or add new categories.

⚡ API Integration: Update OPENAI_API_KEY in your code for LLM usage.

🎨 Visuals: Modify visualization code to change colors/themes.


📌 Future Roadmap
📥 Automated PDF → CSV extraction

💡 Smart budget recommendations

📈 Income vs Expense charts

🌐 Deploy to Streamlit Cloud







