import requests
import streamlit as st

st.snow()
todos_item_list = requests.get("http://localhost:8000/todos")
todos = todos_item_list.json()
st.subheader("Current Todos")
for todo in todos:
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        st.write(f"📝 {todo['title']} - {'✅ Done' if todo['done'] else '❌ Not yet'}")
    with col2:
        if st.button("🗑 削除", key=todo["id"]):
            # 3. DELETEリクエスト送信
            del_res = requests.delete(f"http://localhost:8000/todos/{todo['id']}")
            if del_res.status_code == 200:
                st.success("削除しました")
                st.rerun()
            else:
                st.error("削除に失敗しました")
st.title("todo app")

item_input = st.text_input("Todo Title", "Input todo title here.")
if st.checkbox("Task is finished"):
    flag = True
else:
    flag = False

if st.button("submit"):
    new_todo = {"title": item_input, "done": flag}
    res = requests.post("http://localhost:8000/todos/", json=new_todo)
    if res.status_code == 200:
        st.success("Todo added successfully!")
        st.rerun()
    else:
        st.error("Failed to add Todo")

if st.button("save"):
    res = requests.post("http://localhost:8000/todos/save")
    if res.status_code == 200:
        st.success("Todo saved successfully!")
        st.rerun()
    else:
        st.error("Failed to save Todo")

if st.button("load"):
    res = requests.post("http://localhost:8000/todos/load")
    if res.status_code == 200:
        st.success("Todo loaded successfully!")
        st.rerun()
    else:
        st.error("Failed to load Todo")
