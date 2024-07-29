def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [1, 'coco', False]
values_dict = {'a': 1, 'b': True, 'c': 'Hello world ;)'}
values_list_2 = [22, '"python"']

print_params(b=25)
print_params(b=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)


