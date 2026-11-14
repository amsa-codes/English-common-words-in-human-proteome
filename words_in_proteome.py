def read_words(filename):
    with open(filename,"r") as f:
        L=[]
        for line in f:
            if len(line)>=3:
                L.append(line.strip().upper())

    return L