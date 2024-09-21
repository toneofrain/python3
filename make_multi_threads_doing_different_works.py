import threading
import os

def foo():
    print('This is foo')
    print('thread id', threading.get_native_id())

def bar():
    print('This is bar')
    print('thread id', threading.get_native_id())

def baz():
    print('This is baz')
    print('thread id', threading.get_native_id())

if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread1 = threading.Thread(target=baz).start()

