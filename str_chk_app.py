import streamlit as st
from strength_check import check_password_strength

def main():
    st.set_page_config(page_title = "Password Strength Checker")
    st.title("Password Strength Checker")
    st.write("Enter your password to check its strength.")

    password = st.text_input("Password", type="password")
    if st.button("Check Strength"):
        if password:
            strength = check_password_strength(password)
            if strength == "Weak":
                color = "red"
            elif strength == "Medium" : 
                color = "orange"
            else: 
                color = "green"
            
            st.markdown(f"<h2 style = 'text-align': center; color: {color};'> Password Strength: {strength}</h2>",unsafe_allow_html=True)

            st.subheader("Password Criteria: ")
            if (strength == "Weak" or strength == "Medium"):
                st.write("Have atleast 8 characters with 1 uppercase and 1 special character")
            else:
                st.write("Password is strong!")




if __name__ == "__main__":
    main()