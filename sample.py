def f(x):
    return x / 2

def h(y):
    return y * 4

number = f(5)
print(number)

print(h(number))

def word(word):
    try:
        return float(word)
    except ValueError:
        return 'error'

print(word(3))
