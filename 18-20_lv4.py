print("ต้องการเพิ่มข้อมูล \"snake\" ไปที่ท้ายาุดของ list")
x = ["dog","cat","hamter"]
print(x)
x.append(input())
print(x)

print("ต้องการเพิ่มข้อมูล \"ิbird\" ไปยังตำแหน่งที่2")
print
x = ["dog","cat","hamter"]
print(x)
x.insert(1,input())
print(x)

print("ต้องการการลบข้อมูลตัวสุดท้าย")
x = ["dog","cat","hamter"]

x.pop()
print(x)

print("ต้องการการลบข้อมูล\"dog\" ")
x = ["dog","cat","hamter"]
print(x)
x.remove("dog")
print(x)