from typing import List


def sort_words(words: List[str]) -> List[str]:
    words_sorted = lambda word : len(word)
    words.sort(key=words_sorted,reverse=True)
    return(words)
    pass


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers_list = lambda number: abs(number)
    numbers.sort(key=numbers_list)
    return(numbers)
    pass


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
