import re
import datetime
import matplotlib.pyplot as plt
from pathlib import Path

MARKDOWN_PATH = "project_tracker.md"
OUTPUT_DIR = Path("assets")
OUTPUT_DIR.mkdir(exist_ok=True)
START_DATE = datetime.date(2025, 8, 4)
SPRINT_LENGTH_DAYS = 14


def extract_sprint_tasks(md_text):
    sprint_sections = re.split(r"(?=##\s*(?:[\W_]+\s*)?Sprint \d+)", md_text)
    sprints = []

    for section in sprint_sections[1:]:
        # Updated regex to handle new format: "Sprint X: Title – Description *(dates)*"
        title_match = re.search(r"Sprint (\d+)[:\s]*([^–]*)\s*–\s*(.*?)\s*\*\((.*?)\)\*", section, re.DOTALL)

        if not title_match:
            continue

        sprint_num = int(title_match.group(1))
        sprint_title = title_match.group(2).strip() if title_match.group(2) else ""
        sprint_description = title_match.group(3).strip()
        date_range = title_match.group(4).strip()

        tasks = re.findall(r"[-*] \[([ x~])\] (.+)", section)
        parsed_tasks = []
        for status, desc in tasks:
            status = status.strip()
            if status == "x":
                state = "Done"
            elif status == "~":
                state = "In Progress"
            else:
                state = "To Do"
            parsed_tasks.append((desc.strip(), state))

        sprints.append({
            "number": sprint_num,
            "title": sprint_title,
            "description": sprint_description,
            "date_range": date_range,
            "tasks": parsed_tasks,
        })

    return sprints

def generate_sprint_status_chart(sprints, output_path):
    today = datetime.date.today()

    # Assign actual start and end dates to each sprint based on offsets
    for i, sprint in enumerate(sprints):
        sprint_start = START_DATE + datetime.timedelta(days=i * SPRINT_LENGTH_DAYS)
        sprint_end = sprint_start + datetime.timedelta(days=SPRINT_LENGTH_DAYS - 1)

        sprint["start_date"] = sprint_start
        sprint["end_date"] = sprint_end

    # Prepare data for all sprints
    sprint_names = []
    to_do_counts = []
    in_progress_counts = []
    done_counts = []

    for sprint in sprints:
        sprint_names.append(f"Sprint {sprint['number']}")
        to_do_counts.append(sum(1 for t in sprint["tasks"] if t[1] == "To Do"))
        in_progress_counts.append(sum(1 for t in sprint["tasks"] if t[1] == "In Progress"))
        done_counts.append(sum(1 for t in sprint["tasks"] if t[1] == "Done"))

    # Create stacked bar chart
    plt.figure(figsize=(12, 8))
    
    # Colors for the three states
    colors = ["#BE5959", "#CCAC39", "#117DA1"]  # To Do, In Progress, Done
    
    # Create the stacked bars
    bar1 = plt.bar(sprint_names, to_do_counts, label='To Do', color=colors[0])
    bar2 = plt.bar(sprint_names, in_progress_counts, bottom=to_do_counts, label='In Progress', color=colors[1])
    
    # Calculate bottom for done tasks
    bottom_done = [to_do + in_progress for to_do, in_progress in zip(to_do_counts, in_progress_counts)]
    bar3 = plt.bar(sprint_names, done_counts, bottom=bottom_done, label='Done', color=colors[2])

    # Add text annotations on each segment
    for i, (sprint_name, to_do, in_progress, done) in enumerate(zip(sprint_names, to_do_counts, in_progress_counts, done_counts)):
        # To Do annotation
        if to_do > 0:
            plt.text(i, to_do/2, str(to_do), ha='center', va='center', 
                    fontweight='bold', color='white' if to_do > 1 else 'black')
        
        # In Progress annotation
        if in_progress > 0:
            plt.text(i, to_do + in_progress/2, str(in_progress), ha='center', va='center', 
                    fontweight='bold', color='white' if in_progress > 1 else 'black')
        
        # Done annotation
        if done > 0:
            plt.text(i, to_do + in_progress + done/2, str(done), ha='center', va='center', 
                    fontweight='bold', color='white' if done > 1 else 'black')

    # Highlight current sprint
    current_sprint_index = None
    for i, sprint in enumerate(sprints):
        if sprint["start_date"] <= today <= sprint["end_date"]:
            current_sprint_index = i
            break

    if current_sprint_index is not None:
        # Add a subtle border around the current sprint
        ax = plt.gca()
        bars = ax.patches
        # Each sprint has 3 stacked segments, so we need to highlight all 3 segments of the current sprint
        num_sprints = len(sprints)
        indices_to_highlight = [
            current_sprint_index,  # To Do bar
            num_sprints + current_sprint_index,  # In Progress bar  
            2 * num_sprints + current_sprint_index  # Done bar
        ]
        
        for bar_index in indices_to_highlight:
            if bar_index < len(bars):
                bars[bar_index].set_edgecolor('black')
                bars[bar_index].set_linewidth(2)

    plt.title("Project Sprint Status Overview", fontsize=14, fontweight='bold', pad=20)
    plt.ylabel("Task Count")
    plt.xlabel("Sprints")
    plt.legend(handles=[bar3, bar2, bar1], loc='upper right')  # Reversed order: Done, In Progress, To Do
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150)
    plt.close()


if __name__ == "__main__":
    markdown = Path(MARKDOWN_PATH).read_text()
    sprints = extract_sprint_tasks(markdown)

    generate_sprint_status_chart(sprints, OUTPUT_DIR / "sprint_status_chart.png")

    print("Chart generated in ./assets/")
