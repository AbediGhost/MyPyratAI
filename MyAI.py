##############################################################
# The turn function should always return a move to indicate where to go
# The four possibilities are defined here
##############################################################

MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'



##############################################################
# Please put your code here (imports, variables, functions...)
##############################################################

# Import of random module
import random

visited_location=[]
stuck=False
move_dict = {(0,-1):MOVE_DOWN,(0,1):MOVE_UP,(1,0):MOVE_RIGHT,(-1,0):MOVE_LEFT}


# def random_move_without_collision(player_location,maze_map):

	# # Returns a random move_without_collision
	# allowed_moves = []
	# for neighbor in maze_map[player_location]:
		# allowed_moves.append(move_dict[neighbor[0]-player_location[0],neighbor[1]-player_location[1]])
	# return random.choice(allowed_moves)

def random_move(player_location,maze_map):

	# Returns a random move_without_collision
	global visited_location
	visited_location.append(player_location)
	allowed_moves = []
	for neighbor in maze_map[player_location]:
		if neighbor not in visited_location:
			allowed_moves.append(move_dict[neighbor[0]-player_location[0],neighbor[1]-player_location[1]])
	if len(allowed_moves) == 0:
		a=visited_location[-1]
		visited_location.clear()
		return move_dict[a[0]-player_location[0],a[1]-player_location[1]]
		
	return random.choice(allowed_moves)



##############################################################
# The preprocessing function is called at the start of a game
# It can be used to perform intensive computations that can be
# used later to move the player in the maze.
# ------------------------------------------------------------
# maze_map : dict(pair(int, int), dict(pair(int, int), int))
# maze_width : int
# maze_height : int
# player_location : pair(int, int)
# opponent_location : pair(int,int)
# pieces_of_cheese : list(pair(int, int))
# time_allowed : float
##############################################################

def preprocessing (maze_map, maze_width, maze_height, player_location, opponent_location, pieces_of_cheese, time_allowed) :
    
    # Nothing to do here
    pass



##############################################################
# The turn function is called each time the game is waiting
# for the player to make a decision (a move).
# ------------------------------------------------------------
# maze_map : dict(pair(int, int), dict(pair(int, int), int))
# maze_width : int
# maze_height : int
# player_location : pair(int, int)
# opponent_location : pair(int,int)
# player_score : float
# opponent_score : float
# pieces_of_cheese : list(pair(int, int))
# time_allowed : float
##############################################################

def turn (maze_map, maze_width, maze_height, player_location, opponent_location, player_score, opponent_score, pieces_of_cheese, time_allowed) :
    return random_move(player_location,maze_map)