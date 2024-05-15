from flask import jsonify, render_template, request
from application import app
from werkzeug.utils import secure_filename

import random
from itertools import combinations
from collections import defaultdict

table = defaultdict(list)
levels = range(40, 85, 5)
for a,b in combinations(levels, 2):
    table[abs(a-b)].append((a,b))
table[0] = [(a,a) for a in levels]

lettermap = dict(zip(range(3), 'abc'))

@app.route('/get_graph/<reqstr>', methods=['GET', 'POST'])
def get_graph(reqstr):
    """
    reqstr: String with the format g<graph-number>_l<stress-delta>
    """
    graph, level = reqstr.split("_")
    gnum = int(graph.replace('g', ''))
    lnum = int(level.replace('l', ''))

    print(f"Return graph {gnum}")

    selected_pair = random.choice(table[lnum])
    drawing1 = lettermap[random.randint(0,2)]
    drawing2 = lettermap[random.randint(0,2)]
    print(f"Drawing 1 is stress level {selected_pair[0]}{drawing1}.")
    print(f"Drawing 2 is stress level {selected_pair[1]}{drawing2}.")  

    retstr = f"Drawing 1 is stress level {selected_pair[0]}{drawing1}."
    return jsonify(retstr)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='template', data=None)


@app.route('/about')
def about():
    return render_template('about.html', title='template')

