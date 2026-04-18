#List is a collection which is ordered and changeable. Allows duplicate members.
Courses=['History', 'Math', 'Physics', 'CompSci']
print(Courses)
print(len(Courses))
print(Courses[0])
print(Courses[3])

#Mutable 
list1=['History', 'Math', 'Physics', 'CompSci']
list2=list1
print(list1)
print(list2)

list1[0]='Art'
print(list1)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] 
          for i in range(x + 1) 
          for j in range(y + 1) 
          for k in range(z + 1) 
          if (i + j + k) != n]

print(result)