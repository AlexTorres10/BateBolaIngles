files = ["PL", "Champ","League1","League2","Nat"]
numTeams = [20,24,24,24,23]


for (num,item) in zip(numTeams,files):
    f = open(item+"-TF.txt", "r")
    r = open(item+"-R.txt","w")
    lp = f.read().split('\n')
    teams = lp[:num]
    teams.sort()
    r.write(str(num)+'\n')
    for i in range(len(teams)):
        r.write(teams[i] + " 0 0 0 0"+'\n')
    r.write("0\n")
    r.close()
    f.close()
