import words_in_proteome

W= words_in_proteome.read_words("english-common-words.txt")
print(len(W))
P=words_in_proteome.read_sequences("human-proteome.fasta")
print(len(P))
print(P["O95139"])
D= words_in_proteome.search_words_in_proteome(W,P)
m=words_in_proteome.find_most_frequent_word(D)
print("the percentage of proteome sequences containing this word : ", m/len(P)*100)
DO=word_in_proteome.nbr_occurences_in_proteome(W,P)
mo=word_in_proteome.find_most_frequent_word(DO)