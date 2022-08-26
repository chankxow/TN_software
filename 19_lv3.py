Username = "admin"
Password = "Ad13n@23t"

User = str(input("Username : "))


if User == Username :
    Pass = str(input("Password : "))
    if Pass == Password :
        print("Welcome,admin")
    else :
        print("Your are not admin")
        
elif User != Username :
    Pass = str(input("Password : "))
    if Pass == Password :
        print("Your are not admin")
    else :
        print("Your are not admin")