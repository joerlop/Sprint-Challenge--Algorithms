#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

It's o(n) because with each additional increase in n, the number of operations increases proportionally to n. This can be clearly seen in helper file code.py, in which the algorithm is tested for different values of n. With each 1 increase in the value of n, the algorithm performs 1 additional operation.

b)

It certainly looks like an o(n^2) because of the 2 nested loops. However, it isn't because in the while loop the j doesn't increment by 1 but rather it gets multiplied by 2. This makes the second loop perform less operations than if j increased by 1 each iteration.

So, we know it's less than o(n^2).

We also know it's higher than o(n) because it has 2 loops. The first one increases proportionally with n. The second one also increases with n, although not proportionally.

By running the algorithm in code.py it can be seen that it's also higher than o(n * log n) for many values of n. 

Given this, this algorithm has a performance between o(n^2) and o (n log n).

c)

It's going to be o(n). With each increase in n, the number of operations performed increases proportionally. Each time n increases by 1, the number of operations increases by 1 until bunnies == 0, when the algorithm returns.

## Exercise II


