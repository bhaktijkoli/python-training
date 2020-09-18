# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given n scores.
# Store them in a list and find the score of the runner-up.

score_str = input("Enter scores\n")
score_list = score_str.split(" ")
highestScore = 0;
rupnnerUp = 0
for score in score_list:
    score = int(score)
    if score > highestScore:
        highestScore = score

for score in score_list:
    score = int(score)
    if score > rupnnerUp and score < highestScore:
        rupnnerUp = score

print(rupnnerUp)