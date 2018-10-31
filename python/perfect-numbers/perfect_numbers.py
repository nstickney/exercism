def classify(number):
    if number < 1:
        raise ValueError("Only natural numbers may be classified")

    factors = set()
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)

    aliquot = sum(factors) - number
    if aliquot > number:
        return "abundant"
    elif aliquot < number:
        return "deficient"
    return "perfect"
