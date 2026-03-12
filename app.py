import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SBI Bank App",
    page_icon="🏦",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size:40px;
    color:#0e4c92;
    font-weight:bold;
}

.card {
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Bank Class
class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Transaction Successful. Collected ₹{amount}"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Successful. Total Balance ₹{self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"Mobile Updated: {self.mobile_number}"

    def check_balance(self):
        return f"Total Balance: ₹{self.balance}"


# Session state
if "account" not in st.session_state:
    st.session_state.account = None


# Title
st.markdown('<p class="title">🏦 SBI Smart Banking System</p>', unsafe_allow_html=True)


# Sidebar
menu = ["Create Account", "Deposit", "Withdraw", "Update Mobile", "Check Balance"]
choice = st.sidebar.radio("📌 Select Option", menu)


# Create Account
if choice == "Create Account":

    st.subheader("📝 Create New Account")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        account_number = st.text_input("Account Number")
        age = st.number_input("Age", min_value=18)

    with col2:
        mobile = st.text_input("Mobile Number")
        balance = st.number_input("Initial Balance", min_value=0)

    if st.button("Create Account"):
        st.session_state.account = BankApplication(name, account_number, age, mobile, balance)
        st.success("✅ Account Created Successfully!")


# Deposit
elif choice == "Deposit":

    st.subheader("💰 Deposit Money")

    if st.session_state.account:
        amount = st.number_input("Enter Amount")

        if st.button("Deposit Money"):
            result = st.session_state.account.deposit(amount)
            st.success(result)
    else:
        st.warning("⚠ Create an account first")


# Withdraw
elif choice == "Withdraw":

    st.subheader("🏧 Withdraw Money")

    if st.session_state.account:
        amount = st.number_input("Enter Amount")

        if st.button("Withdraw Money"):
            result = st.session_state.account.withdraw(amount)
            st.success(result)
    else:
        st.warning("⚠ Create an account first")


# Update Mobile
elif choice == "Update Mobile":

    st.subheader("📱 Update Mobile Number")

    if st.session_state.account:
        new_mobile = st.text_input("Enter New Mobile Number")

        if st.button("Update Number"):
            result = st.session_state.account.update_mobile(new_mobile)
            st.success(result)
    else:
        st.warning("⚠ Create an account first")


# Check Balance
elif choice == "Check Balance":

    st.subheader("📊 Account Balance")

    if st.session_state.account:
        balance = st.session_state.account.check_balance()
        st.success(balance)
    else:
        st.warning("⚠ Create an account first")