
## Zum testen des erstellen des Leaderboards in normal Python
import csv
leaderboard = ""
board = " "
score = "99"
username =" le"
pos = 1

with open ("Leaderboard.csv", "a", newline='') as file:
    fields=['score', 'name']
    writer=csv.DictWriter(file, fieldnames=fields)
    writer.writerow({'score' : score, 'name' : username})

with open ("Leaderboard.csv", "r") as file:
    sortlist=["Highscore-Liste"]
    reader=csv.reader(file)
    for i in reader:
        sortlist.append(i)
for i in range(len(sortlist)):
    if i != 0:
        sortlist[i][0]=str(sortlist[i][int(0)])



for i in range(555):
    for i in range(len(sortlist)-1):
        if i != 0:
            if sortlist[i][0] < sortlist[i+1][0]:
                change=sortlist[i]
                sortlist[i]=sortlist[i+1]
                sortlist[i+1]=change

for i in range(len(sortlist)-1):
    leaderboard = leaderboard+"".join(sortlist[i])+ "\n"+str(pos) + ". " 
    pos = pos + 1

print (leaderboard)
