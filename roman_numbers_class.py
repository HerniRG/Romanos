from roman_numbers import RomanNumbers, ArabicNumbers

"""
implementación de la clase RomanNumber
"""

class RomanNumber:
    def __init__(self, cadena):
        self.cadena = cadena

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
        
        # LA PRIMERA VEZ LO HE HECHO MUY ENREVESADO XD
        # for character in roman:       
        #     if index+1 < len(roman) and RomanNumbers[character].value < RomanNumbers[roman[index+1]].value :
        #         arab = arab - acum - RomanNumbers[character].value
        #         acum = 0
        #     elif index+1 < len(roman) and RomanNumbers[character].value == RomanNumbers[roman[index+1]].value:
        #         acum = acum + RomanNumbers[character].value
        #     elif index+1 < len(roman) and RomanNumbers[character].value > RomanNumbers[roman[index+1]].value:
        #         arab = arab + acum + RomanNumbers[character].value
        #         acum = 0
        #     elif index+1 >= len(roman):
        #         arab = arab + acum + RomanNumbers[character].value
        #     index += 1
        # if acum != 0:
        #     arab += acum

        print(arab)
        return arab    

    def arab_to_roman(self):
        arab = int(self.cadena)
        roman = ""

        for roman_letter in ArabicNumbers:
            while arab >= roman_letter.value: # si 1987 es mayor o igual a primer caso M 1000
                roman += roman_letter.name  # añade la letra M
                arab -= roman_letter.value  # y restamos 1000 para que quede 987 y volver a trabajar con el número restante

        print(roman)
        




                
    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass


a = RomanNumber(2)
a.arab_to_roman()
