import csv
import sys
import re



def parse(cards):
    cardlist = []
    for c in cards:
        #print(c)
        card = []
        subcard = []
        i = 1
        if "英語名" in c[0]:
            i = 0
        card.append(c[i].strip("英語名："))
        i += 1
        card.append(c[i].strip("日本語名："))
        i += 1
        if "コスト" in c[i]:
            card.append("'"+c[i].strip("コスト："))
            i += 1
        else:
            card.append("")
        n,typestr = c[i].split("：")
        #print(typestr)
        if "---" in typestr:
            
            t,k = typestr.split('---')
                        
            card.append(t.strip(' '))
            card.append(k.strip(' '))
        else:
            card.append(typestr)
            card.append("")
        i += 1
        details = ""
        if "クリーチャー" in typestr:
            while("Ｐ／Ｔ" not in c[i]):
                #print(c[i])
                details += c[i] + " "
                i += 1
            card.append(details)
            card.append("'"+c[i].strip("Ｐ／Ｔ："))
            i += 1
            if "英語名" in c[i]:
                subcard.append(c[i].strip("英語名："))
                i += 1
                subcard.append(c[i].strip("日本語名："))
                i += 1
                if "コスト" in c[i]:
                    subcard.append("'"+c[i].strip("コスト："))
                    i += 1
                n,typestr = c[i].split("：")
                if "---" in typestr:
                    
                    t,k = typestr.split('---')
                                
                    subcard.append(t.strip())
                    subcard.append(k.strip())
                else:
                    subcard.append(typestr)
                    subcard.append("")
                i += 1
                if "クリーチャー" in typestr:
                    while("Ｐ／Ｔ" not in c[i]):
                        #print(c[i])
                        details += c[i] + " "
                        i += 1
                    subcard.append(details)
                    subcard.append("'"+c[i].strip("Ｐ／Ｔ："))
                    
                else:
                    while("イラスト" not in c[i]):
                        details += c[i] + " "
                        i += 1
                    subcard.append(details)
                    subcard.append("")
        else:
            while("イラスト" not in c[i]):
                details += c[i] + " "
                i += 1
            card.append(details)
            card.append("")
            i += 1
            if "英語名" in c[i]:
                subcard.append(c[i].strip("英語名："))
                i += 1
                subcard.append(c[i].strip("日本語名："))
                i += 1
                if "コスト" in c[i]:
                    subcard.append("'"+c[i].strip("コスト："))
                    i += 1
                n,typestr = c[i].split("：")
                if "---" in typestr:
                    
                    t,k = typestr.split('---')
                                
                    subcard.append(t.strip())
                    subcard.append(k.strip())
                else:
                    subcard.append(typestr)
                    subcard.append("")
                i += 1
                if "クリーチャー" in typestr:
                    while("Ｐ／Ｔ" not in c[i]):
                        #print(c[i])
                        details += c[i] + " "
                        i += 1
                    subcard.append(details)
                    subcard.append("'"+c[i].strip("Ｐ／Ｔ："))
                    
                else:
                    while("イラスト" not in c[i]):
                        details += c[i] + " "
                        i += 1
                    subcard.append(details)
                    subcard.append("")
        
        while("セット" not in c[i]):
            i += 1
        card.append(c[i].strip("セット："))
        if len(subcard) > 0:
            subcard.append(c[i].strip("セット："))
        i += 1
        card.append(c[i].strip("稀少度："))
        if len(subcard) > 0:
            subcard.append(c[i].strip("稀少度："))
        
        
        if len(subcard) > 0:
            card[5] = card[5] + "\n" + subcard[0] + " " + subcard[1] + "と同カード"
            subcard[5] = subcard[5] + "\n" + card[0] + " " + card[1] + "と同カード"
            cardlist.append(subcard)
        cardlist.append(card)
        #print(card)
    return cardlist

def read_file(filename):
    cards = []
    lines = []
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
    card = []
    endflag = False
    
    for line in lines:
        if endflag == True and (re.search('^[0-9]+', line) is not None or re.search('英+', line) is not None):
            if len(card) != 0:
                cards.append(card)
            card = []
            endflag = False
        if line == "\n":
            endflag = True
            continue
        line = line.rstrip().lstrip()
        card.append(line)
        
    return cards

if __name__ == "__main__":
    cards = read_file(sys.argv[2])
    cardlist = parse(cards)
    with open(sys.argv[1], 'a', newline='') as f:
        writer = csv.writer(f)
        for card in cardlist:
            writer.writerow(card)
            

