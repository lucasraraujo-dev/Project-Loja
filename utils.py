import os

def pause_terminal():
    os.system("read -p 'press any key to resume ...'")
    
    
def clear_terminal():
    os.system("cls")
    
    
def clear_and_print(print_buffer):
    clear_terminal()
    print(print_buffer)