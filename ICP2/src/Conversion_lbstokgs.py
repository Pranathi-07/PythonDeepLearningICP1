lst1 = []
lst2 = []
lst1 = [float(weight) for weight in input("Enter the list items : ").split()]
for weight in lst1 :
    kgs = weight * 0.453592
    lst2.append(kgs)
print(lst2)