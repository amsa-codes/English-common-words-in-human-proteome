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

def find_most_frequent_word(dict):
    m=0
    w=""
    for key, value in dict.items():
        if value>m:
            m=value
            w=key
    print(w+" found in  "+str(m)+" sequences")
    return m

def nbr_occurences_in_proteome(words, proteomes):
    d={}
    for word in words:
        occ=0
        for proteome, sequence in proteomes.items():
            occ=occ+sequence.count(word)
            
        d[word]=occ
        print(word," found in ",occ," times in sequences")
    return d