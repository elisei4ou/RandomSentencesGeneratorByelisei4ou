import random
from colorama import Fore


def get_random_word(words):
    return random.choice(words)


when = ['Vchera', 'V momenta', 'Onziden', 'Ne znam koga', 'V 4.20']
names = ['Seiko', 'Deska', 'Miro', 'Tisho', 'Krisa', 'Mariana', 'Achkata', 'Nikola', 'Ganev']
places = ['Delisule', 'silo', 'grada', 'Sofia', 'Frencha', 'kenefa']
verbs = ['hapva', 'igrae', 'cuka', 'gotvi', 'vijda']
nouns = ['kamani', 'mashinki', 'basket', 'kozi', 'krave sirene']
adverbs = ['bavno', 'qvash-qvash', 'mnogo burzo', 'tujno', 'shtastlivo']
details = ['na igrishteto', 'na mashinkite', 'v kafeneto', 'okolo barata', 'u kushti']


while True:
    do_you_want_next = input(Fore.LIGHTGREEN_EX + "Ako iskash random izrechenie napishi: pls brat, ako ne iskash napishi: mn si zle: ")
    if do_you_want_next == "pls brat":
        random_time = get_random_word(when)
        random_name = get_random_word(names)
        random_place = get_random_word(places)
        random_verb = get_random_word(verbs)
        random_noun = get_random_word(nouns)
        random_adverb = get_random_word(adverbs)
        random_detail = get_random_word(details)
        print(Fore.RED + f"{random_time} {random_name} ot {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")
    elif do_you_want_next == "mn si zle":
        print(Fore.LIGHTBLUE_EX + "Em ako shtesh ve")
        break
    else:
        print(Fore.LIGHTRED_EX + "bugna mashinata brat... bral")
        print("are opitai pak")