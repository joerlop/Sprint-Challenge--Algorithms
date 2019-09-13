def question_a(n):
    a = 0
    count = 0

    while (a < n * n * n):
      a = a + n * n
      count += 1
    
    return count

for i in range(50):
    print(f"i: {i}, count: {question_a(i)}")

print("******************************************")

def question_b(n):
    sum = 0
    count = 0

    for i in range(n):
      j = 1
      count += 1
      while j < n:
        j *= 2
        sum += 1
        count += 1
    
    return count

for i in range(20):
    print(f"i: {i}, count: {question_b(i)}")

print("*****************************************")

counter = 0

def bunnyEars(bunnies):
    global counter

    if bunnies == 0:
        return 0
    
    counter += 1

    return 2 + bunnyEars(bunnies-1)

bunnyEars(4)
print(counter)