def sum_of_multiples(limit, multiples):
    return sum(set(i for m in multiples for i in range(m, limit, m)))
