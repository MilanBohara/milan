user = input("Enter username : ")


if user == "Admin":
    print("You are successfully login in admin dasboard")
    attendence = input("Enter attendence : ")
    if attendence == "Full":
        print("staff attendence is full")
    elif attendence == "Half":
        print("Staff attendence is Half")
    elif attendence == "morning ":
        print("staff attendence is morning")
    else:
        print("Staff is absent")
else:
    print("You are admin")
