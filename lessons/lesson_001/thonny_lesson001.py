total_bill_str = '124.54'
num_of_people_str = '5'
percentage_str = '12'

print('Welcome to the tip calculator.')
print('What was the total bill? ')
total_bill = float(total_bill_str)
print('How many people to split the bill? ')
num_of_people = int(num_of_people_str)
print("what percentage? ")
percentage = float(percentage_str)
price = (total_bill * (1+percentage/100)) / num_of_people
float_str = "{:.4f}".format(price)
full_str = "each person should pay " + float_str
print(full_str)
print("hello"[2])

a = 5
b = 2
c = 7
mystr = f"{a} + {b} = {c}"
print(mystr)





