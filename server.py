import os
from flask import Flask, request, abort, Response
from sudoku import Sudoku
import json
from sap import xssec
from cfenv import AppEnv

app = Flask(__name__)
env = AppEnv()

port = int(os.environ.get('PORT', 3000))

uaa_service = env.get_service(name='sudoku-generator-uaa').credentials

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

    return Response(json.dumps(return_game), mimetype='application/json')

    #return json.dumps(return_game)

@app.route('/custom', methods=['GET'])
def generator_custom():
    
    if 'authorization' not in request.headers:
        abort(403)
    access_token = request.headers.get('authorization')[7:]
    print(access_token)
    security_context = xssec.create_security_context(access_token, uaa_service)
    isAuthorized = security_context.check_scope('uaa.resource')
    if not isAuthorized:
        isAuthorized = security_context.check_scope('openid')
        if not isAuthorized:
            abort(403)

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