def get_count_char(str_):
    char_dict = {}
    for char in str_:
      if char.isalpha():
        char_ = char.lower()
        if char_ in char_dict:
          char_dict[char_] += 1
        else:
          char_dict[char_] = 1
    return char_dict  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
      Данное предложение будет разбиваться на отдельные слова. 
      В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
      Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
      """

print(get_count_char(main_str))


def get_char(dict_):
  sum_ = sum(dict_.values())
  for k in dict_:
      dict_[k]= round(dict_[k]/sum_,2)
  return dict_  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
      Данное предложение будет разбиваться на отдельные слова. 
      В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
      Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
      """

print(get_char(get_count_char(main_str)))

