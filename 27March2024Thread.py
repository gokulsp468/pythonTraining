import threading


def fact(start, end, result, lock):
    f = 1
    for i in range(start, end+1):
        f *= i
    with lock:
        result.append(f)


def main():
    num = int(input("enter the number"))
    thread_capacity = 4
    chunk_size = num // thread_capacity
    remainder = num % thread_capacity
    result = []
    lock = threading.Lock()
    threads = []

    for i in range(thread_capacity):
        start = i * chunk_size + 1
        end = start + chunk_size - 1

        if i == thread_capacity - 1:
            end += remainder

        thread = threading.Thread(target=fact, args=(start, end, result, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_result = 1
    for res in result:
        final_result *= res

    print(final_result)


if __name__ == '__main__':
    main()






