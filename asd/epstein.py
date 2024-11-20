from itertools import permutations
import time

def einstein_riddle():
    start_time = time.time()
    # Všetky možné hodnoty atribútov
    farby = ['žltý', 'modrý', 'červený', 'zelený', 'biely']
    narodnosti = ['Nór', 'Dán', 'Brit', 'Nemec', 'Švéd']
    napoje = ['voda', 'čaj', 'mlieko', 'káva', 'pivo']
    cigarety = ['Dunhill', 'Blend', 'Pall Mall', 'Prince', 'Blue Master']
    zvierata = ['mačky', 'kone', 'vtáky', 'ryby', 'psy']

    # Generujeme všetky permutácie pre jednotlivé atribúty
    for f_perm in permutations(farby):
        for n_perm in permutations(narodnosti):
            for d_perm in permutations(napoje):
                for c_perm in permutations(cigarety):
                    for z_perm in permutations(zvierata):
                        # Logické podmienky hádanky
                        if (
                            # Nór býva v prvom dome
                            n_perm[0] == 'Nór'
                            # Zelený dom je naľavo od bieleho
                            and f_perm.index('zelený') == f_perm.index('biely') - 1
                            # Obyvateľ tretieho domu pije mlieko
                            and d_perm[2] == 'mlieko'
                            # Nór býva vedľa modrého domu
                            and f_perm.index('modrý') == 1
                            # Brit býva v červenom dome
                            and n_perm[f_perm.index('červený')] == 'Brit'
                            # Švéd chová psy
                            and z_perm[n_perm.index('Švéd')] == 'psy'
                            # Dán pije čaj
                            and d_perm[n_perm.index('Dán')] == 'čaj'
                            # Zelený dom má obyvateľa, ktorý pije kávu
                            and d_perm[f_perm.index('zelený')] == 'káva'
                            # Ten, kto fajčí Pall Mall, chová vtáky
                            and z_perm[c_perm.index('Pall Mall')] == 'vtáky'
                            # Obyvateľ žltého domu fajčí Dunhill
                            and c_perm[f_perm.index('žltý')] == 'Dunhill'
                            # Ten, kto fajčí Blend, býva vedľa toho, kto chová mačky
                            and abs(c_perm.index('Blend') - z_perm.index('mačky')) == 1
                            # Ten, kto chová kone, býva vedľa toho, kto fajčí Dunhill
                            and abs(z_perm.index('kone') - c_perm.index('Dunhill')) == 1
                            # Ten, kto fajčí Blue Master, pije pivo
                            and d_perm[c_perm.index('Blue Master')] == 'pivo'
                            # Nemec fajčí Prince
                            and c_perm[n_perm.index('Nemec')] == 'Prince'
                            # Ten, kto fajčí Blend, býva vedľa toho, kto pije vodu
                            and abs(c_perm.index('Blend') - d_perm.index('voda')) == 1
                        ):
                            # Nájdeme odpoveď
                            majitel_ryb = n_perm[z_perm.index('ryby')]
                            print(f"Osoba {majitel_ryb} vlastní rybu.")
                            print("--- %s seconds ---" % (time.time() - start_time))
                            return
                        

# Spustíme riešenie
einstein_riddle()
input()
