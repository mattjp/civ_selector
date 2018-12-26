import sys
import random

CIVS_VANILLA = [
	("America", "Teddy Roosevelt"),
	("Arabia",  "Saladin"),
	("Aztec",   "Montezuma"),
	("Brazil",  "Pedro II"),
	("China",   "Qin Shi Huang"),
	("Egypt",   "Cleopatra"),
	("England", "Victoria"),
	("France",  "Catherine de Medici"),
	("Germany", "Frederick Barbarossa"),
	("Greece",  "Gorgo"),
	("Greece",  "Pericles"),
	("India",   "Ghandi"),
	("Japan",   "Hojo Tokimune"),
	("Kongo",   "Mvemba a Nzinga"),
	("Norway",  "Harald Hardrada"),
	("Poland",  "Jadwiga"),
	("Rome",    "Trajan"),
	("Russia",  "Peter"),
	("Scythia", "Tomyris"),
	("Spain",   "Phillip II"),
	("Sumeria", "Gilgamesh")
]

CIVS_RISE_FALL = {
	("Cree",        "Poundmaker"),
	("Georgia",     "Tamar"),
	("India",       "Chandragupta"),
	("Korea",       "Seondeok"),
	("Mapuche",     "Lautaro"),
	("Mongolia",    "Ghengis Khan"),
	("Netherlands", "Wilhelmina"),
	("Scotland",    "Robert the Bruce"),
	("Zulu",        "Shaka")
}

CIVS_GATHERING_STORM = {
	("Canada",    "Laurier"),
	("England",   "Eleanor"),
	("France",    "Eleanor"),
	("Hungary",   "Matthias Corvinus"),
	("Inca",      "Pachacuti"),
	("Mali",      "Mansa Musa"),
	("Maori",     "Kupe"),
	("Ottomans",  "Suleimon"),
	("Phoenicia", "Dido"),
	("Sweden",    "Kristina")
}


# Pick 3 random civilization options
def pick_civs(civs):
	all_civs = []
	for civ in civs:
		all_civs += civ
	return random.sample(all_civs, 3)


# Pretty printing
def print_civs(civs):
	i = 1
	for civ in civs:
		print(str(i) + ". " + civ[0] + " - " + civ[1])
		i +=1


# Output civilization options
def main():
	if len(sys.argv) == 1:
		print("Choosing from vanilla civilizations...")
		print_civs(pick_civs([CIVS_VANILLA]))
	elif len(sys.argv) == 2:
		if sys.argv[1] == "-r":
			print("Choosing from vanilla + Rise and Fall civilizations.")
			print_civs(pick_civs([CIVS_VANILLA, CIVS_RISE_FALL]))
		elif sys.argv[1] == "-g":
			print("Choosing from vanilla + Gathering Storm civilizations.")
			print_civs(pick_civs([CIVS_VANILLA, CIVS_GATHERING_STORM]))
		else:
			print("Invalid argument.")
	elif len(sys.argv) == 3:
		if sys.argv[1] == "-r" and sys.argv[2] == "-g":
			print("Choosing from vanilla + all DLC.")
			print_civs(pick_civs([CIVS_VANILLA, CIVS_RISE_FALL, CIVS_GATHERING_STORM]))
		elif sys.argv[1] == "-g" and sys.argv[2] == "-r":
			print("Choosing from vanilla + all DLC.")
			print_civs(pick_civs([CIVS_VANILLA, CIVS_RISE_FALL, CIVS_GATHERING_STORM]))
		else:
			print("Invalid arguments.")
	else:
		print("Too many arguments.")


if __name__ == "__main__":
	main()