#Write a python program to find the longest word in a file.
f = open("demo.txt", "r")
line = f.readline()
longestWord = ""
while line:
    words = line.split(" ")
    lineLongestWord = max(words, key=len)
    if len(lineLongestWord) > len(longestWord):
        longestWord = lineLongestWord

    line = f.readline()

print("Longest word")
print(longestWord)