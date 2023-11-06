from typing import TypedDict
from datetime import datetime


class GoalDeadline(TypedDict):
    goal: str
    deadline: datetime


def get_user_input() -> None | GoalDeadline:
    user_input = input("Input your goal and deadline split by a colon.\nExample: My goal...:31.2.2025\n")
    if ":" not in user_input:
        print("incorrect format. You didn't provide colon")
        return
    [goal, dead_line_str] = map(str.strip, user_input.split(":"))
    if not len(goal):
        print("Your goal is empty. PLease provide your goal")
        return
    try:
        date = datetime.strptime(dead_line_str, "%d.%m.%Y")
        return {"goal": goal, "deadline": date}
    except ValueError:
        print(f"You provided incorrect date: {dead_line_str}. Please provide a date in a format day.month.full year")
        return


def show_user_goal(goal_deadline: GoalDeadline) -> None:
    difference_days = (goal_deadline["deadline"] - datetime.now()).days
    print(f"Your goal: {goal_deadline["goal"]}.\nYou have {difference_days} days left\n")
