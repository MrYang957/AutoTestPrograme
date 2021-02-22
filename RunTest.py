import pytest
import threading

def Run():
    print('This isanadded Thread,number is %s'% threading.current_thread())



def main():
    added_thread=threading.Thread(target=Run)
    added_thread.start()




if __name__ == '__main__':
    main()