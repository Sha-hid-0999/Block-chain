import streamlit as st

# Title of the app
st.title("Simple Ledger Tracker")

# Initialize session state to store the ledger across interactions
if "ledger" not in st.session_state:
    st.session_state.ledger = []

# Function to add transaction
def add_transaction(transaction):
    st.session_state.ledger.append(transaction)
    st.success(f"Transaction of {transaction} added to the ledger.")

# Input for transaction amount
transaction_input = st.number_input("Enter transaction amount", min_value=0, step=1)

# Button to add transaction
if st.button("Add Transaction"):
    add_transaction(transaction_input)

# Display the current ledger
st.subheader("Current Ledger:")
st.write(st.session_state.ledger)

# Optional: Clear the ledger
if st.button("Clear Ledger"):
    st.session_state.ledger = []
    st.info("Ledger has been cleared.")
