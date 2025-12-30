
from threading import Thread
import time, math

def square(n):
    print("Square:", n*n)

def factorial(n):
    print("Factorial:", math.factorial(n))

start = time.time()

t1 = Thread(target=square, args=(5,))
t2 = Thread(target=factorial, args=(5,))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print("Time taken:", end-start)
