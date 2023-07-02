import pandas


alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows() }
print(alphabet)


is_true = True
while is_true:
    word = input("Enter a word: ").upper()
    try:
        output_list = [alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        # Print the original word
        print("Original word:", word)
        # Print the list of NATO phonetic alphabet codes
        print("Output list:", output_list)
        is_true = False

