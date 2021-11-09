def sum_numbers(*args, **kwargs):
    sum = 0
    for x in args:
        if type(x) == int or type(x) == float:
            sum += x
    return sum


def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)


def suma_pare(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + suma_pare(n - 2)
    return suma_pare(n - 1)


def suma_impare(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return n + suma_impare(n - 2)
    return suma_impare(n - 1)


def main():
    print(sum_numbers(1, 2, 3, -0.4, "abc", [1, 2, 3, 4]))
    print(f'Suma [0, 5]: {suma(5)}')
    print(f'Suma pare [0,6]: {suma_pare(6)}')
    print(f'Suma pare [0,5]: {suma_pare(5)}')
    print(f'Suma impare [0,6]: {suma_impare(6)}')
    print(f'Suma impare [0,5]: {suma_impare(5)}')

    numar = input("Introdu in numar intreg: ")
    try:
        intreg = int(numar)
    except ValueError:
        print(0)
    else:
        print(intreg)


if __name__ == "__main__":
    main()
