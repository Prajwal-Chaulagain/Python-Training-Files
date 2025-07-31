import streamlit as st
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from a JSON file."""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            return tasks if isinstance(tasks, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Saves tasks to a JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def main():
    st.title("✅ To-Do List App")
    st.write("Manage your tasks efficiently!")
    
    if "tasks" not in st.session_state:
        st.session_state.tasks = load_tasks()
    
    # Display tasks
    st.subheader("Tasks")
    if not st.session_state.tasks:
        st.write("No tasks available.")
    else:
        for index, task in enumerate(st.session_state.tasks):
            col1, col2, col3 = st.columns([5, 1, 1])
            col1.write(f"{index + 1}. {task['name']}")
            col2.write("✅" if task["done"] else "❌")
            if col3.button("Remove", key=index):
                st.session_state.tasks.pop(index)
                save_tasks(st.session_state.tasks)
                st.rerun()
    
    # Add task
    st.subheader("Add a New Task")
    new_task = st.text_input("Task Name")
    if st.button("Add Task") and new_task:
        st.session_state.tasks.append({"name": new_task, "done": False})
        save_tasks(st.session_state.tasks)
        st.rerun()
    
    # Mark task as done
    st.subheader("Mark Task as Done")
    task_names = [task["name"] for task in st.session_state.tasks if not task["done"]]
    if task_names:
        task_to_mark = st.selectbox("Select a task", task_names)
        if st.button("Mark as Done"):
            for task in st.session_state.tasks:
                if task["name"] == task_to_mark:
                    task["done"] = True
                    break
            save_tasks(st.session_state.tasks)
            st.rerun()
    else:
        st.write("No pending tasks.")
    
if __name__ == "__main__":
    main()