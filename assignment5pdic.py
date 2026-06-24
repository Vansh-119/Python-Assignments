#1
tuple1=(1,5,2,8,4)
result1=tuple1*3
print(result1)

#2
tuple2=(2,7,1,4,5)
tuple3=(1,6,8,2,4)
result2=tuple1+tuple2+tuple3
print(result2)

#3
element=8
if element in tuple3:
    print("Element found")
else:
    print("Not found")

#4
num=(12,5,18,7,23)
total=0
highest=num[0]
lowest=num[0]

for n in num:
    total += n

    if n>highest:
        highest=n

    if n<lowest:
        lowest=n

print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)

#5
n1 = (3, 14, 7, 22, 9, 41, 18, 5)
result = ()
for i in n1:
    if i > 10:
        result += (i,)
print(result)

#6
s = {"cat", "dog", "bird", "fish"}
count = 0
for item in s:
    count += 1
print("Number of elements:", count)

#7
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result4 = s1 | s2
print(result4)

#8
st1 = {1, 2, 3, 4}
st2 = {3, 4, 5, 6}
common = st1 & st2
print(common)

#9
result5 = st1 ^ st2
print(result5)