# Consider that vowels in the alphabet are a, e, i, o, u and y.
# Function score_words takes a list of lowercase words as an
# argument and returns a score as follows:
# The score of a single word is 2 if the word contains an even number
# of vowels. Otherwise, the score of this word is 1 . The score for the
# whole list of words is the sum of scores of all words in the list.
# Debug the given function score_words such that it returns a correct
# score.

# Rules:
# even number of vowels then score is 2
# odd number of vowels then score is 1

vowels = ["a", "e", "i", "o", "u"]

def score_word(word):
    v = 0
    for c in word:
        if c in vowels:
            v += 1

    if v % 2 == 0:
        return 2
    else:
        return 1

def score_words(words):
    score = 0;
    for word in words:
        score += score_word(word)
    return score

sentance = input("Enter a sentance\n")
words = sentance.split(" ")
print(score_words(words))