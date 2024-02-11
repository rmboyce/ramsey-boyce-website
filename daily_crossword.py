import datetime
from zoneinfo import ZoneInfo

from flask import Blueprint, render_template, send_from_directory, url_for
from markupsafe import Markup
from werkzeug.exceptions import NotFound

#===================================
#=        Daily Crossword          =
#===================================

daily_crossword_pages = Blueprint('daily_crossword_pages', __name__, template_folder='templates')

@daily_crossword_pages.route('/today.puz')
def current_crossword():
    DATE = datetime.datetime.now(ZoneInfo('America/Los_Angeles'))
    FILE = f'{str(DATE.year)}-{str(DATE.month)}-{str(DATE.day)}.puz'
    try:
        return send_from_directory('crosswords', FILE)
    except NotFound:
        # Return the default puzzle if there was an error getting today's puzzle
        return send_from_directory('crosswords', 'default.puz')

@daily_crossword_pages.route('/')
def daily_crossword():
    HEAD = Markup(f'''
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
    return render_template('custom_page.html', title='Daily Crossword', head_html=HEAD, page_content='pages/daily_crossword.html', squeeze=False)
