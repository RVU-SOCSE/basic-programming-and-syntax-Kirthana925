Kirthana.K
1RUA25BCA0050



def word_count(sentence):
    count = 0
    for word in sentence.split():
        count += 1
    return count

text = input("Enter a sentence: ")
print("Number of words:", word_count(text))
