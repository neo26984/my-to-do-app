import streamlit as st
import f

todos = f.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)


st.title("my todo app.")

for index, todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="", placeholder="add a todo...", on_change=add_todo, key="new_todo")
