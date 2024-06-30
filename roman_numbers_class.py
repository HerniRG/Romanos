from roman_numbers import RomanNumbers, ArabicNumbers

"""
implementación de la clase RomanNumber
"""

class RomanNumber:
    def __init__(self, cadena):
        self.cadena = cadena
        if isinstance(cadena, str):
            self.roman_to_arab()
        if isinstance(cadena, (int, float)):  
            self.arab_to_roman()

    def roman_to_arab(self):
        roman = self.cadena
        arab = 0
        value_character_anterior = 0

        for character in roman:
            try:
                actual_value = RomanNumbers[character].value
                if actual_value > value_character_anterior:
                    arab += actual_value - value_character_anterior - value_character_anterior # hay que restarlo dos veces porque se habia sumado anteriormente
                else:
                    arab += actual_value
                value_character_anterior = actual_value
            except KeyError:
                print(f"Caracter {character} no está en ROMAN NUMBERS.")
                break
        
       
        print(arab)
        return arab    

    def arab_to_roman(self):
        arab = int(round(self.cadena))
        roman = ""

        for roman_letter in ArabicNumbers:
            while arab >= roman_letter.value: # si 1987 es mayor o igual a primer caso M 1000
                roman += roman_letter.name  # añade la letra M
                arab -= roman_letter.value  # y restamos 1000 para que quede 987 y volver a trabajar con el número restante

        print(roman)
        return roman
                        
    def __str__(self) -> str:
        if isinstance(self.cadena, str):
            arab_value = self.roman_to_arab()
            return f"El número romano {self.cadena} es: {arab_value}."
        if isinstance(self.cadena, (int, float)):  
            roman_value = self.arab_to_roman()
            return f"El número {self.cadena} es en romano: {roman_value}."

    def __repr__(self) -> str:
        return f"RomanNumber({self.cadena})"