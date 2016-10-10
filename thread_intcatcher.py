"""
Simple 2-threaded script to read text from file and get correct integers
within the range [-1000000000, 1000000000]. File name is parsed from command
line. Try test_intcatcher.
"""
import threading
import argparse

from queue import Queue


def read_text(queue, file_object):
    text = open(file_object).read()
    text_to_list = text.split('\\n')
    for char in text_to_list:
        queue.put(char)
    queue.put(None)


def convert_text(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        try:
            if -1000000000 <= int(item) <= 1000000000:
                print(int(item))
        except ValueError or SyntaxError:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_object')
    args = parser.parse_args()
    q = Queue()
    reader_thread1 = threading.Thread(target=read_text,
                                      args=(q, args.file_object))
    reader_thread1.start()
    translator_thread2 = threading.Thread(target=convert_text, args=(q, ))
    translator_thread2.start()
    translator_thread2.join()


if __name__ == '__main__':
    main()
