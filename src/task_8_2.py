"""2. Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)"""


def polindrom(a):
    b = [i[::-1] for i in a]
    q = {}
    for f in a:
        for g in b:
            if str(f) == str(g):
                q[g] = 'polindrom'
                b.remove(g)
                break
            else:
                q[g] = 'nepolindrom'
                b.remove(g)
                break
    print(q)


polindrom(['ama', 'mama', 'qwertytrewq'])
