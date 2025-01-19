operation = input().upper()

all_value = []

for i in range(12):

    values = [float(input()) for _ in range(12)]
    all_value.append(values)

def above_growing(list_, growing):
    calculation = 0
    for i, numbers in enumerate(list_):
        if i < growing:
            calculation += numbers
        else:
            return calculation
        
def above_decreasing(list_, decreasing):
    calculation = 0
    for i, numbers in enumerate(list_):
        if i < decreasing:
            calculation += numbers
        else:
            return calculation

decreasing = 5
growing = 0
values_select = []
for index_l, numbers in enumerate(all_value):
        if index_l < 6:
            call = above_growing(numbers, growing)
            values_select.append(call)
            growing += 1
        else:
            call = above_decreasing(numbers, decreasing)
            values_select.append(call)
            decreasing -= 1

if operation == 'M':
    complete = sum(values_select) / 30
else:
    complete = sum(values_select)
print(f'{complete:.1f}')