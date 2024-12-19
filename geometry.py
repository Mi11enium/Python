# Нахождение объёма в метрах кубических
# Для конвертации в литры, полученное значение нужно умножить на 1000

# Значения измерения берем в см
# Объём куба
a = 0.3
b = 0.4
c = 0.5

# CUBE
vol_cube_m3 = a ** 3  # formula

vol_cube_l = vol_cube_m3 * 1000

print(vol_cube_m3)
print(vol_cube_l)

# CUBOID
vol_cuboid_m3 = a * b * c  # formula

vol_cuboid_l = vol_cuboid_m3 * 1000
print(vol_cuboid_m3)
print(vol_cuboid_l)

# CYLINDER
pi = 3.14
h = 0.6
r = 0.04
vol_cylinder_m3 = pi * r ** 2 * h  # formula

vol_cylinder_l = vol_cylinder_m3 * 1000

print(vol_cylinder_m3)
print(vol_cylinder_l)
