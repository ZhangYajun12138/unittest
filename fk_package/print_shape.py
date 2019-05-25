def print_blank_triangle(n):
    if n <= 0:
        raise ValueError('n 必须大于零')
    for i in range(n):
        print(' '*(n-1-i),end='')
        print('*',end='')
        if i != n-1:
            print(' '*(2*i-1),end='')
        else:
            print('*' * (2 * i - 1), end='')
        if i != 0:
            print('*')
        else:
            print('')

if __name__ == '__main__':
    print_blank_triangle(5)