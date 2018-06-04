file = "numbers.txt"

#Oppgave a)

def numberOfLines(filename):
    with open(filename) as f:
        #print(f.read())
        lineCount = 0
        for line in f:

            #print(line)
            lineCount +=1
    return lineCount

def file_len(fname):
    i= -1
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1




print(numberOfLines(file))
print(file_len(file))
#oppgave b)


def numberFreq(filename):
    freq = {}
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip('\n'))

        numbersMengde = set(lines)

        for x in numbersMengde:
            freq[x] = lines.count(x)

        for key in sorted(freq.keys()):
            print(key,": ", freq[key], sep="")
    return freq


print(numberFreq(file))