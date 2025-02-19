# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=None, play_order=None):
    if opponent_history is None:
        opponent_history = []
    if play_order is None:
        play_order = {}
    
    # Initialize counters for pattern detection
    if not hasattr(player, "play_counter"):
        player.play_counter = 0
    player.play_counter += 1
    
    # Add the previous play to history
    opponent_history.append(prev_play)
    
    # First move strategy
    if prev_play == "":
        return "R"
    
    # Get the last few plays
    last_ten = opponent_history[-10:] if len(opponent_history) > 10 else opponent_history
    
    # Detect Quincy's pattern
    if len(opponent_history) >= 5:
        quincy_pattern = ["R", "R", "P", "P", "S"]
        last_five = opponent_history[-5:]
        if last_five == quincy_pattern:
            next_quincy = quincy_pattern[player.play_counter % 5]
            counter_moves = {"R": "P", "P": "S", "S": "R"}
            return counter_moves[next_quincy]
    
    # Counter Kris's strategy
    if len(last_ten) >= 2:
        if last_ten[-1] == last_ten[-2]:  # If Kris is detected
            ideal_response = {"P": "S", "R": "P", "S": "R"}
            return ideal_response[prev_play]
    
    # Counter Mrugesh's strategy
    if len(last_ten) >= 3:
        most_frequent = max(set(last_ten), key=last_ten.count)
        if last_ten.count(most_frequent) >= 4:  # If Mrugesh is detected
            counter_moves = {"R": "P", "P": "S", "S": "R"}
            return counter_moves[most_frequent]
    
    # Abbey's strategy counter
    if len(opponent_history) >= 2:
        last_two = "".join(opponent_history[-2:])
        if last_two in play_order:
            play_order[last_two] = play_order.get(last_two, 0) + 1
        else:
            play_order[last_two] = 1
        
        potential_plays = [
            prev_play + "R",
            prev_play + "P",
            prev_play + "S",
        ]
        
        max_count = 0
        predicted_play = "R"
        
        for play in potential_plays:
            if play in play_order and play_order[play] > max_count:
                max_count = play_order[play]
                predicted_play = play[-1]
        
        counter_moves = {"R": "P", "P": "S", "S": "R"}
        return counter_moves[predicted_play]
    
    # Default strategy: counter the last move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[prev_play]


# Quincy: Uses a fixed pattern of ["R", "R", "P", "P", "S"]
 # Mrugesh: Plays based on the most frequent move in the last 10 plays
  # Kris: Simply counters the previous play
   # Abbey: Uses a more complex strategy based on patterns of the last two moves