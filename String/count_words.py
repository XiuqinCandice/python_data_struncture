
def is_delimiter(s):
    pass

# counts words in String

def count_words(s):
    words = 0
    # i = 0
    if len(s) == 1 and is_delimiter(s[0]) == False:
        words += 1

    for i in range(len(s)-1):
        if is_delimiter(s[i]) == False:
            if is_delimiter(s[i+1]) == True:
                words += 1
            if i == len(s)-2 and is_delimiter(s[i+1]) == False:
                words += 1
    return words



S = "this is a cat."

def count_words1(s):
    found = False # if found a word
    words = 0
    for i in range(len(s)):
        if is_delimiter(s[i]) == False:
            found = True
        if found == True and is_delimiter(s[i]) == True:
            words += 1
        if is_delimiter(s[i]) == True:
            found = False
    if found == True: # the last word
        words += 1

    return words

            








s = "A ,   beautiful dog haha"

