# use https://www.rapidtables.com/convert/number/roman-numerals-converter.html to understand calculations

RD_MAP = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def r2d(roman):
    decimal = 0

    while len(roman) > 0:
        char_0_value = RD_MAP[roman[0]]

        if len(roman) >= 2:
            char_1_value = RD_MAP[roman[1]]

            if char_1_value > char_0_value:
                decimal += char_1_value - char_0_value
                roman = roman[2:]
                continue

        decimal += char_0_value
        roman = roman[1:]

    return decimal
