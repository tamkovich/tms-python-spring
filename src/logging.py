from datetime import datetime


def log(args, file):
    with open(file, 'w') as f:
        f.write(f'{args.first_name}\n')
        f.write(f'{args.last_name}\n')
        f.write(f'{datetime.now()}\n')