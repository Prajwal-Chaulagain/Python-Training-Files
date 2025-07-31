import streamlit as st
import json
import os
import base64
import random
import string
from cryptography.fernet import Fernet

# Function to generate encryption key
def generate_key():
    return Fernet.generate_key()

# Load encryption key
def load_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as key_file:
            return key_file.read()
    else:
        key = generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key

key = load_key()
fernet = Fernet(key)

# Encrypt password
def encrypt_password(password):
    return base64.b64encode(fernet.encrypt(password.encode())).decode()

# Decrypt password
def decrypt_password(encrypted_password):
    return fernet.decrypt(base64.b64decode(encrypted_password)).decode()

# Load saved passwords
def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            return json.load(file)
    return {}

# Save passwords
def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

passwords = load_passwords()

# Streamlit UI
st.title("🔐 Password Manager")

menu = st.sidebar.selectbox("Select an Option", ["List Services","Add Password", "Retrieve Password", "Update Password", "Delete Password", "Generate Strong Password"])

if menu == "Add Password":
    service = st.text_input("Service Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Save Password"):
        if service and username and password:
            passwords[service] = {"username": username, "password": encrypt_password(password)}
            save_passwords(passwords)
            st.success(f"Password for {service} saved successfully!")
        else:
            st.error("Please fill in all fields.")

elif menu == "Retrieve Password":
    service = st.text_input("Enter Service Name")
    if st.button("Retrieve"):
        if service in passwords:
            st.success(f"Password: {decrypt_password(passwords[service]['password'])}")
        else:
            st.error("No password found for this service.")

elif menu == "Update Password":
    service = st.text_input("Enter Service Name")
    new_password = st.text_input("New Password", type="password")
    if st.button("Update"):
        if service in passwords:
            passwords[service]["password"] = encrypt_password(new_password)
            save_passwords(passwords)
            st.success("Password updated successfully!")
        else:
            st.error("Service not found.")

elif menu == "Delete Password":
    service = st.text_input("Enter Service Name")
    if st.button("Delete"):
        if service in passwords:
            del passwords[service]
            save_passwords(passwords)
            st.success("Password deleted successfully!")
        else:
            st.error("Service not found.")

elif menu == "List Services":
    st.write("### Stored Services")
    if passwords:
        for service in passwords.keys():
            st.write(f"- {service}")
    else:
        st.write("No services stored yet.")

elif menu == "Generate Strong Password":
    length = st.slider("Password Length", 8, 32, 16)
    if st.button("Generate"):
        strong_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        st.code(strong_password, language="plaintext")