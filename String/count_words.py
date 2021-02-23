
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
# count at the end
def count_words1(s):
    found = False # if found a word
    words = 0
    for i in range(len(s)):
        if is_delimiter(s[i]) == False:
            found = True
        if found == True and is_delimiter(s[i]) == True:
            found = False
            words += 1 # add at the end of word
    if found == True: # the last word
        words += 1

    return words

# count at the beginning
def count_words(s):
    found = False
    words = 0

    for i in range(len(s)):
        # start of the word
        if is_delimiter(s[i]) == False and found == False:
            found = True
            words += 1
        if is_delimiter(s[i]) == True:
            found = False
    return words







s = "A ,   beautiful dog haha"

