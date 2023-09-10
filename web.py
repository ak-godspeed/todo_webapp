from function import get_todos, write_todos
import streamlit as st

todos = get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    if len(new_todo) > 0:
        todos.append(new_todo)
        write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("<h5>This app is used to increase the productivity.</h5>", unsafe_allow_html=True)

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()
st.text_input(label=":heavy_plus_sign:", placeholder="Enter new todo....", key="new_todo", on_change=add_todo)

