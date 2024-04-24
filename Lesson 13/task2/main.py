from modules.str_module import print_many_str, get_char, get_invert_str
from modules.list_module import sum_two_lists, get_invert_list, get_list_element
from modules.num_module import (get_prime_numbers,
                                get_fibonacci_numbers,
                                get_sum_of_digits)

print(get_prime_numbers(50))
print(get_fibonacci_numbers(50))
print(get_sum_of_digits(50454545))

list1 = [5, 3, 4, 5]
list2 = [6, 6, 4, 2]

print(sum_two_lists(list1, list2))
print(get_invert_list(list2))
print(get_list_element(list1, 2))

print_many_str("Hello", 5)
print(get_char("Hello", 2))
print(get_invert_str("Hello"))
