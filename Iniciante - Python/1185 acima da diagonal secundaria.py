operation = input(). upper()

all_value = []
line_final =[]

for _ in range(12):
    generator = [float(input()) for i in range(12)]
    all_value.append(generator)


def num_select(list_, add):
    calculation = 0

    for index, number in enumerate(list_):
        if index <= add:
            calculation += number
        else:
            return calculation

add = 10
for  list in all_value:
        line_final.append(num_select(list, add))
        add -= 1

if operation == 'M':

    complete = sum(line_final) / 66

else:
    complete = sum(line_final)

print(f'{complete:.1f}')
