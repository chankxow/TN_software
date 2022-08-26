main = int(input("lease type 1 to show menu : "))

menu = ["Espresso","Cappucino","latte"]
type_coffee = ["hot", "cold"]
price = ["55","60"]
#หากเลือก 1

if main == 1 :
    print("--- Choose the menu ---")
    print("1 : Espresso ")
    print("2 : Cappucino ")
    print("3 : latte")
    
    select = int(input("select coffee: "))
    if select == 1 or 2  :
        print("---choose the type of the coffee---")
        print(f"1 : {type_coffee[0]} {price[0]} bath")
        print(f"2 : {type_coffee[1]} {price[1]} bath")
        
        type = int(input("select type: "))
        if type == 1 or 2 :
            print(f"you chose {type_coffee[type-1]} {menu[select-1]} {price[type-1]} bath")       
            money = int(input("input your money : "))

            recieved_money = money - int(price[type-1])

            if recieved_money < 0 :
                print("ยอดเงินไม่เพียงพอ")
            elif recieved_money <= 0:
                print(f"recieved a change of {recieved_money} bath" )
                print("---thank you ---")
else :
    print("plz type 12")
