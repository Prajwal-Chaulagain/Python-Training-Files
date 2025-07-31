import streamlit as st
import random

questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is 5 + 7?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the chemical symbol for gold?",
    "What is the largest ocean on Earth?",
    "Who painted the Mona Lisa?",
    "What is the square root of 64?",
    "Which is the longest river in the world?",
    "What is the national animal of China?",
]

choices = [
    ["Paris", "London", "Rome", "Berlin"],
    ["Earth", "Mars", "Jupiter", "Venus"],
    ["10", "11", "12", "13"],
    ["J.K. Rowling", "Harper Lee", "Mark Twain", "Jane Austen"],
    ["Au", "Ag", "Pb", "Fe"],
    ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
    ["6", "7", "8", "9"],
    ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
    ["Tiger", "Panda", "Elephant", "Kangaroo"],
]

answers = [
    "Paris",
    "Mars",
    "12",
    "Harper Lee",
    "Au",
    "Pacific Ocean",
    "Leonardo da Vinci",
    "8",
    "Nile River",
    "Panda",
]


def main():
    st.title("🎯 Quiz Game")
    st.write("Test your knowledge with this fun quiz!")

    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.quiz_started = False

    if not st.session_state.quiz_started:
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.rerun()
    else:
        index = st.session_state.question_index
        if index < len(questions):
            st.subheader(f"Question {index + 1}: {questions[index]}")
            user_choice = st.radio("Choose an answer:", choices[index])
            if st.button("Submit Answer"):
                if user_choice == answers[index]:
                    st.session_state.score += 1
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Wrong! The correct answer was {answers[index]}")
                st.session_state.question_index += 1
                st.rerun()
        else:
            st.subheader("Game Over!")
            st.write(f"Your final score is {st.session_state.score}/{len(questions)}")
            if st.button("Play Again"):
                st.session_state.question_index = 0
                st.session_state.score = 0
                st.session_state.quiz_started = False
                st.rerun()


if __name__ == "__main__":
    main()