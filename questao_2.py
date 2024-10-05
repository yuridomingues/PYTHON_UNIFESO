# Dictionary of Roman numeral values
ROMAN_NUMERALS = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

# List of Roman numeral values and symbols
ROMAN_NUMERAL_VALUES = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

# Function to validate a Roman numeral
def validate_roman(roman: str) -> bool:
    valid_chars = set(ROMAN_NUMERALS.keys())
    # Check if all characters are valid
    for char in roman:
        if char not in valid_chars:
            return False

    # Count sequences and repetition rules
    count = 1
    prev_char = ''

    for i in range(len(roman)):
        char = roman[i]

        # Check consecutive character count
        if i > 0 and char == roman[i - 1]:
            count += 1
        else:
            count = 1
        
        # Validate repetition rules
        if (char in 'IXCM' and count > 3) or (char in 'VLD' and count > 1):
            return False

        # Check invalid combinations
        if prev_char and ROMAN_NUMERALS[prev_char] < ROMAN_NUMERALS[char]:
            if (prev_char == 'I' and char not in 'VX') or \
               (prev_char == 'X' and char not in 'LC') or \
               (prev_char == 'C' and char not in 'DM'):
                return False
        
        prev_char = char

    return True

# Function to convert a Roman numeral to decimal
def roman_to_decimal(roman: str) -> int:
    """Convert a Roman numeral to decimal."""
    if not validate_roman(roman):
        raise ValueError(f"Invalid Roman numeral: {roman}")

    decimal = 0
    prev_value = 0
    for char in reversed(roman):
        value = ROMAN_NUMERALS[char]
        decimal += value if value >= prev_value else -value
        prev_value = value

    return decimal

# Function to convert a decimal number to Roman numeral
def decimal_to_roman(decimal: int) -> str:
    """Convert a decimal number to Roman numeral."""
    if not (1 <= decimal <= 3999):
        raise ValueError("Decimal number out of range (1-3999)")

    roman = ''
    for value, numeral in ROMAN_NUMERAL_VALUES:
        while decimal >= value:
            roman += numeral
            decimal -= value
    return roman

# Main function
def main() -> None:
    try:
        roman_input = input('Enter a valid Roman numeral: ').upper()
        decimal_input = int(input('Enter a decimal number: '))

        if validate_roman(roman_input):
            print(f'{roman_input} in decimal is {roman_to_decimal(roman_input)}')
        else:
            print("Invalid Roman numeral.")

        print(f'{decimal_input} in Roman numeral is {decimal_to_roman(decimal_input)}')
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()