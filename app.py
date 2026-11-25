import random
import streamlit as st

questions = [
    {"emoji": "🦁👑", "answer": "lion king", "display": "The Lion King", "category": "Movies"},
    {"emoji": "🕷️👨", "answer": "spiderman", "display": "Spider-Man", "category": "Movies"},
    {"emoji": "🍎🥧", "answer": "apple pie", "display": "Apple Pie", "category": "Food"},
    {"emoji": "🐝🍯", "answer": "honey", "display": "Honey", "category": "Food"},
    {"emoji": "🌧️🌈", "answer": "rainbow", "display": "Rainbow", "category": "Nature"},
    {"emoji": "🐈", "answer": "cat", "display": "Cat", "category": "Animals"},
    {"emoji": "🧊🍦", "answer": "ice cream", "display": "Ice Cream", "category": "Food"},
    {"emoji": "🌙⭐", "answer": "night sky", "display": "Night Sky", "category": "Nature"},
]

def start_game():
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)
    st.session_state.questions = shuffled_questions
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.game_over = False

if "questions" not in st.session_state:
    start_game()

st.title("🎭 Guess the Emoji")
st.write("Can you figure out what these emojis mean?")

if not st.session_state.game_over:
    current_question = st.session_state.questions[st.session_state.question_index]
    total_questions = len(st.session_state.questions)

    st.progress((st.session_state.question_index) / total_questions)
    st.caption(f"Question {st.session_state.question_index + 1} of {total_questions}")
    st.caption(f"Category: {current_question['category']}")

    st.markdown(f"<h1 style='text-align:center;font-size:90px'>{current_question['emoji']}</h1>", unsafe_allow_html=True)

    if not st.session_state.answered:
        user_answer = st.text_input("Your guess", key=f"answer_{st.session_state.question_index}")

        if st.button("Submit Answer"):
            if user_answer.strip().lower() == current_question["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = "Correct! 🎉"
            else:
                st.session_state.feedback = f"Not quite! The answer was **{current_question['display']}**."
            st.session_state.answered = True
            st.rerun()
    else:
        st.write(st.session_state.feedback)
        st.write(f"Score: {st.session_state.score}")

        if st.button("Next Question"):
            st.session_state.question_index += 1
            st.session_state.answered = False
            st.session_state.feedback = ""
            if st.session_state.question_index >= len(st.session_state.questions):
                st.session_state.game_over = True
            st.rerun()
else:
    st.success("Game completed!")
    st.header(f"Your final score: {st.session_state.score} / {len(st.session_state.questions)}")
    if st.session_state.score == len(st.session_state.questions):
        st.balloons()
        st.write("Amazing! You got every answer right!")
    elif st.session_state.score >= len(st.session_state.questions) // 2:
        st.write("Great job! You know your emojis!")
    else:
        st.write("Good try! Play again to improve your score.")

    if st.button("Play Again"):
        start_game()
        st.rerun()
