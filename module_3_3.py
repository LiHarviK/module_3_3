# Распаковка

def print_params(a=1, b='строка', c=True):
    print(a, b, c)
#
print_params()
print_params(a='Привет')
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров

values_list = []
values_dict = {'a':1,
               'b':'строка',
               'c':True
               }
print_params(*values_list, 1, 2, 3)
print_params(**values_dict)

# Распаковка + отдельные параметры

values_list_2 = [5, 'Учеба']
print_params(*values_list_2, 42)