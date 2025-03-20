class retangulo :
    base = 0.0
    altura = 0.0
    
    def calcular_Area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * self.base + 2 * self.altura
    
objretangulo = retangulo()
objretangulo.base = 2
objretangulo.altura = 4
print(objretangulo.calcular_Area())
print(objretangulo.calcular_perimetro())