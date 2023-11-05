def calculate_minutes(number_of_days):
    return number_of_days * 24 * 60


def handle_user_input():
    days_input = input("Enter numbers in days split by comas or enter \"exit\"\n")
    if days_input.strip().lower() == "exit":
        print("You decided to exit")
        return None
    correct_inputs = []
    for value in days_input.split(","):
        days = handle_user_input_item(value.strip())
        if days:
            correct_inputs.append(days)
    return correct_inputs


def handle_user_input_item(value):
    if not value.isdigit():
        print(f"Provided value: \"{value}\" is not a positive number")
        return 0
    return int(value)
