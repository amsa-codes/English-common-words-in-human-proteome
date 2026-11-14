def read_words(filename):
    with open(filename,"r") as f:
        L=[]
        for line in f:
            if len(line.strip())>=3:
                L.append(line.strip().upper())

    return L

def read_sequences(filename):
    sequences={}
    with open(filename, "r") as f:
        for line in f:
            if (line.startswith(">")):
                x=line.split('|')[1]
                sequences[x]=""
            else:
                sequences[x]=sequences[x]+line.strip()
    return sequences

def search_words_in_proteome(words, proteomes):
    d={}
    for word in words:
        c=0
        for proteome, sequence in proteomes.items():
            if word in sequence:
                c+=1
        d[word]=c
        print(word," found in ",c," sequences")
    return d