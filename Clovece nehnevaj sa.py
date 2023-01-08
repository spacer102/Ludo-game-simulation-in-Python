import random


def gensachovnica(n):
    domov = []
    pozicie = []
    # vytvor pole so správnym poctom Domcekov podla velkosti n(vzorec)
    for i in range((n-3)*2):
        domov.append('D')
    # vytvor pole so správnym poctom pohybovych policok podla velkosti n(vzorec)
    for i in range((n-3)*4+8):
        pozicie.append('*')
    # vrat vygenerovanu sachovnicu s poziciami pre pohyb panacikov, domcekov pre panaciky a zadanou velkostou (n)
    return [pozicie, domov, n]


# funkcia ktora sa postara o to ze rozmer sachovnice bude korektny
def spravny_format_sach():
    while True:
        rozmer_sachovnice = int(input("Zadaj velkost sachovnice(n*n): "))
        if rozmer_sachovnice > 5 and rozmer_sachovnice % 2:
            break
        print("Nezadal si akceptovatelnu hodnotu! ")
    return rozmer_sachovnice


def tlac_suradnice(cislo, navrat):
    # cislo-cislo ktore chceme zapisat, a navrat je kolko krat sme už stretli 10tku aby sme ju vedeli od cisla odcitat
    # vytlacime suradnice sachovnice tak aby po cisle 9 nasledovala 0, 1, 2, ...
    if cislo - (navrat * 10) == 0:
        navrat += 1

    # vypiseme a vratime spracovane cislo, tak aby bolo v spravnej podobe(t.j. ziadna 15, apod.)
    print(str(cislo - ((navrat - 1) * 10)), end='')
    return navrat


def tlac_sachovnicu(sachovnica):
    # dlzka_trasy pocet '*'
    dlzka_trasy = len(sachovnica[0])

    # zadane n-ko od uzivatela
    n = sachovnica[2]

    # cez vzorec vyratany presny stred sachovnice
    stred = (n - 1) // 2

    # premenna na kontrolu aby po 9tom cisle nasledovala 0, 1, 2,...
    j = 1

    # tlac horizontalne indexy sachovnice a zalom riadok na konci
    print(' ', end=' ')
    for i in range(n):
        j = tlac_suradnice(i, j)
        print(' ', end='')
    j = 1
    print()

    # cyklus pomocou ktoreho vypiseme po riadkoch celu sachovnicu
    for i in range(n):
        # vytlacime suradnice sachovnice tak aby po cisle 9 nasledovala 0, 1, 2, ...(vertikalne)
        j = tlac_suradnice(i, j)
        print(end=' ')

        # vypis hornych troch hviezdiciek
        if i == 0:
            # vypis medzier tak aby pred strednym prvkom ostalo este 1 miesto pre vypis hviezdicky
            print('  ' * (stred - 1), end='')

            # vypis 3 hviezdicok na vrchu sachovnice. napr. pre n=9 sa tu zlava-doprava vypisu:
            # sachovnica[0][29], sachovnica[0][30], sachovnica[0][31]
            for x in range(-3, 0, 1):
                print(sachovnica[0][dlzka_trasy + x], end=' ')

            # prechod na novy riadok
            print()

        # vypis riadkov ktore su pred poslednym strednym a nie su prve i==0
        elif 0 < i < (stred - 1):
            # spravny pocet medzier podla premenna stred
            print('  ' * (stred - 1), end='')

            # napr. pre n=9 to vypise 28-prvok sachovnica[0][28], potom prvy domcek v poli sachovnica[1]
            # a nakoniec 1-prvok sprava sachovnice[0][0], po kazdom prechode touto podmienkou sa vypisu
            # hodnoty v poliach o 1na vacsiu
            print(sachovnica[0][dlzka_trasy - i - 3], end=' ')
            print(sachovnica[1][i - 1], end=' ')
            print(sachovnica[0][i - 1], end=' ')

            # prechod na novy riadok
            print()

        # posledny riadok pred stredom
        elif i == (stred - 1):
            # pomocu specialneho vzorca vypiseme spravny pocet hviezdiciek so spravnymi indexmi
            for x in range(stred - 1):
                print(sachovnica[0][dlzka_trasy - i - stred + x - 2], end=' ')

            # vypis predposledneho prvku pred domceku pred stredom
            print(sachovnica[0][dlzka_trasy - i - 3], end=' ')

            # vypis domceku
            print(sachovnica[1][i - 1], end=' ')

            # vypis '*' s opacnej strany
            for x in range(stred):
                print(sachovnica[0][i + x - 1], end=' ')
            print()

        # stredne policko
        elif i == stred:
            # vypis '*' podla indexu
            print(sachovnica[0][dlzka_trasy - i - stred - 2], end=' ')

            # vypis domcekov ktore nevyuzijeme pretoze mame len 2 hracov zlava
            for x in range(stred - 1):
                print(sachovnica[1][i + x - 1], end=' ')

            # stredne X-ko
            print('X', end=' ')

            # vypis domcekov ktore nevyuzijeme pretoze mame len 2 hracov sprava
            for x in range(stred - 1):
                print(sachovnica[1][i + stred + x - 2], end=' ')

            # posledna hviezdicka
            print(sachovnica[0][i + stred - 2], end=' ')
            print()

        # policko ktore je hned po strednom
        elif i == (stred + 1):
            # vypis '*' zlava
            for x in range(stred):
                print(sachovnica[0][dlzka_trasy - i - stred - x - 2], end=' ')

            # stredny domcek
            print(sachovnica[1][i + (2 * stred) - 4], end=' ')

            # vypis '*' sprava
            for x in range(stred):
                print(sachovnica[0][i + (2 * stred) - x - 3], end=' ')

            # novy riadok
            print()

        # to iste ako elif 0 < i < (stred - 1) len zo spodu zo spravnymi indexmi
        elif stred < i < (n - 1):
            print('  ' * (stred - 1), end='')
            print(sachovnica[0][dlzka_trasy - i - (2 * stred) - 1], end=' ')
            print(sachovnica[1][i + (2 * stred) - 4], end=' ')
            print(sachovnica[0][i + (2 * stred) - 3])

        # vypis poslednych 3 '*' zdola so spravnym indexom + zalomenie riadka
        else:
            print('  ' * (stred - 1), end='')
            for x in range(3):
                print(sachovnica[0][dlzka_trasy - i - (2 * stred) - x - 1], end=' ')
            print()
    print()


def nacitaj_hraca(farba_panacika, velkost_sachovnice):
    panaciky = []
    # vytvorime hracovi panacik s farbou napr. 'A' na 1-index, potom miesto suradnic, cize None pretoze
    # este nie je v sachovnici
    # a dame hracovi pocet panacikov podla vzorca (n-3)/2
    for i in range((velkost_sachovnice - 3) // 2):
        panaciky.append([farba_panacika, None, 0])
    return panaciky


def pohyb_hraca(hrac, kolky_panacik, ktore_domceky, pocet_krokov, sachovnica):
    # pozicia vlozime aktualnu polohu panacika
    pozicia = hrac[kolky_panacik][1]

    # do posunu vlozime o kolko krokov sa celkovo ma posunut
    posun = hrac[kolky_panacik][2] + pocet_krokov

    # do max_posun urcime kolko krokov moze spravit kym sa vrati do domceka
    max_posun = len(sachovnica[0])-2

    # do posun_domcekov vlozime na ktoru skupinu domcekov sa ma zamerat pri pripadnom vlozeni do domceka
    posun_domcekov = ktore_domceky * (len(sachovnica[1]) // 4) - 1

    # sem bude po nasledujucej podmienke vlozeny spravny index na miesto v sachovnici
    novy_index = pozicia + pocet_krokov

    # kontrola ak sa panacik napr. posunie z 29 prvku o 6 miest tak to bude 3 od zaciatku
    if novy_index > len(sachovnica[0])-1:
        novy_index -= len(sachovnica[0])

    # ak sa panacik posunie na miesto v sachovnici ktore este nie je jeho domcekom
    # tak uchovaj jeho index, zapis ho so sachovnice, zmaz staru poziciu a pripocitaj k celkovemu poctu krokov
    if posun <= max_posun and sachovnica[0][novy_index] == '*':
        sachovnica[0][pozicia] = '*'
        sachovnica[0][novy_index] = hrac[kolky_panacik][0]
        hrac[kolky_panacik][1] = novy_index
        hrac[kolky_panacik][2] += pocet_krokov

    # ak sa panacik posunie na miesto v sachovnici ktore je jeho domcekom
    # tak daj ho do domceka uloz jeho miesto v sachovnici a vrat True, co znamena ze panacik dosiel do domceka
    elif posun > max_posun and posun - max_posun <= len(hrac) and sachovnica[1][kolky_panacik + posun_domcekov + 1] == 'D':
        sachovnica[0][pozicia] = '*'
        sachovnica[1][kolky_panacik + posun_domcekov + 1] = hrac[kolky_panacik][0]
        hrac[kolky_panacik][1] = kolky_panacik + posun_domcekov + 1
        return True

    # vrat False ak panacik nedosiel do domceka
    return False


# tato funkcia vlozi panacika do sachovnice cez funkciu panacik_mimo_sachovnice
def vloz_hraca_do_sachovnice(hrac, ktory_hrac, startovaci_index, sachovnica):
    hrac[ktory_hrac][1] = startovaci_index
    sachovnica[0][startovaci_index] = hrac[ktory_hrac][0]


# tato funkcia kontroluje panacika ci je mimo sachovnice alebo nie, a ak nie da ho na spravny index a vytlaci sachovnicu
def panacik_mimo_sachovnice(hrac, sucasny, start, sachovnica):
    # kontrola ci ma panacik zapisany v sebe uz nejaku poziciu, alebo este nebol pouzity
    if hrac[sucasny][1] is None:
        vloz_hraca_do_sachovnice(hrac, sucasny, start, sachovnica)
        print("Vlozenie {}.panacika hraca {} do sachovnice: ".format(sucasny+1, hrac[sucasny][0]))
        tlac_sachovnicu(sachovnica)


def tah_panacika(hrac, sucasny, domceky, sachovnica):
    # nekonecny cyklus pre hraca kym nepadne kockou nieco ine nez 6(lebo vtedy ide znovu dalsi tah)
    while True:
        # Hod kockou
        hod = random.randint(1, 6)
        print("hod kockou pre {} je: {}".format(hrac[sucasny][0], hod))

        # kontrola ci nahodou panacik nedosiel do domceku
        if pohyb_hraca(hrac, sucasny, domceky, hod, sachovnica):
            sucasny += 1
            tlac_sachovnicu(sachovnica)
            break
        tlac_sachovnicu(sachovnica)
        if hod != 6:
            break
    return sucasny


# vytvorime sachovnicu a vytlacime ju
sach = gensachovnica(spravny_format_sach())
tlac_sachovnicu(sach)

# nacitame hracov
hrac_A = nacitaj_hraca('A', sach[2])
hrac_B = nacitaj_hraca('B', sach[2])

# startovne indexy hracov
start_A = 0
start_B = ((len(sach[0]) - 2) // 2) + 1

# ktorym panacikom sucasne hybeme
sucasny_A = 0
sucasny_B = 0

# ktoru skupinu domcekov vyuzivame
domceky_A = 0
domceky_B = 3

# ktory hrac da do domcekov vsetkych panacikov skor ako protivnik vyhrava
while sucasny_A < len(hrac_A) and sucasny_B < len(hrac_B):

    # kontrola ci sucasny panacikov uz su v sachovnic alebo nie
    # ak nie su funkcia ich tam vlozi a vykresli sachovnicu
    panacik_mimo_sachovnice(hrac_A, sucasny_A, start_A, sach)
    panacik_mimo_sachovnice(hrac_B, sucasny_B, start_B, sach)

    # Tahy panacikov prico si ukladame ich aktualne pouzivane panaciky
    # ak uz 1 dojde pocas funkcie do domceka prejdeme hned na dalsieho panacika
    sucasny_A = tah_panacika(hrac_A, sucasny_A, domceky_A, sach)
    sucasny_B = tah_panacika(hrac_B, sucasny_B, domceky_B, sach)

# vypis vitaza
if sucasny_B > sucasny_A:
    print("Vyhral hrac B")
else:
    print("Vyhral hrac A")
input("Stlac lubovolnu klavesu pre pokracovanie...")
