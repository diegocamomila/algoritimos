def partition(chars, start, end):
    delimiter = start - 1

    for index in range(start, end):
        if chars[index] <= chars[end]:
            delimiter = delimiter + 1
            chars[index], chars[delimiter] = (
                chars[delimiter],
                chars[index],
            )

    chars[delimiter + 1], chars[end] = chars[end], chars[delimiter + 1]

    return delimiter + 1


def quick_sort(chars, start, end):
    if start < end:
        p = partition(chars, start, end)
        quick_sort(chars, start, p - 1)
        quick_sort(chars, p + 1, end)


def is_anagram(first_string, second_string):
    chars_first_string = list(first_string.lower())
    chars_second_string = list(second_string.lower())

    quick_sort(chars_first_string, 0, len(chars_first_string) - 1)
    quick_sort(chars_second_string, 0, len(chars_second_string) - 1)

    if first_string == "" and second_string == "":
        result = False
    else:
        result = chars_first_string == chars_second_string

    return ("".join(chars_first_string), "".join(chars_second_string), result)
