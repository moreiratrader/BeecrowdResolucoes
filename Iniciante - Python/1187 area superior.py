

operation = input().upper()

all_value = [[8.5, 2.5, 8.1, 3.3, 7.0, 7.4, 8.9, 1.8, 6.5, 6.3, 6.0, 0.3],
             [4.1, 1.2, 4.4, 2.9, 1.5, 5.2, 8.4, 6.5, 7.1, 5.3, 2.5, 2.0],
             [0.6, 3.5, 0.7, 6.3, 0.6, 1.6, 0.5, 0.1, 5.5, 2.2, 4.0, 0.1],
             [1.3, 5.4, 2.5, 0.4, 4.8, 7.2, 5.1, 6.7, 2.1, 4.0, 9.0, 4.7],
             [2.9, 4.2, 6.7, 6.2, 7.7, 6.4, 5.1, 7.4, 0.4, 3.2, 6.8, 5.3],
             [2.7, 0.4, 5.5, 5.2, 0.8, 4.5, 2.8, 3.8, 5.7, 8.3, 0.2, 6.4],
             [8.6, 8.7, 1.7, 2.9, 0.4, 7.9, 7.0, 6.1, 2.0, 8.5, 3.8, 5.2],
             [2.2, 0.1, 4.3, 8.4, 3.7, 6.5, 2.8, 8.0, 1.0, 3.7, 8.1, 2.5],
             [5.9, 8.3, 4.0, 1.3, 3.4, 5.4, 0.4, 8.6, 5.8, 4.1, 1.8, 5.9],
             [2.8, 3.5, 1.5, 1.0, 1.1, 2.2, 0.1, 1.3, 8.7, 7.6, 0.4, 3.5],
             [4.5, 1.1, 6.2, 8.4, 6.1, 3.2, 3.8, 3.2, 2.3, 6.6, 1.8, 6.1],
             [8.4, 3.4, 7.1, 6.7, 1.3, 4.2, 5.3, 6.7, 5.7, 5.3, 4.8, 0.4]]

# for i in range(12):

#     values = [float(input()) for _ in range(12)]
#     all_value.append(values)

def above(list_,i_start, i_stop):
    calculation = 0
    for i, numbers in enumerate(list_):
        if i > i_start and i < i_stop:
            calculation += numbers
    return calculation

i_start = 0
i_stop = 11
values_select = []
for index_l, numbers in enumerate(all_value):
    if index_l <= 4:
        call = above(numbers,i_start, i_stop)
        values_select.append(call)
    elif index_l == 5:
        break
    i_start += 1
    i_stop -= 1

if operation == 'M':
    complete = sum(values_select) / 30
else:
    complete = sum(values_select)
print(f'{complete:.1f}')