from helper import calculate_minutes, handle_user_input

while True:
    values = handle_user_input()
    if values is None:
        break
    for value in values:
        minutes = calculate_minutes(value)
        print(f"There are {minutes} minutes in {value} hours")
