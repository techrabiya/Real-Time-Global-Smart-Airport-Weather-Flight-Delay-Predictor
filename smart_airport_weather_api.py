import streamlit as st
import random
import string

st.title("🛡️ Rabia's Advanced Password Security Suite")
st.write("Evaluate password entropy, complexity metrics, and generate secure keys instantly.")

user_pwd = st.text_input("Enter password for security evaluation:", type="password")

if user_pwd:
    length = len(user_pwd) >= 10
    digit = any(c.isdigit() for c in user_pwd)
    upper = any(c.isupper() for c in user_pwd)
    special = any(c in string.punctuation for c in user_pwd)
    
    score = sum([length, digit, upper, special])
    
    st.markdown("---")
    st.write(f"**Target Password:** `{user_pwd}`")
    
    if score == 4:
        st.success("Security Status: 🟢 ENTERPRISE GRADE (Maximum Strength)")
    elif score >= 2:
        st.warning("Security Status: 🟡 MODERATE (Upgrade Recommended)")
    else:
        st.error("Security Status: 🔴 VULNERABLE (High Risk)")
    st.markdown("---")

st.subheader("🔑 High-Entropy Key Generator")
if st.button("Generate Enterprise Key"):
    chars = string.ascii_letters + string.digits + string.punctuation
    secure_key = "".join(random.choice(chars) for _ in range(16))
    st.info(f"Generated Key: `{secure_key}`")
