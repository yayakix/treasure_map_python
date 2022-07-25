
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

array = []
for x in position:
  array.append(x)
  
print(array)
# position 1 is the row
rowpos = 0
columnpos = 0

# check column

if array[0] == '1':
  columnpos = 1
elif array[0] == '2':
  columnpos = 2
  
elif array[0] == '3':
  columnpos = 3

  
# check row
if array[1] == '1':
  row1[columnpos - 1] = "x"
elif array[1] == '2':
  row2[columnpos - 1] = "x"
  
elif array[1] == '3':
  row3[columnpos - 1] = "x"


# position 0 is the column




print(f"{row1}\n{row2}\n{row3}")