book_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def zada4a(book_list):
    return list(zip(list(map(lambda y: y[0], book_list)), (list(map(lambda x: x[2] * (x[3] + 10) if x[2] * x[3] < 100 else x[2] * x[3], book_list)))))


zada4a(book_list)
