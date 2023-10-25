import pandas
df = pandas.read_csv("nato_phonetic_alphabet/nato_phonetic_alphabet.csv")

data_dic = {row.letter: row.code for (index, row) in df.iterrows()}
print(data_dic)

word = input("write the word: ").upper()
list_of_code = [data_dic[letter] for letter in word]

print(list_of_code)
