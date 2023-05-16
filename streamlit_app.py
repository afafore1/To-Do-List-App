import streamlit as st

def add_task(task, tasks):
    tasks.append(task)

def remove_task(task, tasks):
    tasks.remove(task)

def main():
    st.title("To-Do List")
    tasks = st.session_state.get("tasks", [])

    task = st.text_input("New Task")
    if st.button("Add"):
        add_task(task, tasks)
        st.success("Task added!")

    if tasks:
        st.subheader("Tasks")
        for task in tasks:
            st.write(task)

        remove = st.selectbox("Select a task to remove", tasks)
        if st.button("Remove"):
            remove_task(remove, tasks)
            st.success("Task removed!")
    
    st.session_state["tasks"] = tasks

if __name__ == "__main__":
    main()
