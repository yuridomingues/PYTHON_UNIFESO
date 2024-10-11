import re

ROMAN_NUMERALS = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

ROMAN_NUMERAL_VALUES = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

# Regex para verificar números romanos válidos de 1 a 3999
ROMAN_REGEX = re.compile(
    r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
)

def is_valid_roman(roman: str) -> bool:
    return bool(ROMAN_REGEX.match(roman))

def roman_to_decimal(roman: str) -> int:
    if not is_valid_roman(roman):
        raise ValueError(f"Número romano inválido: {roman}")

    decimal = 0
    prev_value = 0
    for char in reversed(roman):
        value = ROMAN_NUMERALS.get(char)
        if value is None:
            raise ValueError(f"Número romano inválido: {char}")
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value

    if not (1 <= decimal <= 3999):
        raise ValueError("Número decimal fora do limite (precisa ser 1-3999)")

    return decimal

def decimal_to_roman(decimal: int) -> str:
    if not (1 <= decimal <= 3999):
        raise ValueError("Número decimal fora do limite (precisa ser 1-3999)")
    
    roman = ''
    for value, numeral in ROMAN_NUMERAL_VALUES:
        while decimal >= value:
            roman += numeral
            decimal -= value
    return roman

def main() -> None:
    try:
        roman_input = input('Digite um número romano: ').upper()

        if not is_valid_roman(roman_input):
            raise ValueError(f"Número romano inválido: {roman_input}")

        decimal_input = int(input('Digite um número decimal: '))

        print(f'{roman_input} em decimal é {roman_to_decimal(roman_input)}')
        print(f'{decimal_input} em romano é {decimal_to_roman(decimal_input)}')
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()