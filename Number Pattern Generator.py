def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    nums = []
    for i in range(1, n+1):
        nums.append(str(i))
    return " ".join(nums)


print(number_pattern(5))
print(number_pattern(15))
