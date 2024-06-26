my_dict = {'mash': 100, 'sasha': 500, 'roma': 15000}
print(my_dict)
print(my_dict['sasha'])
print(my_dict.get('serg'))
my_dict.update({'anna': 400, 'olga': 600})
print(my_dict)
print(my_dict.pop('sasha'))
print(my_dict)

my_set = {1, 3, 5, 1, 8, 5, 'string', 'stop', 'string'}
print(my_set)
my_set.update({13, 68, 13, 'full', 'call', 'hill', 'call'})
print(my_set)
print(my_set.discard(1))
print(my_set)