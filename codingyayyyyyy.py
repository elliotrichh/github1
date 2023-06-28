def biggestprimenum(temp):
    i = 2
    while i * i <= temp:
        if temp % i:
            i += 1
        else:
            temp //= i
    if temp > 1:
        return temp
    return i

number = 600851475143
largest_factor = biggestprimenum(number)
print("The largest prime factor of", number, "is", largest_factor)
