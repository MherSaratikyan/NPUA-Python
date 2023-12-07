import os
import time
import threading
import multiprocessing

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time

    return wrapper

def create_large_text_file(file_path):
    latin_words = ["qui", "blanditiis", "praesentium", "voluptatum", "deleniti", "atque,", "corrupti", "quos"]
    with open(file_path, 'w') as large_text_file:
        for _ in range(10**3):
            sentence = "".join([latin_words[i % len(latin_words)] + " " for i in range(2**10)])
            large_text_file.write(sentence + "\n")

@measure_execution_time
def word_counter(file_name):
    word_frequencies = {}
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies

@measure_execution_time
def word_counter_multithread(file_name, num_threads):
    word_frequencies = {}

    def process_chunk(chunk):
        local_word_frequencies = {}
        for line in chunk:
            words = line.split()
            for word in words:
                local_word_frequencies[word] = local_word_frequencies.get(word, 0) + 1
        return local_word_frequencies

    with open(file_name, 'r') as file:
        lines = file.readlines()

    chunk_minimal_size = max(1, len(lines) // num_threads)
    chunks = [lines[i:i + chunk_minimal_size] for i in range(0, len(lines), chunk_minimal_size)]

    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=lambda: word_frequencies.update(process_chunk(chunk)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return word_frequencies

def process_chunk(chunk, frequency_dict):
    local_word_frequencies = {}
    for line in chunk:
        words = line.split()
        for word in words:
            local_word_frequencies[word] = local_word_frequencies.get(word, 0) + 1
    for key, value in local_word_frequencies.items():
        frequency_dict[key] = frequency_dict.get(key, 0) + value

@measure_execution_time
def word_counter_multiprocess(file_name, num_processes):
    word_frequencies = multiprocessing.Manager().dict()

    with open(file_name, 'r') as file:
        lines = file.readlines()

    chunk_minimal_size = max(1, len(lines) // num_processes)
    chunks = [lines[i:i + chunk_minimal_size] for i in range(0, len(lines), chunk_minimal_size)]

    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(target=process_chunk, args=(chunk, word_frequencies))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return dict(word_frequencies)


if __name__ == "__main__":
    num_threads = 8
    num_processes = 8

    
    file_path = "largeText.txt"
    create_large_text_file(file_path)

        
    _, seq_counting_time = word_counter(file_path)

    _, multithread_counting_time = word_counter_multithread(file_path, num_threads)

    _, multiprocess_counting_time = word_counter_multiprocess(file_path, num_processes)

    print(f"Sequential Execution Time: {seq_counting_time:.6f} sec")
    print(f"Multithreading Execution Time: {multithread_counting_time:.6f} sec")
    print(f"Multiprocessing Execution Time: {multiprocess_counting_time:.6f} sec")

    multithread_speedup = seq_counting_time / multithread_counting_time
    multiprocess_speedup = seq_counting_time / multiprocess_counting_time

    print(f"Multithreading Speedup: {multithread_speedup:.2f}x")
    print(f"Multiprocessing Speedup: {multiprocess_speedup:.2f}x")