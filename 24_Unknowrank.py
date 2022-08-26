Username = str(input(""))

Strcount = len(Username)

i = ["1","2","3","4","5","6","7","8","9","0"]

if Username[0] in i :
    print("ต้องขึ้นต้นด้วยตัวอักษร")
elif Username[-1] == "_" :
    print("Username ต้องไม่ลงท้ายด้วย \"_")
elif Strcount > 25 :
    print("Username ของคุณมากกว่า 25")
elif Strcount < 4 :
    print("Username ของคุณน้อยกว่า 4")
elif 4 <= Strcount <= 25:
    print("คุณมีจำนวนตัวอักษรทั้งหมด ",Strcount," ตัว ")
    print("ชื่อของคุณคือ " , Username)
