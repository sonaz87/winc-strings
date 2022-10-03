# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = scorer_0 + ' ' + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)
report = f"{scorer_0} scored in the {str(goal_0)}nd minute\n{scorer_1} scored in the {str(goal_1)}th minute"

player = "Erwin Koeman"
first_name = player[:player.find(" ")]
last_name_len = len(player[player.find(" ")+1:])
name_short = first_name[0] + "." + player[player.find(" "):]

chant_list = [(first_name + "!") for char in first_name]
chant = " ".join(chant_list)
good_chant = chant[-1] != " "