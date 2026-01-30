"""
Day 2: Python Control Flow
Topics: for, while, if/elif/else, match-case, pass
"""
# for loop 
for number in range(-8,-1):
    print(number)
if 10>8:print('if block')
else:print('else block')
# While condition
count=0
while(count<10):
     print(count)
     count+=1
#elif block
if False:
     print("first block")
elif True and False:
     print("second block")
else:
     print("else block")
#match
match(100):
     case 10:
          print("this is 10")
     case 100:
          print("its 100")
     case _:
        print("this is last")
#pass
if True:
     pass
#for loop
word=["cat783","56rat","2dogs"]
for item in word:
     numbers=""
     letters=""
     for char in item:
          if char.isdigit():
               numbers+=char
          else:
               letters+=char

     print(f"{item} length {len(item)} and the numericals are {numbers} & letters are {letters}")

#############Generator expression##########
get_non_digit="".join(dig for dig in "abcd3#$45&67" if not dig.isdigit())
print(get_non_digit)
print("_".join(digit for digit in "asdasd3223234##" if digit.isdigit()))
print("".join(['1','e','3']))

