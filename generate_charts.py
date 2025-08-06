import streamlit as st
import re
import datetime
import matplotlib.pyplot as plt
from pathlib import Path

# --- CONFIG ---
MARKDOWN_PATH = "project_tracker.md"
START_DATE = datetime.date(2025, 8, 4)
SPRINT_LENGTH_DAYS = 14

# --- FUNCTIONS ---

def extract_sprint_tasks(markdown_text):
    sprint_sections = re.split(r"(?=## Sprint \d+)", markdown_text)
    sprints = []

    for section in sprint_sections[1:]:
        title_match = re.search(r"Sprint (\d+) – (.*?)\*\((.*?)\)\*", section)
        if not title_match:
            continue

        sprint_num = int(title_match.group(1))
        sprint_name = title_match.group(2).strip()
        date_range = title_match.group(3).strip()

        tasks = re.findall(r"^\s*[-*] \[([ x~])\] (.+)$", section, re.MULTILINE)
        parsed_tasks = []
        for status, task in tasks:
            status = status.strip()
            if status == "x":
                state = "Done"
            elif status == "~":
                state = "In Progress"
            else:
                state = "To Do"
            parsed_tasks.append((task, state))

        sprints.append({
            "number": sprint_num,
            "title": sprint_name,
            "date_range": date_range,
            "tasks": parsed_tasks,
        })

    return sprints

def plot_burndown(sprints):
    total_tasks = sum(len(s["tasks"]) for s in sprints)
    completed = 0
    tasks_remaining = []
    dates = []

    current_date = START_DATE
    for sprint in sprints:
        completed += sum(1 for task in sprint["tasks"] if task[1] == "Done")
        tasks_remaining.append(total_tasks - completed)
        dates.append(current_date.strftime("%b %d"))
        current_date += datetime.timedelta(days=SPRINT_LENGTH_DAYS)

    fig, ax = plt.subplots()
    ax.plot(dates, tasks_remaining, marker='o', linestyle='-')
    ax.set_title("Burndown Chart")
    ax.set_xlabel("Sprint Start Date")
    ax.set_ylabel("Tasks Remaining")
    ax.grid(True)
    st.pyplot(fig)

# --- APP START ---
st.title("📊 ML Project Sprint Tracker")

markdown_text = Path(MARKDOWN_PATH).read_text()
sprints = extract_sprint_tasks(markdown_text)

tab1, tab2 = st.tabs(["🗂 Kanban Board", "📉 Burndown Chart"])

with tab1:
    for sprint in sprints:
        st.subheader(f"Sprint {sprint['number']}: {sprint['title']} ({sprint['date_range']})")
        cols = st.columns(3)
        for col, state in zip(cols, ["To Do", "In Progress", "Done"]):
            with col:
                st.markdown(f"### {state}")
                for task, task_state in sprint["tasks"]:
                    if task_state == state:
                        st.markdown(f"- {task}")

with tab2:
    plot_burndown(sprints)