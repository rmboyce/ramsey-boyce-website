from flask import Flask, render_template, Markup, url_for
from __main__ import app

@app.route('/daily_crossword')
def daily_crossword():
    h = Markup('''
        <link rel="stylesheet" href="''' + url_for('static', filename='css/crosswordnexus.css') + '''">

        <script src="''' + url_for('static', filename='daily_crossword/crosswords.js') + '''"></script>
        <script src="''' + url_for('static', filename='daily_crossword/puz.min.js') + '''"></script>
        
        <script src="''' + url_for('static', filename='daily_crossword/jquery.js') + '''"></script>
        <script src="''' + url_for('static', filename='daily_crossword/zip.js') + '''"></script>
        <script src="''' + url_for('static', filename='daily_crossword/jspdf.min.js') + '''"></script>
        
        <style>
            div.crossword { position: absolute; left: 0; top: 0; width: 100%; height: 100%; text-align: center; }
        </style>
    ''')
    p = Markup('''
        <div class="bigWrapper">
            <div class="crossword"></div>

            <script>
                (function(){
                    CrosswordNexus.createCrossword($('div.crossword'));
                })();
            </script>
        </div>
        
        <p class="centered">
            <a href="''' + url_for('serpent_fusion') + '''" title="My projects">How the puzzles are generated</a>
            &middot;
            <a href = "''' + url_for('serpent_fusion') + '''" title="Archive">Puzzle archive</a>
        </p>
    ''')
    return render_template('customPage.html', title='Daily Crossword', headHtml=h, pageHtml=p, squeeze=False)