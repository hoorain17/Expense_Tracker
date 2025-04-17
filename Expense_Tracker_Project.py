# Expense_Tracker_Streamlit.py
import streamlit as st

st.set_page_config(page_title="Expense Tracker", page_icon="💰")

st.title("💸 Expense Tracker & Financial Health Checker")
st.write("Welcome! Let's understand your finances and boost your savings. 🚀")

# --- User Info ---
name = st.text_input("Enter your name:")
profession = st.text_input("Enter your profession:")

if name and profession:
    st.subheader(f"Hello {name}, a {profession}. Let's review your finances!")

# --- Monthly Income & Expenses ---
income = st.number_input("Enter your monthly income:", min_value=0.0, format="%.2f")

if income > 0:
    expenses = st.number_input("Enter your total monthly expenses:", min_value=0.0, max_value=income, format="%.2f")

    if expenses <= income:
        # --- Savings ---
        savings = income - expenses
        savings_pct = (savings / income) * 100

        st.success(f"💰 Savings this month: {savings:.2f} ({savings_pct:.2f}%)")

        # --- Financial Health ---
        if savings_pct >= 20:
            st.info(f"Great job, {name}! You have a strong savings habit.")
        elif 10 <= savings_pct < 20:
            st.warning(f"Not bad, {name}, but try saving a bit more.")
        else:
            st.error(f"Careful, {name}! Your savings are low. Try reducing expenses.")

        # --- Expense Breakdown ---
        st.subheader("📊 Let's break down your spending:")

        essentials = st.number_input("Essentials (rent, groceries):", min_value=0.0, format="%.2f")
        wants = st.number_input("Wants (fun, entertainment):", min_value=0.0, format="%.2f")
        investments = st.number_input("Savings / Investments:", min_value=0.0, format="%.2f")

        total_breakdown = essentials + wants + investments

        if round(total_breakdown, 2) == round(income, 2):
            essentials_pct = (essentials / income) * 100
            wants_pct = (wants / income) * 100
            investments_pct = (investments / income) * 100

            st.write("### 💡 Money Distribution:")
            st.progress(essentials_pct / 100, text=f"Essentials: {essentials_pct:.2f}%")
            st.progress(wants_pct / 100, text=f"Wants: {wants_pct:.2f}%")
            st.progress(investments_pct / 100, text=f"Savings/Investments: {investments_pct:.2f}%")

            # --- Savings Goal ---
            goal = st.slider("Set your savings goal (% of income):", min_value=1, max_value=100, value=20)
            st.write(f"📈 Your current savings: {savings_pct:.2f}% | Goal: {goal}%")

            if savings_pct >= goal:
                st.success(f"🎉 Congrats {name}, you’ve met your savings goal!")
            else:
                gap = goal - savings_pct
                st.warning(f"You're {gap:.2f}% away from your goal. Keep going!")

            # --- Summary ---
            summary = f"""
==================== Financial Summary ====================
Name: {name}
Profession: {profession}

Monthly Income: {income}
Monthly Expenses: {expenses}
Monthly Savings: {savings} ({savings_pct:.2f}%)

Breakdown:
- Essentials: {essentials_pct:.2f}%
- Wants: {wants_pct:.2f}%
- Savings/Investments: {investments_pct:.2f}%

Savings Goal: {goal}%
Status: {"Goal Achieved ✅" if savings_pct >= goal else f"{gap:.2f}% away from goal ❗"}

===========================================================
"""

            st.text_area("📄 Your Financial Summary", summary, height=300)

            # --- File Download ---
            st.download_button("📥 Download Summary as Text File", summary, file_name="financial_summary.txt")
        else:
            st.warning("⚠️ Your breakdown does not match your income. Please adjust the numbers.")
