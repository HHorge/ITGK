cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

#Oppgave a)

print(cheeses["port salut"])
print(cheeses.keys())

#oppgave b)
infectedCheeses = []
infectedShelves = ['B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4',
                   'A234-2', 'A234-3', 'A234-4', 'A234-5', 'A235-1', 'A235-2', 'A235-3','A235-4',
                   'C31-1', 'C31-2']
for key, element in cheeses.items():

        for x in element:
            if x in infectedShelves and key not in infectedCheeses:
                infectedCheeses.append(key)
            if x not in infectedShelves and key not in infectedCheeses:

                print(x,key)


print(infectedCheeses)
for key, value in cheeses.items():
    if key not in infectedCheeses:
        for x in value:
            print(x, key)
