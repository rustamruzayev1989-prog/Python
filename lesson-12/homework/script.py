import threading

def is_prime(n: int) -> bool:
    """Проверка, является ли число простым."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_range(start: int, end: int, result: list):
    """Проверка поддиапазона чисел и добавление простых в общий список."""
    local_primes = [n for n in range(start, end + 1) if is_prime(n)]
    result.extend(local_primes)

def threaded_prime_check(start: int, end: int, num_threads: int = 4):
    step = (end - start + 1) // num_threads
    threads = []
    result = []  # общий список простых чисел
    lock = threading.Lock()  # для синхронизации доступа к result

    def safe_check(s, e):
        local_result = []
        check_range(s, e, local_result)
        with lock:  # безопасно добавляем найденные простые
            result.extend(local_result)

    for i in range(num_threads):
        s = start + i * step
        e = start + (i + 1) * step - 1 if i < num_threads - 1 else end
        t = threading.Thread(target=safe_check, args=(s, e))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return sorted(result)

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    primes = threaded_prime_check(start_range, end_range, num_threads=4)
    print(f"Простые числа от {start_range} до {end_range}:")
    print(primes)
