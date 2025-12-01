def str_reverse (word):
    res = ""
    for i in range(len(word) - 1, -1, -1):
        res += word[i]
    print(res)