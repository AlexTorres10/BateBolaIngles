#!/usr/bin/env python
# coding: utf-8

# In[1]:

import win32com.client
import math

def callteams():
    shortnames = {}
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
    return shortnames

def readmatches(f, numTeams):
    shortnames = callteams()
    lp = f.read().split('\n')
    numMatches = int(lp[numTeams+1])
    matchlist = []
    for i in range(numMatches):
        try:
            match = lp[numTeams+2+i].split(' ')
            matchlist.append([shortnames[match[0]],shortnames[match[2]],match[1]])
        except:
            matchlist.append(['ERRO','ERRO','ERRO'])
            print("Algo deu errado com os times")
    maxMatches = numTeams // 2
    diff = maxMatches - numMatches
    if (diff > 0):
        layers = list(range(maxMatches))[math.floor(diff/2):maxMatches-math.ceil(diff/2)]
    else:
        layers = list(range(maxMatches))
    return matchlist, layers

psApp = win32com.client.Dispatch("Photoshop.Application")


# In[3]:


files = ["Champ","League1","League2","Nat"]
full_name = ["EFL Championship","EFL League 1","EFL League 2","National League"]
teams  = [24, 24, 24, 23]
div = 2

for item, league, numTeams in zip(files,full_name,teams):
    print("Atualizando a",league)
    f = open(item+"-R.txt", "r")
    all_layers, matches = readmatches(f, numTeams)
    
    if (len(matches) > 0):
        psApp.Open("C:\\Users\\Alex Torres\\Desktop\\BBI\\Templates\\1. Ligas\\"+str(div)+" - "+league+"\\"+item+"-Resultados.psd")
        # C:\Users\Alex Torres\Desktop\BBI\Templates\1. Ligas
        doc = psApp.Application.ActiveDocument

        if (len(matches) < (numTeams//2)):
            for i in range(numTeams//2):
                layer_home = doc.ArtLayers['HOME '+ str(i+1)]
                layer_away = doc.ArtLayers['AWAY '+str(i+1)]
                layer_result = doc.ArtLayers['RESULT '+str(i+1)]
                layer_crest_home = doc.ArtLayers['CREST HOME '+str(i+1)]
                layer_crest_away = doc.ArtLayers['CREST AWAY '+str(i+1)]
                if i in matches:
                    layer_home.visible = True
                    layer_away.visible = True
                    layer_result.visible = True
                    layer_crest_home.visible = True
                    layer_crest_away.visible = True
                else:
                    layer_home.visible = False
                    layer_away.visible = False
                    layer_result.visible = False
                    layer_crest_home.visible = False
                    layer_crest_away.visible = False
                    
        for layer, i in zip(all_layers,matches):
            layer_home = doc.ArtLayers['HOME '+ str(i+1)]
            layer_away = doc.ArtLayers['AWAY '+str(i+1)]
            layer_result = doc.ArtLayers['RESULT '+str(i+1)]
            layer_crest_home = doc.ArtLayers['CREST HOME '+str(i+1)]
            layer_crest_away = doc.ArtLayers['CREST AWAY '+str(i+1)]
            if i in matches:
                layer_home.TextItem.contents = layer[0]
                layer_away.TextItem.contents = layer[1]
                layer_result.TextItem.contents = layer[2]
                layer_home.visible = True
                layer_away.visible = True
                if layer[2] != 'D-D':
                    layer_result.visible = True
                else:
                    layer_result.visible = False
                layer_crest_home.visible = True
                layer_crest_away.visible = True
            else:
                layer_home.visible = False
                layer_away.visible = False
                layer_result.visible = False
                layer_crest_home.visible = False
                layer_crest_away.visible = False
        psApp.Open("C:\\Users\\Alex Torres\\Desktop\\BBI\\Templates\\1. Ligas\\"+str(div)+" - "+league+"\\"+item+"-Tabela.psd")
    print(league,"atualizada!")
    div+=1

