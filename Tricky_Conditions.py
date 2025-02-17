def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tricky_conditions(a, b, c):
    if a == b == c:
        return "All Equal"
    elif a < b < c:
        return "Increasing Order"
    elif a > b > c:
        return "Decreasing Order"
    elif a == b or b == c or a == c:
        return "Any Two Equal"
    elif any(is_prime(n) for n in (a, b, c)):
        return "Prime Dominance"
    else:
        return "Random Pattern"

a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
print("Category:", tricky_conditions(a,b,c))
