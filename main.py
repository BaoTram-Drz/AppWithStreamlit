import streamlit as st

def show_about():
    st.title("About")
    st.write("This is the about page.")
    st.write("Some text about the application.")

def show_contact():
    st.title("Contact")
    st.write("This is the contact page.")
    st.text_input("Name", key="contact_name", help="Enter your name")
    st.text_input("Email", key="contact_email", help="Enter your email")
    st.text_area("Message", key="contact_message", help="Enter your message")

def show_my_information():
    st.title("My Information")
    st.write("This is the my information page.")
    st.write("Name: John Doe")
    st.write("Age: 30")
    st.write("Email: john.doe@example.com")

def main():
    st.title("Navigation App")

    # Add buttons to navigate to different pages
    selected_page = st.sidebar.radio("Select Page", ["About", "Contact", "My Information"])

    if selected_page == "About":
        show_about()
    elif selected_page == "Contact":
        show_contact()
    elif selected_page == "My Information":
        show_my_information()

if __name__ == "__main__":
    main()
