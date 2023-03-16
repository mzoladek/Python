"""
Oto program sortujący napisy (ciągi liter/cyfr oraz znaków specjalnych) różnej długości
(zajmujące różne ilości pamięci), stosując sortowanie pozycyjne (od ostatniego znaku do pierwszego)
gdzie sortowanie według kolejnych znaków (nie rozróżniając dużych i małych liter) jest wykonane sortowaniem przez zliczanie. 
 
Sample Input:  

old owl bar sin set end bus kit arm lid tip hip hen joy win fax oil beg eye lie hot pit cat flu log nun fix say dip ban  

Sample Output:  

arm ban bar beg bus cat dip end eye fax fix flu hen hip hot joy kit lid lie log nun oil old owl pit say set sin tip win
"""


def get_ascii_value(word, char_number):

    if char_number < len(word):

        if word[char_number].isalpha() is False:

            return ord(word[char_number])

        elif word[char_number].isalpha() is True:

            return ord(word[char_number].upper())

    else:

        return 0


def countingSort(a, char_number):

    ascii_size = 127

    a_size = len(a)

    b = [0] * a_size

    c = [0] * ascii_size

    for word in a:

        ascii_val = get_ascii_value(word, char_number)

        c[ascii_val] += 1

    for i in range(1, ascii_size):

        c[i] += c[i - 1]

    i = a_size - 1

    while i >= 0:

        ascii_val = get_ascii_value(a[i], char_number)

        b[c[ascii_val] - 1] = a[i]

        c[ascii_val] -= 1

        i -= 1

    for i in range(0, a_size):

        a[i] = b[i]

    return a


def radixSort(word_array):

    max_word_len = len(max(word_array, key=len))

    for char_number in range(max_word_len - 1, -1, -1):

        word_array = countingSort(word_array, char_number)

    return word_array


word_array = input().split()

radixSort(word_array)

result = ""


for word in word_array:

    result += word + " "


print(result[:-1])
