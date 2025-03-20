def raio_esfera (x):
    volume = 4/3 * 3.141592 * x**3
    return volume
n = float(input('digite o raio da esfera: '))
o_volume = raio_esfera(n)
print(o_volume)