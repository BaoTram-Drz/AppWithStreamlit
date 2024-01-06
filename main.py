import streamlit as st

class EnglishLearningApp:
    def __init__(self):
        self.pages = [
            {"title": "Greetings", "content": "Learn common greetings in English."},
            {"title": "Colors", "content": "Study the names of different colors."},
            {"title": "Numbers", "content": "Practice counting in English."},
        ]
        self.current_page_index = 0

    def display_current_page(self):
        page = self.pages[self.current_page_index]
        st.markdown(f"# {page['title']}")
        st.write(page['content'])

def main():
    st.title("English Learning App")
    app = EnglishLearningApp()

    # Hiển thị nội dung của trang hiện tại
    app.display_current_page()

    # Tạo thanh điều hướng để chuyển đến trang trước và trang sau
    col1, col2, col3 = st.beta_columns(3)
    if col2.button("Previous Page") and app.current_page_index > 0:
        app.current_page_index -= 1
    if col2.button("Next Page") and app.current_page_index < len(app.pages) - 1:
        app.current_page_index += 1

    # Hiển thị nội dung của trang được chọn (nếu có sự thay đổi)
    app.display_current_page()

if __name__ == "__main__":
    main()
