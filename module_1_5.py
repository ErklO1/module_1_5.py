immutable_var=(1,2,3,'Toy', True)
print(immutable_var)
#immutable_var[3]='book' В кортежах элементы не возможно изменять, потому что они не изменяемые. Они используются в том случае, когда нам особенно важно сохранить данные списка в целостности и порядке.
mutable_list=([1,2,3,'book', True])
print(mutable_list)
mutable_list[3]='car'
print(mutable_list)