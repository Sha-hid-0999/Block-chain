import streamlit as st
import json
import os

# Path to the JSON file
LEDGER_FILE = "ledger.json"

# Function to load ledger from JSON file
def load_ledger():
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            return json.load(f)
    return []

# Function to save ledger to JSON file
def save_ledger(ledger):
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f)

# Initialize session state
if "ledger" not in st.session_state:
    st.session_state.ledger = load_ledger()

# Title
st.title("Simple Ledger Tracker with JSON Storage")

# Transaction input
transaction_input = st.number_input("Enter transaction amount", min_value=0, step=1)

# Add transaction button
if st.button("Add Transaction"):
    st.session_state.ledger.append(transaction_input)
    save_ledger(st.session_state.ledger)
    st.success(f"Transaction of {transaction_input} added to the ledger.")

# Display current ledger
st.subheader("Current Ledger:")
st.write(st.session_state.ledger)

# Clear ledger button
if st.button("Clear Ledger"):
    st.session_state.ledger = []
    save_ledger(st.session_state.ledger)
    st.info("Ledger has been cleared.")
