from untils.untils import *

if __name__ == '__main__':
    a = ['cherry', 'gateron', 'alpacas']
    g = 5
    c = 7
    d = 7.8
    e = 6.7
    for x in a:
        print(x)
    b = [1, 5, 7, 4, 3, 0, 8]
    for i in range(len(b)):
        print(f'b({i})={b[i]}')
    print(f'Tong hai so nguyen: {add(g,c)}')
    print(f'Tong hai so thuc: {add_float(d,e)}')
    compare_two_number_int(g, c)