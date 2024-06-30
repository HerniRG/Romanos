from roman_numbers import roman_to_arabic, arabic_to_roman

"""
implementación de la clase RomanNumber
"""

class RomanNumber:
    def __init__(self, cadena):
        self.cadena = cadena
        if isinstance(cadena, str):
            self.value = self.roman_to_arab()
        if isinstance(cadena, (int, float)):  
            self.value = cadena

    def roman_to_arab(self):
        roman = self.cadena
        arab = 0
        value_character_anterior = 0
        isNegative = False
        for character in roman:
            if character == "-":
                isNegative = True
                roman = roman[1:]
                break


        for character in roman:
            try:
                actual_value = roman_to_arabic[character]
                if actual_value > value_character_anterior:
                    arab += actual_value - value_character_anterior - value_character_anterior # hay que restarlo dos veces porque se habia sumado anteriormente
                else:
                    arab += actual_value
                value_character_anterior = actual_value
            except KeyError:
                arab = "Número romano no válido"
                isNegative = False
                break
                
        if isNegative:
            arab *=- 1     

        return arab    

    def arab_to_roman(self):
        arab = int(round(self.cadena))
        isNegative = False
        if arab < 0:
            isNegative = True
            arab *= -1
        roman = ""

        for key, value in arabic_to_roman.items():
            while arab >= key: # si 1987 es mayor o igual a primer caso M 1000
                roman += value  # añade la letra M
                arab -= key  # y restamos 1000 para que quede 987 y volver a trabajar con el número restante

        if isNegative:
            roman = "-" + roman

        return roman
                        
    def __str__(self):
        if isinstance(self.cadena, str):
            return f"El número romano {self.cadena} es: {self.value}."
        if isinstance(self.cadena, (int, float)):  
            return f"El número {self.cadena} en romano: {self.value}."

    def __repr__(self):
        return f"RomanNumber({self.cadena})"
    
    def __add__(self, segundo_roman_number):
        if isinstance(segundo_roman_number, RomanNumber):
            suma = self.value + segundo_roman_number.value
            return RomanNumber(suma)
    
    def __mul__(self, segundo_roman_number):
        resultado = 0

        if isinstance(segundo_roman_number, (RomanNumber, int, float)):
            if isinstance(segundo_roman_number, RomanNumber):
                multiplicador = segundo_roman_number.value
            else:
                multiplicador = segundo_roman_number
            
            producto = self.value * multiplicador
            resultado = RomanNumber(producto)
                
        return resultado

    
    def __eq__(self, segundo_roman_number):
        isEqual = False
        if isinstance(segundo_roman_number, RomanNumber):
            isEqual = self.value == segundo_roman_number.value
        elif isinstance(segundo_roman_number, (int, float, str)):
            other_value = RomanNumber(segundo_roman_number).value
            isEqual = self.value == other_value
        return isEqual


    
# Ejemplo de uso
uno = RomanNumber(1)
dos = RomanNumber("II")
print(uno)
print(dos)
tres = uno + dos
print(tres)

print(tres == RomanNumber(3))  # True
print(tres == RomanNumber("III"))  # True

grande = tres * 1000
print(grande == RomanNumber("MMM"))  # True

mas_grande = grande * dos
print(mas_grande == RomanNumber("MMMMMM"))  # True