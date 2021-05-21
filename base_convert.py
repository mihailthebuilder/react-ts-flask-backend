# great base converter: https://www.dcode.fr/base-n-convert


def bc(base, num):
    upper_bound = 1
    upper_power = 0
    num_decreasing = num
    rebased_num = ""

    while upper_bound * base < num:
        upper_bound *= base
        upper_power += 1

    while upper_power >= 0:
        (digit, num_decreasing) = divmod(num_decreasing, upper_bound)
        rebased_num += str(digit)
        upper_bound = upper_bound // base
        upper_power -= 1

    return rebased_num
