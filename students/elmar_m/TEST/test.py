

def countdown(n):
    if n == 0:
        print('bumm!')
    else:
        print(n)
        countdown(n-1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print('please import me...')
