# 1 Basic: print 0 through 150
for i in range(151):
    print(i)

# # 2 Multples of 5: 5 through 1000
num5 = 5
for n in range(1000):
    print(num5)
    num5 += 5
    if(num5 > 1000):
        break

# 3 Counting, the Dojo Way: print 1-100, div/5: Coding. div/10 Coding Dojo
for m in range(101):
    if(m % 10 == 0):
        print('Coding Dojo')
    elif(m % 5 == 0):
        print('Coding')
    else:
        print(m)
    m = m + 1

# 4 The Sucker's Huge. add odd ints 0 through 500,000, print the final sum
sum = 1
for odd in range(500000):
    sum += 2
print(sum)

# 5 Countdown by Fours: count down by four form 2018
num2018 = 2018
while num2018 > 0:
    print(num2018)
    num2018 = num2018 - 4

# 6 Flexible Counter
lowNum = 3
highNum = 20
mult = 4
while(mult < highNum):
    print(mult)
    mult += mult