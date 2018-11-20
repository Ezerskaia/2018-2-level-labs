"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
def read_from_file(path_to_file, lines_limit: int) -> str:
    my_text = ''
    count_lines = 0
    my_file = open(path_to_file, 'r')
    for line in my_file.read():
        if count_lines == lines_limit:
            return my_text
        my_text += line
        count_lines += 1
    my_file.close()
    return my_text


def calculate_frequences(text: str) -> dict:
    first_dict = {}
    list_of_marks = [
                    '.', ',', ':', '"', '`', '[', ']',
                    '?', '!', '@', '&', "'", '-',
                    '$', '^', '*', '(', ')',
                    '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                    ]
    try:
        elements = text.split()
    except AttributeError:
        return first_dict
    for thing in elements:
        if thing.isdigit():
            continue
        for mark in list_of_marks:
            if mark in thing:
                pos_mark = thing.find(mark)
                thing = thing[:pos_mark] + thing[pos_mark + 1:]
            thing = thing.strip(mark)
        thing = thing.lower()
        first_dict[thing] = first_dict.get(thing, 0) + 1
    if '' in first_dict.keys():
        first_dict.pop('')
    return first_dict


def filter_stop_words(vocabulary: dict, stop_words: tuple)-> dict:
    if not isinstance(vocabulary, dict):
        return {}
    if not isinstance(stop_words, tuple):
        return vocabulary
    del_list = []
    for key in vocabulary.keys():
        if key in stop_words:
            del_list.append(key)
        if not isinstance(key, str):
            del_list.append(key)
    for element in del_list:
        vocabulary.pop(element)
    return vocabulary

def get_top_n(vocabulary: dict, n_top_words: int)-> tuple:
    if n_top_words < 0:
        return ()
    for key, value in third_dict.items():
        list_of_value_key.append([value, key])
    list_of_value_key.sort(reverse=True)
    for item in list_of_value_key:
        if count == top_n:
            break
        list_of_top_words.append(item[1])
        count += 1
    return tuple(list_of_top_words)


def write_to_file(path_to_file: str, content: tuple):
    my_file = open(path_to_file, 'w')
    for word in content:
        my_file.write(word + '\n')
    my_file.close()
