import streamlit as st

def custom_title(text, font="Autour One", size=36, color="blue", background_color="lightgrey", padding="10px", margin="10px"):
    style = f"font-family:{font}; font-size:{size}px; color:{color}; background-color:{background_color}; padding:{padding}; margin:{margin};"
    st.markdown(f"<p style='{style}'><b>{text}</b></p>", unsafe_allow_html=True)

def show_about():
    custom_title("About", color="green", background_color="lightyellow", padding="20px", margin="20px")
    st.write("This is the about page.")
    st.write("Some text about the application.")

def show_contact():
    custom_title("Contact", color="orange", background_color="lightblue", padding="20px", margin="20px")
    st.write("This is the contact page.")
    st.text_input("Name", key="contact_name", help="Enter your name")
    st.text_input("Email", key="contact_email", help="Enter your email")
    st.text_area("Message", key="contact_message", help="Enter your message")

def show_my_information():
    custom_title("My Information", color="purple", background_color="lightgreen", padding="20px", margin="20px")
    st.write("This is the my information page.")
    st.write("Name: John Doe")
    st.write("Age: 30")
    st.write("Email: john.doe@example.com")

def main():
    custom_title("Navigation App", color="red", background_color="lightgrey", padding="20px", margin="20px")
    
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
