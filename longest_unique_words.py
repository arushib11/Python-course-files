# A function thay accepts a list of strings that represent a word and a positive integer n,
# representing number of words to return. Function should return new list, containing n longest unique words

#words = ["Longer", "Whatever", "Longer","Ball", "Rock", "Rocky", "Rocky","weeped","books"]

def get_n_longest_unique_words(words,n):
    list_phase_1=[]
    for word in words:
        w=words.count(word)
        if w==1:
            list_phase_1.append(word)

    list_phase_mid=[]
    count=0

    def func(elem):
        return len(elem)
    list_phase_mid=sorted(list_phase_1,reverse=True,key=func)
    return list_phase_mid[:n]

lst=get_n_longest_unique_words(["Longer", "Whatever", "Longer","Ball", "Rock", "Rocky", "Rocky"],3)
print(lst)

# Learnt the importance of slice



