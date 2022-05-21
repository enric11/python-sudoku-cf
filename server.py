import os
from flask import Flask, request
from sudoku import Sudoku
import json

app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))

@app.route('/')
#Default generation
def generator():
    puzzle = Sudoku(3).difficulty(0.5)
    solution = puzzle.solve()

    return_game = {
        "difficulty" : puzzle._Sudoku__difficulty,
        "board" : puzzle.board,
        "with" : puzzle.width,
        "height" : puzzle.height,
        "boardSolution" : solution.board
    }
    return json.dumps(return_game)

@app.route('/custom', methods=['GET'])
def generator_custom():
    
    puzzle = Sudoku(int(request.args.get("size"))).difficulty(float(request.args.get("dificulty")))
    solution = puzzle.solve()

    return_game = {
        "difficulty" : puzzle._Sudoku__difficulty,
        "board" : puzzle.board,
        "with" : puzzle.width,
        "height" : puzzle.height,
        "boardSolution" : solution.board
    }
    return json.dumps(return_game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)