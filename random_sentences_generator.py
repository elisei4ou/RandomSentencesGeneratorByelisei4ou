import random


def get_random_word(words):
    return random.choice(words)


names = ['Seiko', 'Deska', 'Miro', 'Tisho', 'Krisa', 'Mariana', 'Achkata', 'Nikola', 'Ganev']
places = ['Delisule', 'silo', 'grada', 'Sofia', 'Frencha', 'kenefa']
verbs = ['hapva', 'igrae', 'cuka', 'gotvi', 'vijda']
nouns = ['kamani', 'mashinki', 'basket', 'kozi', 'krave sirene']
adverbs = ['bavno', 'qvash-qvash', 'mnogo burzo', 'tujno', 'shtastlivo']
details = ['na igrishteto', 'na mashinkite', 'v kafeneto', 'okolo barata', 'u kushti']


while True:
    do_you_want_next = input("Ako iskash random izrechenie napishi: pls brat, ako ne iskash napishi: mn si zle: ")
    if do_you_want_next == "pls brat":
        random_name = get_random_word(names)
        random_place = get_random_word(places)
        random_verb = get_random_word(verbs)
        random_noun = get_random_word(nouns)
        random_adverb = get_random_word(adverbs)
        random_detail = get_random_word(details)
        print(f"{random_name} ot {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")
    elif do_you_want_next == "mn si zle":
        print("Em ako shtesh ve")
        break
    else:
        print("bugna mashinata brat... bral")
        print("are opitai pak")




