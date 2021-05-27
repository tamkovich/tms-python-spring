pupils = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Stepa',
        'Group': 42,
        'physics': 2,
        'informatics': 3,
        'history': 4,
    },
    {
        'firstname': 'Zeka',
        'Group': 42,
        'physics': 5,
        'informatics': 7,
        'history': 5,
    },
]
pupils.append(
    {
        'firstname': 'Liza',
        'Group': 42,
        'physics': 9,
        'informatics': 8,
        'history': 6,
        'english': 10
    }
)
pupils.append(
    {
        'firstname': 'Petr',
        'Group': 42,
        'physics': 9,
        'history': 6,
    }
)
SUBJECT_SET = {
    "physics",
    "history",
    "english",
    "informatics",
    "math",
    "russian",
    "music",
}

# Step 3
for person in pupils:
    summa = 0
    count_lessons = 0
    for subject, value in person.items():
        if subject in SUBJECT_SET:
            # print(subject, end='; ')
            summa += value
            count_lessons += 1
    if summa > 0 and summa / count_lessons > 4:
        print(person['firstname'])
        print("Сумма всех оценок:", summa)
        print("Среднее по всем оценкам ученика:", summa / count_lessons)
        print()
