def check_goal(steps, goal):
    """Проверяет сделана ли цель"""
    if steps >= goal:
        return True
    else:
        return False
"""Запрашиваем у пользователя цель"""
input_user_goal = int(input("What is yor daily goal?"))

"""Проверяем на наличие отрицательного числа или нуля"""
if input_user_goal <= 0:
    print("You enterd a negative or zero character, try again.")
else:
    total_steps = 0
    goal_ok = 0
    for day in range(1, 8):
        """Спрашиваем про ежедневные достижения и общее число шагов"""
        daily_steps = int(input(f"Enter steps for Day {day}:  "))
        total_steps = total_steps + daily_steps

        if check_goal(daily_steps, input_user_goal) == True:
            goal_ok+=1

    print("\n--- WEEKLY REPORT ---")
    print(f"Total steps per day: {total_steps:,}")

    average = round(total_steps / 7)
    print(f"Average steps per day: {average:,}")

    print(f"Days goal met: {goal_ok}/7")

    if goal_ok >= 4:
        print("Verdict: Great job! The week has wrapped up successfully!")
    else:
        print("Verdict: We need to push harder next week!")
