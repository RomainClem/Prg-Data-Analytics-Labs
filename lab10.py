from random import randrange


def question1(collection):
    return collection if type(collection) == tuple else tuple(collection)         

def question2():
    matrix = []
    for x in range(10):
        column = []
        for x in range(10):
            column.append(randrange(1, 100))
        matrix.append(column)
    print(matrix[7])


if __name__ == '__main__':
    question2()
    