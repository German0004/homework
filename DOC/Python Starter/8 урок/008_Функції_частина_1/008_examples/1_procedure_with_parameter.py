# limit - формальний параметр функції print_numbers
def print_numbers(limit):
    for i in range(limit):
        print(i)


# Тут викликається функція print_numbers, а її формально
# параметр limit замінюється фактичним параметром 10
print_numbers(5)
