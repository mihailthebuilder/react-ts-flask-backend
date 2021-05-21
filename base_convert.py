# great base converter: https://www.dcode.fr/base-n-convert


def bc(base, num):
    upper_bound = 1
    upper_power = 0
    num_decreasing = num
    rebased_num = ""

    # find the highest power for the base that's smaller than the number
    while upper_bound * base < num:
        upper_bound *= base
        upper_power += 1

    # for each base power that's <= highest power...
    while upper_power >= 0:
        # divmod gets the quotient (digit) and remainder (num_decreasing)
        # num_decreasing is reassigned the remainder
        (digit, num_decreasing) = divmod(num_decreasing, upper_bound)

        # quotient becomes the next digit in the rebased number
        rebased_num += str(digit)

        # go one power lower
        upper_bound = upper_bound // base
        upper_power -= 1

    return rebased_num
