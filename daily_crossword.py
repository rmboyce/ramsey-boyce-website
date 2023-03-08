import datetime
from zoneinfo import ZoneInfo

from flask import Markup, render_template, send_from_directory, url_for
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
        return send_from_directory('crosswords', f)
    except NotFound:
        # Return the default puzzle if there was an error getting today's
        # puzzle
        return send_from_directory('crosswords', 'default.puz')

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
    return render_template('custom_page.html', title='Daily Crossword', head_html=h, page_content='pages/daily_crossword.html', squeeze=False)
