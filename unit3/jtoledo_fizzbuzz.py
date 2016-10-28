num = input("Enter a number to start with: ")
end = input("Enter a number to end with: ")
end = int(end)
nam = int(num)

for x in range(nam -1, end):
    x = x + 1
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 5 == 0: 
        print("buzz")
    elif x % 3 == 0:
        print("fizz")
    else:
            print(x)
        
        
        
            