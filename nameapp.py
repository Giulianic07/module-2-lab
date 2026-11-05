last_Name = input("what is your last name ( type ZZZ if you want to quit): ")

while last_Name != "ZZZ":
    
    first_Name = input("Enter first name: ")
    
    gpa = float(input("Enter GPA: "))
    
    if gpa >=3.5:
        print(f"{first_Name} {last_Name} has made the Dean's List.")
    
    else:
        if gpa >= 3.25:
            print(f"{first_Name} {last_Name} has made the Honor Roll.")
    


