def fixing(stats, nt):
    # Organizando a tabela
    for i in range(len(stats)):
        if (not stats[i].isalpha() and '-' not in stats[i] and '.' not in stats[i] and '&' not in stats[i] and '\'' not in stats[i]):
            if (int(stats[i]) <= nt*2):
                posstats = i
                break
    team = stats[:posstats]
    team = ' '.join(team)
    pld = int(stats[posstats])
    gm = int(stats[posstats + 1])
    gd = int(stats[posstats + 2])
    pts = int(stats[posstats + 3])
    stat = [pld, gm, gd, pts]
    return team, stat

# Retorna a posição do time
def indexTeam(teamname, teams):
    for i in range(len(teams)):
        if (teamname == teams[i]):
            return i

def validMatch(twoteams):
    for team in twoteams:
        if (indexTeam(team, teams) == None):
            return False
    return True

def changingstats(teams, twoteams, allstats, home, away, homescore, awayscore):
    #Define se é o time da casa ou não
    try:
        if(validMatch(twoteams)):
            for team in twoteams:
                i = indexTeam(team, teams)
                if (team == home):
                    ishome = True
                else:
                    ishome = False
                if (homescore != 'A'):
                    if (ishome):
                        gd = homescore-awayscore
                        #Mais um jogo
                        allstats[i][0]+=1
                        allstats[i][2]+=(gd)
                        allstats[i][1]+=(homescore)
                        if (gd > 0):
                            allstats[i][3]+=3
                        elif (gd == 0):
                            allstats[i][3]+=1
                    else:
                        gd = awayscore-homescore
                        #Mais um jogo
                        allstats[i][0]+=1
                        allstats[i][2]+=(gd)
                        allstats[i][1]+=(awayscore)
                        if (gd > 0):
                            allstats[i][3]+=3
                        elif (gd == 0):
                            allstats[i][3]+=1
    except:
        print("Mudei a tabela e olha no que deu")

def fixingteams(match, teams, shortnames):
    try:
        home = shortnames[match[0]]
        away = shortnames[match[2]]
        twoteams = [home, away]
        result = match[1].split('-')
        if (result[0] == "A"):
            homescore = 'A'
            awayscore = 'A'
        elif(result[0] == "D"):
            homescore = 'A'
            awayscore = 'A' 
        else:
            homescore = int(result[0])
            awayscore = int(result[1])
        changingstats(teams, twoteams, allstats, home, away, homescore, awayscore)
    except:
        print("Foi quando errou o placar")

def infront(teams, i, j):
    # Aqui, j deve ser maior que i.
    for k in range (4,1,-1):
        # Primeiro compara os pontos e dps saldo de gols
        if (teams[i][k] > teams[j][k]):
            return False
        elif (teams[j][k] > teams[i][k]):
            return True


    # Se empatou, o desempate é pelo nome, pq n tem gols marcados
    if (teams[j][0] < teams[i][0]):
        return True
    else:
        return False

def sorting(teams):
    for i in range(1, len(teams)):
        j = i
        while j > 0 and infront(teams, j-1, j):
            aux = teams[j]
            teams[j] = teams[j-1]
            teams[j-1] = aux
            j-=1

def splitting(stats, nt):
    for i in range(len(stats)):
        if (not stats[i].isalpha() and '&' not in stats[i]):
            if (int(stats[i]) <= nt*2):
                posstats = i
                break
    team = stats[:posstats]
    team = ' '.join(team)

    pld = int(stats[posstats])
    gd = int(stats[posstats + 2])
    pts = int(stats[posstats + 3])
    stat = [pld, gd, pts]
    return team, stat

def callteams():
    # Fiz essa função só pra diminuir isso na hora de editar. Ô treco chato.
    shortnames['ACC'] = 'Accrington Stanley'
    shortnames['WIM'] = 'AFC Wimbledon'
    shortnames['ARS'] = 'Arsenal'
    shortnames['AVL'] = 'Aston Villa'
    shortnames['BAR'] = 'Barnsley'
    shortnames['BRW'] = 'Barrow'
    shortnames['BIR'] = 'Birmingham City'
    shortnames['BLB'] = 'Blackburn Rovers'
    shortnames['BLP'] = 'Blackpool'
    shortnames['BOL'] = 'Bolton Wanderers'
    shortnames['BOU'] = 'Bournemouth'
    shortnames['BRD'] = 'Bradford City'
    shortnames['BRE'] = 'Brentford'
    shortnames['BHA'] = 'Brighton'
    shortnames['BRC'] = 'Bristol City'
    shortnames['BRR'] = 'Bristol Rovers'
    shortnames['BUR'] = 'Burnley'
    shortnames['BRT'] = 'Burton Albion'
    shortnames['CAM'] = 'Cambridge United'
    shortnames['CAR'] = 'Cardiff City'
    shortnames['CRL'] = 'Carlisle United'
    shortnames['CHA'] = 'Charlton Athletic'
    shortnames['CHE'] = 'Chelsea'
    shortnames['CHL'] = 'Cheltenham Town'
    shortnames['COL'] = 'Colchester United'
    shortnames['COV'] = 'Coventry City'
    shortnames['CRA'] = 'Crawley Town'
    shortnames['CRE'] = 'Crewe Alexandra'
    shortnames['CRY'] = 'Crystal Palace'
    shortnames['DER'] = 'Derby County'
    shortnames['DON'] = 'Doncaster Rovers'
    shortnames['EVE'] = 'Everton'
    shortnames['EXE'] = 'Exeter City'
    shortnames['FUL'] = 'Fulham'
    shortnames['FLT'] = 'Fleetwood Town'
    shortnames['FGR'] = 'Forest Green Rovers'
    shortnames['GIL'] = 'Gillingham'
    shortnames['HAR'] = 'Hartlepool United'
    shortnames['HRR'] = 'Harrogate Town'
    shortnames['HUD'] = 'Huddersfield Town'
    shortnames['HUL'] = 'Hull City'
    shortnames['IPS'] = 'Ipswich Town'
    shortnames['LEE'] = 'Leeds United'
    shortnames['LEI'] = 'Leicester City'
    shortnames['LEY'] = 'Leyton Orient'
    shortnames['LIN'] = 'Lincoln City'
    shortnames['LIV'] = 'Liverpool'
    shortnames['LUT'] = 'Luton Town'
    shortnames['MCI'] = 'Manchester City'
    shortnames['MUN'] = 'Manchester United'
    shortnames['MAN'] = 'Mansfield Town'
    shortnames['MID'] = 'Middlesbrough'
    shortnames['MIL'] = 'Millwall'
    shortnames['MKD'] = 'Milton Keynes Dons'
    shortnames['MOR'] = 'Morecambe'
    shortnames['NEW'] = 'Newcastle United'
    shortnames['NPC'] = 'Newport County'
    shortnames['NTH'] = 'Northampton Town'
    shortnames['NOR'] = 'Norwich City'
    shortnames['NFO'] = 'Nottingham Forest'
    shortnames['OLD'] = 'Oldham Athletic'
    shortnames['OXF'] = 'Oxford United'
    shortnames['PET'] = 'Peterborough United'
    shortnames['PLY'] = 'Plymouth Argyle'
    shortnames['POR'] = 'Portsmouth'
    shortnames['PVL'] = 'Port Vale'
    shortnames['PNE'] = 'Preston North End'
    shortnames['QPR'] = 'Queens Park Rangers'
    shortnames['REA'] = 'Reading'
    shortnames['ROC'] = 'Rochdale'
    shortnames['ROT'] = 'Rotherham United'
    shortnames['SAL'] = 'Salford City'
    shortnames['SCU'] = 'Scunthorpe United'
    shortnames['SHU'] = 'Sheffield United'
    shortnames['SHW'] = 'Sheffield Wednesday'
    shortnames['SHR'] = 'Shrewsbury Town'
    shortnames['SOU'] = 'Southampton'
    shortnames['STE'] = 'Stevenage'
    shortnames['STK'] = 'Stoke City'
    shortnames['SUN'] = 'Sunderland'
    shortnames['SUT'] = 'Sutton United'
    shortnames['SWA'] = 'Swansea City'
    shortnames['SWI'] = 'Swindon Town'
    shortnames['TOT'] = 'Tottenham'
    shortnames['TRA'] = 'Tranmere Rovers'
    shortnames['WAL'] = 'Walsall'
    shortnames['WAT'] = 'Watford'
    shortnames['WBA'] = 'West Bromwich'
    shortnames['WHU'] = 'West Ham'
    shortnames['WIG'] = 'Wigan Athletic'
    shortnames['WOL'] = 'Wolverhampton'
    shortnames['WYC'] = 'Wycombe Wanderers'
    
    #Non-League
    shortnames['ALD'] = 'Aldershot Town'
    shortnames['ALT'] = 'Altrincham'
    shortnames['BNT'] = 'Barnet'
    shortnames['BOR'] = 'Boreham Wood'
    shortnames['BRO'] = 'Bromley'
    shortnames['CHF'] = 'Chesterfield'
    shortnames['DAG'] = 'Dagenham & Redbridge'
    shortnames['DOV'] = 'Dover Athletic'
    shortnames['EAS'] = 'Eastleigh'
    shortnames['GRI'] = 'Grimsby Town'
    shortnames['HAL'] = 'FC Halifax Town'
    shortnames['KLT'] = 'King\'s Lynn Town'
    shortnames['MDH'] = 'Maidenhead United'
    shortnames['NOT'] = 'Notts County'
    shortnames['SOL'] = 'Solihull Moors'
    shortnames['SND'] = 'Southend United'
    shortnames['STC'] = 'Stockport County'
    shortnames['TOR'] = 'Torquay United'
    shortnames['WEA'] = 'Wealdstone'
    shortnames['WEY'] = 'Weymouth'
    shortnames['WOK'] = 'Woking'
    shortnames['WRE'] = 'Wrexham'
    shortnames['YEO'] = 'Yeovil Town'

shortnames = {}
callteams()
s = ["J", "GM", "SG", "Pts"]
files = ["PL", "Champ","League1","League2","Nat"]

for item in files:
    teams = []
    allstats = []
    f = open(item+"-R.txt", "r")
    t = open(item+"-T.txt", "w")
    tf = open(item+"-TF.txt", "w")
    lp = f.read().split('\n')
    numTeams = int(lp[0])

    for i in range(1, numTeams+1):
        try:
            stats = lp[i].split(' ')
            team, stat = fixing(stats, numTeams)
            teams.append(team)
            allstats.append(stat)
        except:
            print("Algo deu errado na tabela")
    # Parte que lê os resultados
    numMatches = int(lp[numTeams+1])
    for i in range(numMatches):
        try:
            match = lp[numTeams+2+i].split(' ')
            fixingteams(match, teams, shortnames)
        except:
            print("Algo deu errado com os times")
    t.write(str(numTeams)+'\n')
    for i in range(len(teams)):
        teams[i] = [teams[i], allstats[i][0], allstats[i][1], allstats[i][2], allstats[i][3]]
    sorting(teams)
    
    for team in teams:
        print(team[0], team[1], team[2], team[3], team[4])
        t.write(str(team[0]) + ' ' + str(team[1]) + ' ' + str(team[2]) + ' ' + str(team[3]) + ' ' + str(team[4]) + '\n')

    for i in range(len(teams)):
        teams[i] = [teams[i][0], teams[i][1], teams[i][3], teams[i][4]]

    numTeams = len(teams)

    for j in range(len(teams[0])):
        #print(s[j])
        for i in range(len(teams)):
            tf.write(str(teams[i][j]) +'\n')
        tf.write('\n')
    f.close()
    t.close()
    tf.close()
