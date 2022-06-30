letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# -----------

print("Question 1:\n")

letter_to_points = {key:value for key, value in zip(letters, points)}

print("letter_to_points =", letter_to_points, "\n")

# -----------

print("Question 2:\n")

print("Adding a blank to the points card...")
letter_to_points[" "] = 0

print("letter_to_points =", letter_to_points, "\n")

# -----------

print("Question 3-6:\n")
print("Creating the score_word() function...\n")

def score_word(word):
  point_total = 0 
  for letter in word:
    if letter not in letter_to_points:
      point_total += 0
    else:
      point_total += letter_to_points[letter]
  return point_total

# -----------

print("Question 7-8:\n")

brownie_points = score_word("BROWNIE")
print("brownie_points =", brownie_points, "\n")

# -----------

print("Question 9 -10:\n")

player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

print("player_to_words =", player_to_words, "\n")

player_to_points = {}

print("player_to_points =", player_to_points, "\n")

# -----------

print("Question 11 - 14:\n")
print("Calculating the player's score...\n")

for player in player_to_words:
  #print("player =", player)
  player_points = 0
  for word in player_to_words[player]:
    #print("word =", word)
    player_points += score_word(word)
  player_to_points[player] = player_points

print("player_to_points = ", player_to_points, "\n")

# -----------

print("Bonus Questions:\n")

print("Task #1 \nplay_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played\n")

def play_word(player, word):
  if player not in player_to_words:
    player_to_words[player] = [word]
    print("A new player has entered!")
    print(player, "played the word", word, "\n")
  else:
    player_to_words[player].append(word)
    print(player, "played the word", word, "\n")

play_word('player1', "MEMES")
play_word("daniel", "SPEEDY")

#print(player_to_words)

print("Task #2 \nupdate_point_totals() — turn your nested loops into a function that you can call any time a word is played\n")

print("Task #3 \nmake your letter_to_points dictionary able to handle lowercase inputs as well")















