integers = []

odd_ints = []

alternating = []

indexes = []

index_add = []

index_sub = []

sequence = [1]

x = 1

for i in range(48):
    integers.append(i+1)

for element in integers:
    odd_ints.append(element*2 + 1)

for i in range(48):
    alternating.append(integers.pop(0))
    alternating.append(odd_ints.pop(0))

for element in alternating:
    indexes.append(x)
    x += element

indexes_copy = indexes

for i in range(12):
    index_add.append(indexes_copy.pop(0))
    index_add.append(indexes_copy.pop(0))
    index_sub.append(indexes_copy.pop(0))
    index_sub.append(indexes_copy.pop(0))

def compute_next(index_add, index_sub, sequence):
    next_item = 0
    for element in index_add:
        if len(sequence) >= element:
            next_item += sequence[-element]
    
    for element in index_sub:
        if len(sequence) >= element:
            next_item -= sequence[-element]
    return next_item

for i in range(700):
    next_item = compute_next(index_add, index_sub, sequence)
    sequence.append(next_item)

print(sequence[665])
print(sequence[666])
print(sequence[667])