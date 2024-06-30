from roman_numbers_class import RomanNumber

from roman_numbers_class import RomanNumber

def test_roman_to_arab():
    # Casos básicos
    assert RomanNumber("IV").roman_to_arab() == 4
    assert RomanNumber("IX").roman_to_arab() == 9
    assert RomanNumber("XXI").roman_to_arab() == 21
    assert RomanNumber("XLII").roman_to_arab() == 42
    assert RomanNumber("LXXVIII").roman_to_arab() == 78
    assert RomanNumber("XCIX").roman_to_arab() == 99
    assert RomanNumber("CXXV").roman_to_arab() == 125
    assert RomanNumber("CDXLIV").roman_to_arab() == 444
    assert RomanNumber("DCCCXC").roman_to_arab() == 890
    assert RomanNumber("CMXCIX").roman_to_arab() == 999
    assert RomanNumber("MCMXCIV").roman_to_arab() == 1994
    assert RomanNumber("MMMCMXCIX").roman_to_arab() == 3999

def test_arab_to_roman():
    # Casos básicos
    assert RomanNumber(4).arab_to_roman() == "IV"
    assert RomanNumber(9).arab_to_roman() == "IX"
    assert RomanNumber(21).arab_to_roman() == "XXI"
    assert RomanNumber(42).arab_to_roman() == "XLII"
    assert RomanNumber(78).arab_to_roman() == "LXXVIII"
    assert RomanNumber(99).arab_to_roman() == "XCIX"
    assert RomanNumber(125).arab_to_roman() == "CXXV"
    assert RomanNumber(444).arab_to_roman() == "CDXLIV"
    assert RomanNumber(890).arab_to_roman() == "DCCCXC"
    assert RomanNumber(999).arab_to_roman() == "CMXCIX"
