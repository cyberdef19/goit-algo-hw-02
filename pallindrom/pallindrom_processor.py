from collections import deque

def pallindrom_processor(pallindrom_possible: str) -> bool:

    strqueue = deque()
    palpos = preprocessing(pallindrom_possible)
    #Додаємо символи рядка до двосторонньої черги
    [strqueue.append(x) for x in palpos]
    if len(strqueue) %2 == 0:
        #В такому випадку у палліндрома не повинно бути центрального символа
        return is_even_pallindrom(strqueue)
    else:
        #У такому випадку у палліндрома є центральний символ
        return is_odd_pallindrom(strqueue)

def preprocessing(palpos: str) -> str:
    palpos = palpos.lower()
    arr = palpos.split(" ")
    return "".join(arr)

def is_even_pallindrom(strqueue: deque) -> bool:
    i = 0
    center_index = (len(strqueue)/2) - 1
    while i <= center_index:
        left = strqueue.popleft()
        right = strqueue.pop()
        if left != right:
            return False
        i += 1
    return True

def is_odd_pallindrom(strqueue: deque) -> bool:
    center_index = int(len(strqueue)/2)
    i = 0
    while i < center_index:
        left = strqueue.popleft()
        right = strqueue.pop()
        if left != right:
            return False
        i += 1
    return True
