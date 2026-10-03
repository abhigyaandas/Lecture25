basket1={"Orange","Grape","Apple","Watermelon","Apricot"}
basket2={"Orange","Kiwi","Plums","Plums","Apricot"}
print("Fruits in basket 1: ",basket1)
print("Fruits in basket 2: ",basket2)

basket1.add("Bannana")
basket2.add("Kiwi")
print("Fruits in basket 1 after adding Banannaaa: ",basket1)
print("Fruits in basket 2 afer adding another kiwi: ",basket2)

fruites=basket1 & basket2
print("Fruits in both of the baskets are: ",fruites)

import array as arr
count=arr.array('i',[5,3,4,2])
print("The array of gruites", count)
count.insert(1,5)
count.append(6)
print("New stuff added", count)