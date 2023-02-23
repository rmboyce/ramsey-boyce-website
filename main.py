from flask import Markup, redirect, render_template, request, url_for

from daily_crossword import *
from javascript_demos import *
from projects import *
from route_config import app


# Force https
def force_https():
    # Redirect any non-https requests to https
    # Based largely on flask-sslify

    if not app.debug:
        app.config['SESSION_COOKIE_SECURE'] = True

    criteria = [
        app.debug,
        request.is_secure,
        request.headers.get('X-Forwarded-Proto', 'http') == 'https',
    ]

    if not any(criteria):
        if request.url.startswith('http://'):
            url = request.url.replace('http://', 'https://', 1)
            #code = 302
            code = 301
            r = redirect(url, code=code)
            return r

app.before_request(force_https)


#===================================
#=              Index              =
#===================================

@app.route('/index')
@app.route('/')
def index():
    p = Markup(f'''
        <p>Hey, I'm Ramsey!</p>
        
        <p>My main interests are engineering, programming, rock climbing, and puzzle design.</p>

        <p>Some of my links: 
            <a href="https://github.com/rmboyce">github.com/rmboyce</a>
            &middot;
            <a href="https://www.linkedin.com/in/ramseyboyce/">linkedin.com/in/ramseyboyce</a>
        </p>

        <p>Here's a gallery of my recent projects!</p>

        <h2><a href = "{url_for('crossword_generator')}" 
        title="Crossword Generator">Crossword Generator</a> 
        (<a href="{url_for('daily_crossword')}" 
        title="Daily computer-generated crossword">Try today's puzzle!</a>)</h2>
        <p>A program that generates a new crossword puzzle each day</p>
        <p><a href="{url_for('crossword_generator')}" class="linkImage" style="width:402px">
            <img alt="Crossword" 
            src="{url_for('static', filename='resources/crossword.png')}" 
            width="392" height="393">
        </a></p>
        
        <h2><a href="{url_for('serpent_fusion')}" title="Serpent Fusion">Serpent Fusion</a></h2>
        <p>A puzzle game created with the Unity engine and C#</p>
        <p><a href="{url_for('serpent_fusion')}" class="linkImage" style="width:645px">
           <img alt="Serpent Fusion" 
           src="{url_for('static', filename='resources/serpent_fusion.png')}" 
           width="635" height="308">
        </a></p>
        
        <h2><a href = "{url_for('arduino_autoclicker')}" title="Arduino autoclicker">Arduino Autoclicker</a></h2>
        <p>An Arduino shield to augment your mouse</p>
        <p><a href="{url_for('arduino_autoclicker')}" class="linkImage" style="width:494px">
           <img alt="Autoclicker pcb" 
           src="{url_for('static', filename='resources/clickotron_pcb.png')}" 
           width="484" height="679">
        </a></p>

        <h2><a href="{url_for('voronoi_generator')}" title="Voronoi Generator">Voronoi Generator</a></h2>
        <p>An interactive visualization of Voronoi diagrams</p>
        <p>Note: optimized for desktop use</p>
        <p><a href="{url_for('voronoi_generator')}" class="linkImage" style="width:417px">
           <img alt="Voronoi generator" 
           src="{url_for('static', filename='resources/voronoi_generator.png')}" 
           width="407" height="333">
        </a></p>
        
        <p>I also enjoy rock climbing! See more on my 
        <a href = "{url_for('rock_climbing')}" title="Outdoor climbing log">
        outdoor climbing log</a>!</p>
    ''')
    return render_template('customPage.html', title='About Me', pageHtml=p)


if __name__ == '__main__':
    app.run(debug=True)
