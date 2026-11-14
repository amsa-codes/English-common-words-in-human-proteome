def read_words(filename):
    with open(filename,"r") as f:
        L=[]
        for line in f:
            if len(line)>=3:
                L.append(line.strip().upper())

    return L
def read_sequences(filename):
    sequences={}
    with open(filename, "r") as f:
        for line in f:
            if (line.startswith(">")):
                sequences[line.split('|')[1]].get()