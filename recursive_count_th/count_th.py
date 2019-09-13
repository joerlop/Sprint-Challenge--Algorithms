'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    i = 0
    count = 0

    if len(word) <= 1:
        return 0

    else:

        if word[0:2] == "th":
            return 1 + count_th(word[i + 1 : ])

        else:
            count += count_th(word[i + 1 : ])

    return count
    

print(count_th("thabcthefthghith"))