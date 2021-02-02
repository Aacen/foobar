def foo(number):
  if number % 5 == 0:
    return True

def bar(number):
  if number % 7 == 0:
    return True
 
def fooBar(number):
  if foo(number) and bar(number):
    return True

for number in range(1,150):
  if fooBar(number):
    print ("foobar "  + str(number))
  elif foo(number):
    print("foo " + str(number))
  elif bar(number):
    print("bar " + str(number))
