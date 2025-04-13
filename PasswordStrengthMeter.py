# PROJECT 02: PASSWORD STRENGTH METER
# A PASSWORD STRENGTH METER USING PYTHON AND STREAMLIT

import re
import streamlit as st

# page styling
st.set_page_config(page_title="Password Strength Meter By Khazra Ayub 🚀", page_icon="🔑" , layout="centered")

# custom css
st.markdown(
    """
    <style>
        .main{
            text-align: center;
        }
         .stApp{
            background: linear-gradient(135deg,rgb(82, 236, 216),rgb(198, 214, 238));
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
        }
       
        .stButton button{
            width: 50%;
            background-color:rgb(50, 124, 124);
            color: white; 
            font-size: 18px;
        }
        .stButton button:hover{
            background-color:rgb(75, 69, 160);
        }
        .footer{
            text-align: center;
            margin-top: 50px;
            font-size: 18px;
            color: white;
            background:rgb(50, 124, 124);
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 5px 15px rgba(67, 78, 80, 0.96);
        }
        
    </style>
    """,
    unsafe_allow_html=True
)

# page title
st.title("Password Strength Generator🔐")
st.write("Enter your password below to check it's security level 🔍")

# function for checking password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score +=1 
    else:
        feedback.append("❌Password should be atleast **8 characters long**.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score +=1
    else:
        feedback.append("❌Password should include **both upper (A-Z) and lower case(a-z)**.")

    if re.search(r"\d", password):
        score +=1
    else:
        feedback.append("❌Password should be atleast **one (0-9) number**.")
    
    if re.search(r"[!@#$%^&*]", password):
        score +=1
    else:
        feedback.append("❌Password should be atleast **one special character include (!@#$%^&*)**.")
    
    # display password strength
    if score == 4:
        st.success("✅ **Strong Pasword** - Your Password is Secure!.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features")
    else:
        st.error("❌ **Week Password** - Follow the suggestion below to strength it.")
    

    # feedback
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:" , type="password", help="Ensure your password is strong 🔐")

# button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")


st.markdown("<div class = 'footer'>Created By Khazra Ayub 💖</div>" , unsafe_allow_html = True)
        


