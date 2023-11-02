import pandas
df = pandas.read_csv("nato_phonetic_alphabet/nato_phonetic_alphabet.csv")

data_dic = {row.letter: row.code for (index, row) in df.iterrows()}
print(data_dic)

def generate_phonetic():
    word = input("write the word: ").upper()
    try:
        list_of_code = [data_dic[letter] for letter in word]
    except KeyError:
        print("only letters")
        generate_phonetic()
    else:
        print(list_of_code)

generate_phonetic()