def question_a(n):
    a = 0
    count = 0

    while (a < n * n * n):
      a = a + n * n
      count += 1
    
    return count

for i in range(50):
    print(f"i: {i}, count: {question_a(i)}")