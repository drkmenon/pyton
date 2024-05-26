
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def calculate_years_to_retirement(income, expenses, savings_rate, annual_return, withdrawal_rate, initial_balance):
    annual_savings = income * savings_rate
    total_balance = initial_balance
    years = 0
    balances = [total_balance]
    while total_balance * withdrawal_rate < expenses:
        total_balance = total_balance * (1 + annual_return) + annual_savings
        balances.append(total_balance)
        years += 1
    return years, balances

st.title("Early Retirement Calculator")

income = st.number_input("Annual Income (₹):", min_value=0, value=70000, step=1000)
initial_balance = st.number_input("Initial Balance (₹):", min_value=0, value=0, step=1000)
savings_rate = st.number_input("Savings Rate (%):", min_value=0.0, max_value=100.0, value=20.0, step=0.5) / 100
annual_return = st.number_input("Annual Return Rate (%):", min_value=0.0, max_value=100.0, value=5.0, step=0.5) / 100
withdrawal_rate = st.number_input("Safe Withdrawal Rate (%):", min_value=0.0, max_value=100.0, value=4.0, step=0.5) / 100
expenses = st.number_input("Annual Expenses (₹):", min_value=0, value=25200, step=1000)

if st.button("Calculate"):
    years, balances = calculate_years_to_retirement(income, expenses, savings_rate, annual_return, withdrawal_rate, initial_balance)
    st.write(f"You can retire in approximately {years} years.")

