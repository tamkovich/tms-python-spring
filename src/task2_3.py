list_with_two_elements = ['киса','котя']
tuple_with_two_elements = ('котик', 'кот')
print(list_with_two_elements,tuple_with_two_elements)
dict_with_tuple_in_key_and_list_in_value = {
    tuple_with_two_elements : list_with_two_elements
}
print(dict_with_tuple_in_key_and_list_in_value)
dict_with_list_in_key_and_tuple_in_value = {
    list_with_two_elements : tuple_with_two_elements
}
print(dict_with_list_in_key_and_tuple_in_value)