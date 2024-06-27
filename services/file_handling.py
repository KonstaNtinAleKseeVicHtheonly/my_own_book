"""Файл с хранением книги (текст книги будет хранится в словаре, 
где ключ-номер страницы, значение-текст книги)"""
import os
import sys
BOOK_PATH = 'D:\confession_of_economic_killer\mars.txt' # вставить сюда свой текстовый формат книги в файле txt
PAGE_SIZE = 1050 # лиммт символов для одной страницы

book: dict[int, str] = {}


def _get_part_text(text:str,start,size):
    end_signs = ',.!:;?'
    counter = 0
    if len(text) < start + size:
        size = len(text) - start
        text = text[start:start + size]
    else:
        if text[start + size] == '.' and text[start + size - 1] in end_signs:
            text = text[start:start + size - 2]
            size -= 2
        else:
            text = text[start:start + size]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size



def prepare_book(path: str) -> None:
    page_counter = 1
    beginning = 0
    with open (path,'r') as our_book:
        hz = our_book.read()
        while beginning < len(hz):
                book[page_counter] = _get_part_text(hz,beginning,PAGE_SIZE)[0].strip()
                beginning += _get_part_text(hz,beginning,PAGE_SIZE)[1]
                page_counter += 1

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH))) # что бы книга читалась на любых ОС(LINUX,MACOS)