import random



my_dict = {}
a = 5
b = 8
for i in range(a,b+1):
    my_dict[i] = 0
    
for i in range(100000):
    rnd = random.randint(a,b)
    my_dict[rnd] += 1
        
for j in range(a,b+1):
    print(f"{j} exists {my_dict[j]} times")

