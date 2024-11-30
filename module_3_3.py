def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(44, 444, False)
print_params(23, 'Hello', 'True')
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [18, True, 'Jeka']
values_dict = {
    "a": 10,
    "b": "Hello",
    "c": False
}
def print_params(a=1, b="T", c=True):
    print(f"a = {a}, b = {b}, c = {c}")
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [12, True]
print_params(*values_list_2, 42)
