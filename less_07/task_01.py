"""
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **Вывод:** Парам пам-пам

"""


def word_rhythm(word):
    lines = word.split()
    counts = []
    for i in lines:
        words = i.split('-')
        counts.append(sum(1 for word in words for char in word.lower() if char in 'ауоиэыяюеё'))
    if len(set(counts)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"


correct_input = "пара-ра-рам рам-пам-папам па-ра-па-да"
incorrect_input = "Ви-ни -- Пух и (на-до) тык-ви --"
print(word_rhythm(correct_input))