userName = input("Enter your name: ")
daysRemaining = input("Days remaining for your birthday: ")
dayToWeekConvert = round(int(daysRemaining)/7, 2)
print(f"Username is {userName} and weeks left for user's birthday are {dayToWeekConvert}")