# Округление до ближайшего целого числа round()
average_price = 16.25
avr = round(average_price)
print(avr)

print(dir(average_price))


# float можно конвертировать между str, int, float

num_str = "10"
num_int = int(num_str)
print(type(num_int))

num_nint = 25
num_nstr = str(num_nint)
num_nstr = "25.5"
num_nfloat = float(num_nstr)
print(num_nfloat)
