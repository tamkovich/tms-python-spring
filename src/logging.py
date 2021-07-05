

def log(file, info_to_log):
    with open(file, 'w') as f:
        f.write(f'{info_to_log}\n')