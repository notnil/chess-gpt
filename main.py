import os
import chess
import chess.pgn
import openai

def get_legal_moves(board):
    """Returns a list of legal moves in UCI notation."""
    return list(map(board.san, board.legal_moves))

def init_game() -> tuple[chess.pgn.Game, chess.Board]:
    """Initializes a new game."""
    board = chess.Board()
    game = chess.pgn.Game()
    game.headers["White"] = "User"
    game.headers["Black"] = "ChatGPT"
    del game.headers["Event"]
    del game.headers["Date"]
    del game.headers["Site"]
    del game.headers["Round"]
    game.setup(board)
    return game, board

def generate_prompt(game: chess.pgn.Game, board: chess.Board) -> str:
    """Generates a prompt for OpenAI."""
    moves = get_legal_moves(board)
    moves_str = ",".join(moves)
    return f"""You are a chess engine playing a chess match against the user as black and trying to win.  The current PGN is:
    {str(game)}

    The current FEN notation is:
    {board.fen()}

    The valid moves are:
    {moves_str}

    Pick a move from the list above that maximizes your chance of winning and provide an explanation of why you picked in the following example format.  Even if you think you can't win still pick a valid move using the following format:

    Move: e5
    Explanation: 1...e5, the Open Game (or Double King's Pawn Game), is Black's classical response to 1. e4. By mirroring White's move, Black grabs an equal share of the centre and scope to develop some pieces. 1...e5 is one of the few moves that directly interferes with White's ideal plan of playing d4."""

def get_move_from_prompt(prompt: str) -> tuple[str,str]:
    """Returns the move from the prompt."""
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    content = response['choices'][0]['message']['content']
    lines = content.splitlines()
    mv, explanation = None, None
    for line in lines:
        if line.startswith("Move:"):
          mv = line[6:]
        if line.startswith("Explanation:"):
          explanation = line[14:]         
    return mv, explanation

game, board = init_game()
game_cp, _ = init_game()
node = game
node_copy = game_cp
while not board.is_game_over():
  if board.turn == chess.WHITE:
      print(board)
      print(game)
      print(board.fen())
      print(get_legal_moves(board))
      move = input("Enter your move: ")
      try:
        board.push_san(move)
      except ValueError:
        print("Invalid move")
        continue
      node = node.add_variation(board.move_stack[-1])
      node_copy = node_copy.add_variation(board.move_stack[-1])
  else:
    prompt = generate_prompt(game, board)
    move, explaination = get_move_from_prompt(prompt)
    board.push_san(move)
    node = node.add_variation(board.move_stack[-1])
    node_copy = node_copy.add_variation(board.move_stack[-1])
    node_copy.comment = explaination
    print(f"ChatGPT played {move} because {explaination}")
  print(game_cp, file=open("out.pgn", "w"), end="\n\n")