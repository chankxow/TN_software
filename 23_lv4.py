sentence = str(input(""))

sentence = sentence.lower()

print(sentence)

Ac = sentence.count("a")
Ec = sentence.count("e")
Ic = sentence.count("i")
Oc = sentence.count("o")
Uc = sentence.count("u")

print("a = " ,Ac)
print("e = ",Ec)
print("i = ",Ic)
print("o = ",Oc)
print("u = ",Uc)

print("total = ", Ac+Ec+Ic+Oc+Uc)


