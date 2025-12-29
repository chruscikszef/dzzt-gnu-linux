#!/usr/bin/env python3

#
# Skrypt naprawiający Linuxową wersję wybitnego dzieła pt. "Dzień z Życia Teklaga"
# Niestety autor nie zadbał o testy i ewentualne bugfixy na GNU/Linuxie, więc musiało zrobić to jakże wielkie community tej wybitnej gry
# Stworzone przez Chruścika (https://github.com/chruscikszef)
# Dystrybuowane na licencji GNU General Public License v3 
#

import os
import math
from pathlib import Path

gameroot = os.getcwd()

def sed(sedArg, file):
	os.system(f"sed -i {sedArg} {os.path.join(gameroot, "www/data", file)}")

def link(dest, name):
	os.system(f"ln -sfv {dest} {name}")

def sedJson():
	print("Patchowanie plików JSON...")
	jsonPath = os.path.join(gameroot, "www/data")
	jsonFiles = [f.name for f in Path(jsonPath).glob("*.json")] 
	fCount = len(jsonFiles)
	#print(jsonPath, "\n", jsonFiles, "\n", fCount)

	percent = 100 / fCount
	fC = 1
	for f in jsonFiles:
		cP = percent * fC
		print(f"{math.trunc(cP * 10) / 10} % --> {f}")
		sed('"s/Obudź się/Obudz sie/g"', f)
		sed('"s/Nie dziś/Nie dzis/g"', f)
		sed('"s/Zaćmienie/Zacmienie/g"', f)
		sed('"s/Złe wieści/Zle wiesci/g"', f)
		sed('"s/Zapomniałem jak nazywa się ten utwór/Zapomnialem jak nazywa sie ten utwor/g"', f)
		sed('"s/Sąsiedzi (Slowed Down)/Sasiedzi (Slowed Down)/g"', f)
	
		fC = fC + 1

def printPerc(oP, cP):
	print(f"{math.trunc(oP * cP * 10)} %")

def linkOgg():
	print("Linkowanie plików Ogg...")
	os.chdir(os.path.join(gameroot, "www/audio/bgm"))

	perc = 100 / 70

	printPerc(perc, 1)
	link("'Teklag - Nie dziШ.ogg'", "'Teklag - Nie dzis.ogg'")
	printPerc(perc, 2)
	link("'Teklag - Obudл siй.ogg'", "'Teklag - Obudz sie.ogg'")
	printPerc(perc, 3)
	link("'Teklag - ZaЖmienie.ogg'", "'Teklag - Zacmienie.ogg'")
	printPerc(perc, 4)
	link("'Teklag - ZaЖmienie (Reprise).ogg'", "'Teklag - Zacmienie (Reprise).ogg'")
	printPerc(perc, 5)
	link("'Teklag - ZapomniaИem jak nazywa siй ten utwвr.ogg'", "'Teklag - Zapomnialem jak nazywa sie ten utwor.ogg'")
	printPerc(perc, 6)
	link("'Teklag - ZИe wieШci.ogg'", "'Teklag - Zle wiesci.ogg'")
	printPerc(perc, 7)
	link("'Sеsiedzi (Slowed Down).ogg'", "'Sasiedzi (Slowed Down).ogg'")

def clearExecstack():
	print("Czyszczenie execstacku...")
	os.system(f"patchelf --clear-execstack {os.path.join(gameroot, "lib/libnode.so")}")

def main():
	sedJson()
	linkOgg()
	clearExecstack()

if __name__ == "__main__":
	main()

#'Teklag - Nie dziШ.ogg' 'Teklag - Obudл siй.ogg' 'Teklag - ZaЖmienie.ogg' 'Teklag - ZaЖmienie (Reprise).ogg' 'Teklag - ZapomniaИem jak nazywa siй ten utwвr.ogg' 'Teklag - ZИe wieШci.ogg'
#Sеsiedzi (Slowed Down).ogg
