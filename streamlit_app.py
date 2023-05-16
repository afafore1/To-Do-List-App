import streamlit as st

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def remove_task(task):
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
    
    with open("tasks.txt", "w") as file:
        for line in lines:
            if line.strip() != task:
                file.write(line)

def main():
    st.title("To-Do List")
    task = st.text_input("New Task")
    if st.button("Add"):
        add_task(task)
        st.success("Task added!")

    tasks = []
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if tasks:
        st.subheader("Tasks")
        for task in tasks:
            st.write(task)

        remove = st.selectbox("Select a task to remove", tasks)
        if st.button("Remove"):
            remove_task(remove)
            st.success("Task removed!")
    
if __name__ == "__main__":
    main()
