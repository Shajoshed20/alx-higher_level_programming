def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    digits = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    roman = 0

    for i in range(len(roman_string)):
        if digits.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                digits[roman_string[i]] < digits[roman_string[i + 1]]):
            roman += digits[roman_string[i]] * -1

        else:
            roman += digits[roman_string[i]]
    return (roman)
