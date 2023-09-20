def divi2(cookies, kids):
  result = {}
  for kid in kids:
    result[kid] = []
  print(result)
  while True:
    if len(cookies) < len(kids):
      return result, cookies
    for kid in kids:
      result[kid].append(cookies.pop())


def ttt_player(symbol, game, pos):
  game[pos] = symbol
  return player_won(symbol)


def player_won(symbol, game):
  for line in winning_lines:
    result = True
    for k in line:
      if game[k] != symbol:
        result = False
    if result:
      return True
  return False


winning_rows = [
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
]

winning_cols = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
]

winning_diags = [
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

winning_lines = (winning_rows + winning_cols + winning_diags)


def init_game():
  game = {}
  for row in range(3):
    for col in range(3):
      game[(row, col)] = ""
  return game