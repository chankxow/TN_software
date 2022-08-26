weight = float(input("weight (kg) : "))
height = float(input("height (m) :  "))



bmi = (weight)/(height*height)

print(f"height is  {height} m. and weight is  {weight} kg.")
print(f" BMI is {bmi:.1f} ")

if bmi < 18.5 :
    print("Underweight")
elif 18.5 <= bmi < 25 :
    print("Normal weight")
elif 25 <= bmi < 30  :
    print("Overweight")
elif bmi > 30  :
    print("Obesity")
    
