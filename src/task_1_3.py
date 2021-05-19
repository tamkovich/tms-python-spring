# Задача 1.3
# Дана длина ребра куба.
# Найти объем куба и площадь его боковой поверхности.

cube_edge_len = 70

cube_volume = cube_edge_len ** 3  # Cube volume
cube_surf_area = 6 * (cube_edge_len ** 2)  # Area of cube surface

print(f'Length of cube edge: {cube_edge_len}',
      f'Volume of cube: {cube_volume}',
      f'Area of cube surface: {cube_surf_area}', sep="\n")
