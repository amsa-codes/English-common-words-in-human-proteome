import words_in_proteome

W= words_in_proteome.read_words("english-common-words.txt")
print(len(W))
P=words_in_proteome.read_sequences("human-proteome.fasta")
print(len(P))
print(P["O95139"])