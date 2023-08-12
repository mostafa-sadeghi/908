# def getChessSquareColor(row, col):
#     if row % 2 == col % 2:
#         return 'white'
#     return 'black'


# print(getChessSquareColor(0, 0))
# print(getChessSquareColor(1, 0))
# print(getChessSquareColor(1, 1))
# print(getChessSquareColor(1, 3))
# print(getChessSquareColor(5, 8))
# print(getChessSquareColor(4, 6))
# print(getChessSquareColor(7, 3))


# def find_and_replace(sentense, old_word, new_word):
#     replaced_text = ''
#     i = 0
#     while i < len(sentense):
#         if sentense[i:i+len(old_word)] == old_word:
#             replaced_text += new_word
#             i += len(old_word)

#         else:
#             replaced_text += sentense[i]
#             i += 1

#     return replaced_text


# print(find_and_replace('The fox', 'fox', 'dog'))  # The dog
# print(find_and_replace('Firefox', 'fox', 'dog'))  # Firedog
# print(find_and_replace('The fox and fox.', 'fox', 'dog'))  # The dog and dog.


# TODO

"""
تابعی بنویسید که یک عدد از ورودی دریافت نماید 
و عدد را تبدیل به ساعت دقیقه و ثانیه نماید


get_hours_minuts_seconds(30)       ->     30s
get_hours_minuts_seconds(60)       ->     1m
get_hours_minuts_seconds(90)       ->     1m 30s
get_hours_minuts_seconds(3600)     ->     1h
get_hours_minuts_seconds(3601)     ->     1h 1s


"""
