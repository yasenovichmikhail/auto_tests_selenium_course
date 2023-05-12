
def get_coding_message(letters, morse, text):
    my_dict = dict(zip(letters, morse))
    my_text = text.upper()
    for i in my_text:
        for j in my_dict:
            if i == j:
                print(my_dict[j], end=' ')
                
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
text = 'Interstellar'

get_coding_message(letters, morse, text)