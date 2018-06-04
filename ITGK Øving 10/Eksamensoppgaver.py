def file_to_list(filename):
    f = open(filename, "r")
    tabell = []
    for line in f:
        row = line.split("\t")
        row[2] = float(row[2])
        tabell.append(row)
    return tabell

def list_stores(dataList):
    lister_av_butikker = []
    for x in dataList:
        if x[0] not in lister_av_butikker:
            lister_av_butikker.append(x[0])
    return lister_av_butikker
def sum_price_stores(dataList, storeList):
    pris_liste =[0 for x in range(len(storeList))]
    for x in dataList:
        pris_liste[storeList.index(x[0])] += x[2]
    return pris_liste

def rank_stores(storeList, sumStores):
    ranking = []
    for x in range(len(storeList)):
        a = sumStores.index(min(sumStores))
        ranking.append(storeList[a])
        storeList.pop(a)
        sumStores.pop(a)
    return ranking

def store_analysis(filename):
    tabell = file_to_list(filename)
    storeNames = list_stores(tabell)
    storePrices = sum_price_stores(tabell, storeNames)
    rankings = rank_stores(storeNames, storePrices)
    print("The total price for shopping per store is:")
    for x in range(len(storeNames)):
        print(storeNames[x], ":", storePrices[x])
    print("The rankingof the these stores according to price is")
    for x in range(len(rankings)):
        print(x+1, rankings[x])