line_4 = "123416789"
midle_line = int(len(line_4) / 2)
print(f"центральный символ - {line_4[midle_line]}")
if line_4[0] == line_4[midle_line]:
    print(f"первый символ совпал с центральным \n  новая строка - 111{line_4[1:-1]}")
