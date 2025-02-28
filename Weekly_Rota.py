import random

managers = [
    'Sarah', 'Dasa', 'Mati', 'James', 'Olivia', 'Ethan', 'Sophia'
]

employees = [
    'Louis', 'Lorna', 'Dan', 'D', 'Emma', 'Noah', 'Ava', 'Liam', 'Mia', 'Benjamin'
]

eshifts = ['Morning', 'Afternoon', 'Evening']
mshift = ['9-5', '5-1']

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

schedule = {}


def week_schedule():
    for day in days_of_the_week:
        daily_schedule = []
        available_employees = employees.copy()  

        for shift in eshifts:
            num_needed = 2 if shift != 'Afternoon' else 3
            if len(available_employees) < num_needed:
                print(f"Warning: Not enough employees for {shift} on {day}. Reassigning some employees.")
                available_employees = employees.copy()  # Reset

            selected_employees = random.sample(available_employees, num_needed)
            for e in selected_employees:
                available_employees.remove(e)

            daily_schedule.append(f"{day}: {', '.join(selected_employees)} > {shift}")

        schedule[day] = daily_schedule
        print(f"Schedule for {day}:\n{daily_schedule}\n")


def manager_shift():
    for day in days_of_the_week:
        manager_schedule = []
        available_managers = managers.copy()
        for shift in mshift:
            if len(available_managers) < 2:
                break

            random.shuffle(available_managers)
            selected_manager = available_managers.pop(1)
            manager_schedule.append(f"{day}: {shift} > {selected_manager}")

        print(f"Schedule for {day}:\n{manager_schedule}\n")


def main():
    manager_shift()
    week_schedule()


main()