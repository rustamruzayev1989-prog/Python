import threading
from collections import Counter

def process_chunk(lines, result_list, lock):
    """Подсчёт слов в куске текста."""
    local_counter = Counter()
    for line in lines:
        # Разделяем на слова, приводим к нижнему регистру, убираем лишние символы
        words = [w.strip(".,!?;:\"'()[]").lower() for w in line.split()]
        words = [w for w in words if w]  # убираем пустые строки
        local_counter.update(words)

    # Потокобезопасное добавление в общий список результатов
    with lock:
        result_list.append(local_counter)

def threaded_word_count(filename, num_threads=4):
    # Считываем все строки файла
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Делим строки на равные части для каждого потока
    chunk_size = len(lines) // num_threads
    threads = []
    results = []
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        # последний поток берёт все оставшиеся строки
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
        t = threading.Thread(target=process_chunk, args=(lines[start:end], results, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Объединяем все локальные счётчики в один
    total_counter = Counter()
    for c in results:
        total_counter.update(c)

    return total_counter

if __name__ == "__main__":
    filename = "big_text_file.txt"   # замените на имя вашего файла
    word_counts = threaded_word_count(filename, num_threads=4)

    # Вывод 20 самых частых слов
    print("Топ 20 слов:")
    for word, count in word_counts.most_common(20):
        print(f"{word}: {count}")
