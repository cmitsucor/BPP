import pdb
pdb.set_trace()


def mayores(lista):
    max_num = [max(i) for i in lista]
    return max_num


def es_primo(n):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    print(mayores(
        [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]))

    lista = [3, 4, 8, 5, 5, 22, 13]

    print(list(filter(es_primo, lista)))
