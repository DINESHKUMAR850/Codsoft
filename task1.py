print("I am chat Bot: Welcome Student!!")
print("What can i help you.\n")

while True:
    user = input("You: ")

    if "exam schedule" in user:
        print("I am chat Bot: Exams start from 15th December and ends in 1 Month.Kindly Check notice board.")

    elif "minimum attendance" in user:
        print("I am chat Bot: Minimum attendance required is 75%.")

    elif "library Timing" in user:
        print("I am chat Bot: Library is open from 9 AM to 4 PM.")

    elif "upcoming holiday except sunday" in user:
        print("I am chat Bot: Next holiday is on Monday (Public Holiday).")

    elif "college timing" in user:
        print("I am chat Bot: College working hours are 9 AM to 4 PM.")

    elif "help" in user:
        print("I am chat Bot: you can Ask about exams, library, attendance, or holidays.")

    elif user == "exit":
        print("I am chat Bot: Goodbye! Study well ")
    elif "canteen timing" in user:
        print("I am chat Bot: canteen opens from 8.45 AM to 4.30 PM")    
        break

    else:
        print("I am chat Bot: Sorry, I don’t have information on that.")
