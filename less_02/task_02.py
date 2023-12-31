# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


def guess_the_number(s: int, p: int) -> str:
    x = (s - int((s ** 2 - 4 * p) ** 0.5)) // 2
    y = (s + int((s ** 2 - 4 * p) ** 0.5)) // 2
    return f'Загаданные числа: {x} и {y}'


try:
    s = int(input('Введите сумму чисел: '))
    p = int(input('Введите произведение чисел: '))
    if (s and p) < 1000:
        print(guess_the_number(s, p))
    else:
        print('Введите числа менее 1000.')
except ValueError:
    print('Что-то пошло не так. Повторите попытку.')
