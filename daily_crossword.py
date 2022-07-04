import datetime
from zoneinfo import ZoneInfo
from flask import Markup, url_for, render_template, send_from_directory
from werkzeug.exceptions import NotFound
from route_config import app

#===================================
#=        Daily Crossword          =
#===================================

@app.route('/daily_crossword/today.puz')
def current_crossword():
    d = datetime.datetime.now(ZoneInfo('America/Los_Angeles'))
    f = f'{str(d.year)}-{str(d.month)}-{str(d.day)}.puz'

    try:
        return send_from_directory('crosswords', filename=f)
    except NotFound:
        # Return the default puzzle if there was an error getting today's 
        # puzzle
        return send_from_directory('crosswords', filename='default.puz')

@app.route('/daily_crossword')
def daily_crossword():
    h = Markup(f'''
        <link rel="stylesheet" href="{url_for('static', filename='css/crosswordnexus.css')}">

        <script src="{url_for('static', filename='js/daily_crossword/crosswords.js')}"></script>
        <script src="{url_for('static', filename='js/daily_crossword/puz.min.js')}"></script>
        
        <script src="{url_for('static', filename='js/daily_crossword/jquery.js')}"></script>
        <script src="{url_for('static', filename='js/daily_crossword/zip.js')}"></script>
        <script src="{url_for('static', filename='js/daily_crossword/jspdf.min.js')}"></script>
        
        <style>
            div.crossword {{ position: absolute; left: 0; top: 0; width: 100%; height: 100%; text-align: center; }}
        </style>
    ''')
    p = Markup(f'''
        <div class="bigWrapper">
            <div class="crossword"></div>

            <script>
                (function(){{
                    CrosswordNexus.createCrossword($('div.crossword'), "{url_for('current_crossword')}");
                }})();
            </script>
        </div>
        
        <p class="centered">
            <a href="{url_for('crossword_generator')}" title="My projects">How the puzzles are generated</a>
            &middot;
            <a href = "{url_for('current_crossword')}" title="Archive">Download today's puz file</a>
            &middot;
            <a href = "https://crosswordnexus.com/" title="CrosswordNexus">Player from CrosswordNexus</a>
        </p>
    ''')
    return render_template('customPage.html', title='Daily Crossword', headHtml=h, pageHtml=p, squeeze=False)
