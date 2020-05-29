def ensayis(num):
    a = list(map(int, str(num)))
    a.sort(reverse=True)
    my_lst_str = ''.join(map(str, a))
    return int(my_lst_str)


num = 123456789

a = ensayis(num)
print(str(a))
