# cuvant = 'a _ _ a _ _ t'
# alfabet
word = 'onomatopee'
word_list = []
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())

#print(word_list)
#print(" ".join(word_list))

count_nr = 1
list_already_checked = []
new_word = " ".join(word_list)
while count_nr <= 7:
    user_letter = input('Alege o litera: ').lower()
    if user_letter == '':
        print("Introdu o litera")
        continue
    if user_letter in word_list:
        print("Litera deja afisata pe ecran")
    elif user_letter in list_already_checked:
        print(f"Litera deja a fost incercata, litere deja incercate sunt: {''.join(list_already_checked)}")
    else:
        if user_letter in word:
            for iterator, value in enumerate(word):
                if user_letter == value:
                    word_list[iterator] = value
            print(" ".join(word_list))
        else:
            count_nr += 1

        if '_' not in "".join(word_list):
            print("Ai castigat")
            break
        elif count_nr > 7:
            print(f"Ai pierdut! Cuvantul era {word}")

        list_already_checked.append(user_letter)
