# N**2
'''
def counter(s):
    for sym in s:
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count += 1
        print(sym, count)

counter('abcdaa')
'''
# M*N M - уникальные элем, N - все элементы
'''
def counter(s):
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count += 1
        print(sym, count)

counter('abcdaa')
'''
# N
def counter(s):
    symb_count = {}
    for sym in s:
        symb_count[sym] = symb_count.get(sym, 0) + 1

    for sym, count in symb_count.items():
        print(sym, count)

counter('akkldsfsaffbcdaa')

# Fadsad
