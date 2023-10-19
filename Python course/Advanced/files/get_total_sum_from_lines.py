with open('ledger.txt', encoding='utf-8') as file:
    print(f"${sum(int(line[1:].strip())for line in file)}")