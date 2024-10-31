import string

class WordsFinder:
    def __init__(self, *file_names):
        # Создаем атрибут для хранения имён файлов в виде кортежа
        self.file_names = file_names

    def get_all_words(self):
        # Подготовительный метод для получения всех слов из файлов
        all_words = {}
        # Задаем набор знаков пунктуации, от которых нужно избавиться
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем текст и приводим к нижнему регистру
                    content = file.read().lower()
                    # Удаляем указанные знаки пунктуации
                    for p in punctuation:
                        content = content.replace(p, ' ')
                    # Разбиваем текст на слова по пробелам
                    words = content.split()
                    # Добавляем список слов в словарь
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        # Метод для поиска первой позиции слова
        word = word.lower()
        results = {}
        for name, words in self.get_all_words().items():
            try:
                # Находим индекс первого вхождения слова
                index = words.index(word)
                results[name] = index
            except ValueError:
                # Если слово не найдено, оно не добавляется в словарь
                continue
        return results

    def count(self, word):
        # Метод для подсчета количества вхождений слова
        word = word.lower()
        counts = {}
        for name, words in self.get_all_words().items():
            # Подсчитываем количество вхождений слова
            counts[name] = words.count(word)
        return counts

# Пример использования класса
finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())  # Все слова из файлов
print(finder1.find('TEXT'))     # Позиция первого вхождения слова
print(finder1.count('teXT'))    # Количество вхождений слова

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())  # Все слова из файлов
print(finder1.find('Child'))     # Позиция первого вхождения слова
print(finder1.count('Child'))    # Количество вхождений слова

finder1 = WordsFinder('Rudyard Kipling - If.txt')
print(finder1.get_all_words())  # Все слова из файлов
print(finder1.find('if'))     # Позиция первого вхождения слова
print(finder1.count('if'))    # Количество вхождений слова

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())  # Все слова из файлов
print(finder1.find('captain'))     # Позиция первого вхождения слова
print(finder1.count('captain'))    # Количество вхождений слова
