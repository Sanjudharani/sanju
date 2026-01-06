def wrapper(f):
    def fun(l):
        formatted_numbers = []
        for number in l:
            number = number[-10:]
            formatted_numbers.append("+91 " + number[:5] + " " + number[5:])
        f(formatted_numbers)
    return fun

