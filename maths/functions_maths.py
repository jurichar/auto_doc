def sum(a, b):
    """
    Calcule la somme de deux nombres.

    Args:
        a (int): Le premier nombre à additionner.
        b (int): Le deuxième nombre à additionner.

    Returns:
        int: La somme des deux nombres.
    """
    return a + b


def multiplication(a, b):
    """
    Calcule le produit de deux nombres.

    Args:
        a (int): Le premier nombre à multiplier.
        b (int): Le deuxième nombre à multiplier.

    Returns:
        int: Le produit des deux nombres.
    """
    return a * b


def factorial(n):
    """
    Calcule la factorielle d'un nombre.

    Args:
        n (int): Le nombre dont on veut calculer la factorielle.

    Returns:
        int: La factorielle du nombre.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    """
    Calcule le n-ième nombre de la suite de Fibonacci.

    Args:
        n (int): Le rang du nombre à calculer.

    Returns:
        int: Le n-ième nombre de la suite de Fibonacci.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)