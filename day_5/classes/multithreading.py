# Multithreading

# A thread is the smallest unit of execution with independent set of instructions
# The ability of a process to execute multiple threads parallely is called Multithreading



#     # without threading
# import time
# def calc_squares(numbers):
#     print("squares")
#     for n in numbers:
#         #time.sleep(0.2)
#         print("Square of ", n, "is:", n*n)
# def calc_cubes(numbers):
#     print("cubes")
#     for n in numbers:
#         #time.sleep(0.2)
#         print("Cube of", n, "is: ", n*n*n)

# list1 = [2,3,8,9]
# s = time.time()
# calc_squares(list1)
# calc_cubes(list1)
# e = time.time()

# print((e-s)*1000, "ms")

    #with threading
import time
import threading
def calc_squares(numbers):
    print("squares")
    for n in numbers:
        #time.sleep(0.2)
        print("Square of ", n, "is:", n*n)
def calc_cubes(numbers):
    print("cubes")
    for n in numbers:
        #time.sleep(0.3)
        print("Cube of", n, "is: ", n*n*n)
list1 = [2,3,8,9]

tic = time.time()
# create threads 
t1 = threading.Thread(target=calc_squares, args=(list1,))
t2 = threading.Thread(target=calc_cubes, args=(list1,))

# use start() function -> both functions will run parallely
t1.start()
t2.start()

# join() -> wait here until its done
t1.join()
t2.join()

toc = time.time()

print((toc-tic)*1000, "ms")