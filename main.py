#1
name = input()

if len(name) <= 2:
    print(name)
else:
    masked = name[0] + "X" * (len(name) - 2) + name[-1]
    print(masked)
  
#2
my_tuple = ("a", "b", "c", "d")

result = tuple((i, my_tuple[i]) for i in range(len(my_tuple)))
print(result)

#3
my_tuple = ("apple", "banana", "rubob")

result = tuple(s[::-1] for s in my_tuple)
print(result)
