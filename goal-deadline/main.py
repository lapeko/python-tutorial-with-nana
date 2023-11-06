from helper import get_user_input, show_user_goal

while True:
    goal_deadline = get_user_input()
    if goal_deadline is None:
        break
    show_user_goal(goal_deadline)