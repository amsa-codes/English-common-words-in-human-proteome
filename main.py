import words_in_proteome

W= words_in_proteome.read_words("english-common-words.txt")
print(len(W))
P=words_in_proteome.read_sequences("human-proteome.fasta")
print(len(P))
print(P["O95139"])
D= words_in_proteome.search_words_in_proteome(W,P)
m=find_most_frequent_word(D)
print("le pourcentage des sequences du proteome contenant ce mot est : ", m/len(P)*100)