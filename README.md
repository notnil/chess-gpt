# chess-gpt

Welcome to Chess-GPT! This is a not-so-powerful chess bot that utilizes OpenAI's GPT-3.5-turbo API to provide you with an interesting chess playing experience. Watch it generate extremely confident explanations for moves while it blunders like a sub 500 ELO noob!

# Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Prompt](#prompt)
4. [Example Game](#example-game)

# Installation 

To run Chess-GPT, please follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chess-gpt.git
cd chess-gpt
```

2. Setup the environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Add your OpenAI API key:
Create a .env file in the root directory and add the following line:
```bash
OPENAI_API_KEY=your_api_key_here
```

# Usage

To start the Chess-GPT bot, run the following command:

```bash
dotenv run python main.py
```

This will start a command-line interface where you can interact with the Chess-GPT bot.  The player is always white and Chess-GPT is always black.   

# Prompt

Only a few iterations were required to create a prompt that would reliably make ChatGPT play chess. The most important realization was that I could give ChatGPT a list of moves and instruct it to choose one regardless of the situation. This ensured that any move it made would be valid. Additionally, ChatGPT needed both the PGN (game history) and FEN (current board state) for context to pick non-random moves. The most interesting part of the prompt was the required addition of the phrase, "Even if you think you can't win, still pick a valid move," or ChatGPT would effectively give up. ChatGPT apparently interpreted the prompt very pessimistically and didn't see a path to maximizing its winning chances.

Code to Generate:

```python
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

```

Example Output:
```
You are a chess engine playing a chess match against the user as black and trying to win.  The current PGN is:
    [White "User"]
[Black "ChatGPT"]
[Result "*"]

1. e4 *

The current FEN notation is:
rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1

The valid moves are:
Nh6,Nf6,Nc6,Na6,h6,g6,f6,e6,d6,c6,b6,a6,h5,g5,f5,e5,d5,c5,b5,a5

Pick a move from the list above that maximizes your chance of winning and provide an explanation of why you picked in the following example format.  Even if you think you can't win still pick a valid move using the following format:

Move: e5
Explanation: 1...e5, the Open Game (or Double King's Pawn Game), is Black's classical response to 1. e4. By mirroring White's move, Black grabs an equal share of the centre and scope to develop some pieces. 1...e5 is one of the few moves that directly interferes with White's ideal plan of playing d4.
```

Example Output:
```
Move: Nf6
Explanation: 1...Nf6 is a solid move that develops a knight to a good square, controls e4, and prepares castle kingside. It puts pressure on White's pawn on e4 and forces White to make a decision on how to defend it. Additionally, it supports the move d5 in the future, which can help Black to gain a foothold in the center.
ChatGPT played Nf6 because ...Nf6 is a solid move that develops a knight to a good square, controls e4, and prepares castle kingside. It puts pressure on White's pawn on e4 and forces White to make a decision on how to defend it. Additionally, it supports the move d5 in the future, which can help Black to gain a foothold in the center.
```


# Example Game

Lichess Game Link: https://lichess.org/6aGY4ULm
Lichess Study Link: https://lichess.org/study/WU0i6otP
![Chess Game](https://lichess1.org/game/export/gif/white/6aGY4ULm.gif?theme=brown&piece=cburnett)


|Move number|White move                   |Black move|Explanation                                  |
|-----------|-----------------------------|----------|---------------------------------------------|
|1          |e4                           |d6        |y playing d6, Black creates a solid pawn structure and prepares to develop the bishop to either d7 or e6. This move also indirectly attacks White's e4 pawn, making it more difficult for White to defend it in the long term. Additionally, it controls the square e5, making it harder for White to advance their pawn there and gain more space in the center of the board. |
|2          |d4                           |Nf6       |...Nf6 develops a piece and attacks White's e4 pawn, creating an immediate threat. It also supports the idea of playing d5 to control the center, which can be a strong counter to White's opening. Additionally, by developing the knight to f6, it prevents White from playing g5 to push the knight away, which could be problematic for Black's pawn structure. |
|3          |Nc3                          |Nbd7      |bd7 develops the knight and prepares to challenge White's control of the center with moves like c5 or e6. It also keeps an eye on the e5 square, potentially putting pressure on White's pawn. Additionally, it avoids doubling the pawns after 4.Nxd4 e5. Overall, Nbd7 is a solid move that maintains Black's chances of equalizing the game. |
|4          |Nf3                          |Nd5       |...Nd5 attacks the pawn on c3, which can cause some problems for White as they need to figure out how to defend it. Additionally, the knight on d5 may put pressure on White's position and provide potential for future tactics. This move also fits into Black's general plan in this opening, which is to play for control of the center and develop their pieces harmoniously. |
|5          |exd5                         |Ne5       |...Ne5 attacks the pawn on d4 and forces White to make a decision. If White chooses to defend the pawn with c3, then Black can follow up with Nxf3+ followed by Qg5, creating pressure on the weakened kingside. If White chooses to capture on e5 with fxe5, then Black can recapture with dxe5, opening up the d-file and creating pressure on White's central pawn structure. Overall, 5...Ne5 puts pressure on White and opens up possibilities for counterplay. |
|6          |dxe5                         |dxe5      |choose 6...dxe5 since it gains a pawn and opens up the position. By capturing with the pawn, Black is able to control the central squares and create more space for their pieces. Additionally, this move creates potential for the Black bishop on c8 to be developed to b7 or a6 in the future. Overall, it puts pressure on White and gives Black a small advantage in the game. |
|7          |Nxe5                         |Qd6       |d6 pins the knight on e5, which is White's most centralized piece at the moment. This move defends the pawn on d6 and prepares for possible maneuvers such as Nd7, Bd7, or even f6 to strengthen the e5 pawn. Additionally, the queen on d6 adds pressure on the long diagonal which could lead to tactical opportunities. This move helps to maintain Black's position and create potential chances to counterattack. |
|8          |Nf3                          |Qd7       |d7 defends the pawn on d6 and prepares for potential pinning of the knight on f6 by White's bishop on c4. It also allows for the possibility of bringing the queen over to the kingside to assist in an attack if White castles kingside. Additionally, Qd7 puts pressure on White's pawn on d4, potentially forcing it to advance and weaken White's pawn structure. |
|9          |Bb5                          |Qc6       |...Qc6 attacks the b5 bishop and threatens to capture it. If White responds with 10.Nd4, Black can follow up with 10...Qxd5, winning material. If White moves the bishop, Black can continue developing with moves like ...Bg4 or ...0-0. Overall, Qc6 puts pressure on White's position and creates potential for Black to gain a material advantage.|
|10         |dxc6                         |Bd7       |d7 is a reasonable move to make. It activates the bishop and helps Black to control the central squares. After Bd7, black can also castle kingside which will solidify the position of the King and establish a good connection between the Rooks. Additionally, since the pawn on c6 can't move it makes sense to move the Black Bishop to a safer position. Before making the move, it's important to anticipate White's response and evaluate the next few moves to respond accordingly.|
|11         |cxd7+                        |Kd8       |The current position is already lost for Black as White has a significant material advantage. All of Black's pieces are either blocked or poorly placed, and there is no way to stop the impending checkmate. Therefore, any move Black makes will only prolong the game without changing the outcome. Choosing Kd8 over other moves like Bd7 or c6 is simply a matter of preference, as all possible moves result in a lost game.|
|12         |Ne5                          |c5        |... c5 hits White's d4 pawn, putting pressure on their central pawn chain. This move also prepares for Black to possibly fianchetto their bishop on the c8-h3 diagonal, allowing them to control more of the board. Additionally, controlling the c4 square could potentially limit the movement of White's knight on c3. Overall, c5 is a strong move that improves Black's position while putting pressure on White.|
|13         |Nxf7+                        |Kc7       |3...Kc7 is the only valid move and it defends the attacked bishop on d7. While Black's position is currently inferior due to the material disadvantage and the exposed king, it's important to minimize any further losses and try to hold on for as long as possible. By playing Kc7, Black also prepares to activate their rook on a8 and potentially put pressure on White's weak b2 pawn.|
|14         |Bf4+                         |Kb6       |...Kb6, moves the king towards safety and out of potential pin tactics by a rook or a bishop that White could set up. It also frees up the c7 pawn and allows for potential counterplay by attacking White's b5 pawn. This move is a defensive one, as Black doesn't have a strong attacking position at the moment, so prioritizing safety is a rational choice.|
|15         |Ba4                          |c4        |This move is a strong response to white's placement of their bishop on b5, preventing any future development of Black's knight on d7. It also allows Black to gain control over the center of the board and put pressure on White's position. This move opens up the possibility for the Black queen and bishop to come into the game, preparing for a potential attack against White's position. Overall, c4 is a solid move that strikes a balance between development and control of the board.|
|16         |Qd4+                         |Ka5       |Moving the king closer to the center of the board is a good idea to better protect the remaining pieces. Also, it avoids the checkmate threat that could arise from Bd7+. However, it is important to note that the position is still very difficult for Black and their chances of winning are very low.|
|17         |Qc5+                         |Ka6       |his move allows Black to safely move their king out of harm's way and potentially put pressure on White's position with the king's presence on the queenside. It also prevents any potential checks from White's bishop on a4. Additionally, the move Ka6 opens up the possibility of Black advancing their pawn on the queenside and potentially creating a passed pawn. As Black is currently down material, it may be advantageous to try and create some counterplay to put pressure on White.|
