# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#spelers die gescoord hebben
player1 = "Ruud Gullit"
player2 = "Marco van Basten"

#wanneer is welke goal gescoord in min
goal_0 = 32
goal_1 = 54

#met de + operator
scorers = player1 + " " + str(goal_0) + ", " +  player2 + " " + str(goal_1)

#met de f-string
report = f"{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute"

player = "Marco van Basten"

first_name = (player[:player.find(" ")]) #find functie zoekt de eerste spatie op alles voor de spatie word gesliced

last_name_len = len(player[player.find(" ")+1:]) #zoekt de eerste spatie op alle daarna is de achternaam

#player(0) pakt de eerste letter van de naam, vervolgens zoeken we weer de eerste spatie op en slicen we alles na de spatie. En voegen we dit toe.
name_short = f"{player[0]}.{player[player.find(' '):]}"

#we pakken weer de eerste naam en printen dit keer de lengte van het aantal letters van de naam

chant_gehele_tekst = f"{first_name}! " * (len(player[:player.find(" ")]) )

chant = chant_gehele_tekst
chant = (chant_gehele_tekst[:-1]) #ik haal de laatste spatie er vanaf, ben er nog niet achter hoe ik dit zonder deze stap kan doen

good_chant = " " != chant[-1]

print(chant)