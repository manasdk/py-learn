import eventlet
import math

def is_prime(num):
    for j in range(2,int(math.sqrt(num)+1)):
        if (num % j) == 0: 
            return False
    return True

def nth_prime(n):
    i = 0
    num = 2
    while i < n:
        if is_prime(num):
            i += 1
            return num
        num += 1
    return -1

def do_work(index):
    while(True):
        print '%d computing prime.' % index 
        nth_prime(10)
        print '%d done computing prime.' % index
        eventlet.sleep(1)

def main():
    thread_count = 10
    pool = eventlet.GreenPool(thread_count)
    for index in range(1,thread_count * 10):
         pool.spawn(do_work, index)
    pool.waitall()
    print 'Done'

if __name__ == '__main__':
    main()

