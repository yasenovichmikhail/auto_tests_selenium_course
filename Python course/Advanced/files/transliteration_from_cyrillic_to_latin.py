letters = {
    'а':'a', 'к':'k', 'х': 'h',
'б':'b','л':'l','ц':'c',
'в':'v','м':'m','ч':'ch',
'г':'g','н':'n','ш':'sh',
'д':'d','о':'o','щ':'shh',
'е':'e','п':'p','ъ':'*',
'ё':'jo','р':'r', 'ы':'y',
'ж':'zh','с':'s','ь':"'",
'з':'z','т':'t','э':'je',
'и':'i','у':'u','ю':'ju',
'й':'j','ф':'f','я':'ya'
    }

with open('cyrillic.txt') as file1, open('transliteration.txt', 'w') as file2:
    for i in file1.read():
        if i in letters:
            file2.write(letters[i])
        elif i.lower() in letters:
            file2.write(letters[i.lower()].capitalize())
        else:
            file2.write(i)