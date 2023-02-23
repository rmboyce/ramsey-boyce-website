from flask import Markup, render_template, url_for

from route_config import app

#===================================
#=        Javascript Demos         =
#===================================

@app.route('/javascript_demos')
def javascript_demos():
    p = Markup(f'''
        <p class="smallDesc">Note: optimized for desktop use</p>

        <h2>
            <a href="{url_for('voronoi_generator')}" title="Voronoi Generator">Voronoi Generator</a>
        </h2>
        <p><a href="{url_for('voronoi_generator')}" class="linkImage" style="width:417px">
           <img alt="Voronoi generator" src="{url_for('static', filename='resources/voronoi_generator.png')}" width="407" height="333">
        </a></p>

        <h2>
            <a href="{url_for('fractal_tree')}" title="Fractal Tree">Fractal Tree</a>
        </h2>
        <p><a href="{url_for('fractal_tree')}" class="linkImage" style="width:453px">
            <img alt="Fractal tree" src="{url_for('static', filename='resources/fractal_tree.png')}" width="443" height="331">
        </a></p>

        <h2>
            <a href="{url_for('orbit_sim')}" title="Orbit Simulator">Orbit Simulator</a>
        </h2>
        <p><a href="{url_for('orbit_sim')}" class="linkImage" style="width:345px">
            <img alt="Orbit simulator" src="{url_for('static', filename='resources/orbit_sim.png')}" width="335" height="335">
        </a></p>

        <h2>
            <a href="{url_for('particle_life')}" title="Particle Life">Particle Life</a>
        </h2>
        <p><a href="{url_for('particle_life')}" class="linkImage" style="width:310px">
            <img alt="Particle life" src="{url_for('static', filename='resources/particle_life.png')}" width="300" height="300">
        </a></p>
        
        <h2>
            <a href="{url_for('element_words')}" title="Element Words">Element Words</a>
        </h2>
        <p><a href="{url_for('element_words')}" class="linkImage" style="width:393px">
            <img alt="Element words" src="{url_for('static', filename='resources/element_words.png')}" width="383" height="323">
        </a></p>
        
        <h2>
            <a href="{url_for('chaos_game')}" title="Chaos Game">Chaos Game</a>
        </h2>
        <p><a href="{url_for('chaos_game')}" class="linkImage" style="width:374px">
            <img alt="Chaos game" src="{url_for('static', filename='resources/chaos_game.png')}" width="364" height="333">
        </a></p>
    ''')
    return render_template('customPage.html', title='Javascript Demos', pageHtml=p)

def generateJsMarkup(jsPath, fileList):
    js = ''
    for f in fileList:
        js += f'''<script src="{url_for('static', filename=(f'js/{jsPath}/{f}'))}" type="text/javascript"></script>\n'''

    return Markup(js)

@app.route('/javascript_demos/chaos_game')
def chaos_game():
    j = generateJsMarkup('chaos_game', ['chaos_game.js', 'Button.js', 'Checkbox.js', 'HScrollbar.js'])
    p = Markup('''
        <p>See the code: <a href="https://github.com/rmboyce/chaos-game" title="Chaos game code" rel="nofollow">https://github.com/rmboyce/chaos-game</a></p>
        <p>This program starts with a polygon and a point in a random location 
        inside it. Then, the program chooses a random vertex from the polygon 
        and makes a copy of the point some fraction of the way between the old 
        point and the vertex. The process is repeated using the new point. 
        Eventually, the points will make a pattern.</p>
        <p>The Sierpinski Carpet Fraction is the ratio between the size of a 
        polygon and the size of smaller polygons that can be put inside the 
        original against its vertices without colliding the other small 
        polygons. The Sierpinski Fraction causes the points to make nice 
        patterns usually, and is calculated in the method 
        CalculateCarpetFraction() if you want to look more into it.</p>
        <p>More information:</p>
        <ul>
            <li><a href="https://en.wikipedia.org/wiki/Sierpinski_carpet" title="Sierpinski carpet Wikipedia" rel="nofollow">https://en.wikipedia.org/wiki/Sierpinski_carpet</a></li>
            <li><a href="http://shiftingmind.com/chaosgame/" title="Shifting mind chaos game" rel="nofollow">http://shiftingmind.com/chaosgame/</a></li>
        </ul>
    ''')
    return render_template('jsDemoPage.html', title='Chaos Game', pageJs=j, pageHtml=p)

@app.route('/javascript_demos/element_words')
def element_words():
    j = generateJsMarkup('element_words', ['element_words.js', 'HScrollbar.js', 'console.js'])
    p = Markup('''
        <p>See the code: <a href="https://github.com/rmboyce/element-words" title="Element words code" rel="nofollow">https://github.com/rmboyce/element-words</a></p>
        <p>Uses atomic element symbols to spell an inputted word. This program 
        finds all possible spellings of a word using elements. If the word 
        cannot be spelled fully, the program goes as far as possible.</p>
        <p>Interesting words that can be spelled:</p>
        <ul>
            <li>Princess</li>
            <li>Accessibilities</li>
            <li>Xenophobe</li>
            <li>Candy cane</li>
            <li>Hyperbolic</li>
        </ul>
    ''')
    return render_template('jsDemoPage.html', title='Element Words', pageJs=j, pageHtml=p)

@app.route('/javascript_demos/fractal_tree')
def fractal_tree():
    j = generateJsMarkup('fractal_tree', ['fractal_tree.js', 'HScrollbar.js'])
    p = Markup('''
        <p>See the code: <a href="https://github.com/rmboyce/fractal-tree" title="Fractal tree code" rel="nofollow">https://github.com/rmboyce/fractal-tree</a></p>
        <p>Draws a fractal tree based on the number of child branches that 
        split off from each parent branch, the size that each child branch 
        will be compared to its parent branch, the minimum branch length the 
        program draws, and the angle between branches.</p>
        <p>The branch angle scrollbar is special; it has momentum and loops.</p>
    ''')
    return render_template('jsDemoPage.html', title='Fractal Tree', pageJs=j, pageHtml=p)

@app.route('/javascript_demos/orbit_sim')
def orbit_sim():
    j = generateJsMarkup('orbit_sim', ['orbit_sim.js', 'Button.js'])
    p = Markup('''
        <p>See the code: <a href="https://github.com/rmboyce/orbit-sim" title="Orbit simulator code" rel="nofollow">https://github.com/rmboyce/orbit-sim</a></p>
        <p>Simple orbit simulator that ignores interactions between planets. 
        It finds where the planets should be and what speeds they should be 
        moving at by solving the two-body problem with the <a href="https://en.wikipedia.org/wiki/Kepler%27s_equation" title="Kepler equation Wikipedia" rel="nofollow">Kepler Equation</a>. 
        Uses Newton's Method to calculate a numerical approximation.</p>
        <p>Control by using four clicks: The first two clicks set the orbit, 
        and the last two set the planet radius.</p>
    ''')
    return render_template('jsDemoPage.html', title='Orbit Simulator', pageJs=j, pageHtml=p)

@app.route('/javascript_demos/particle_life')
def particle_life():
    j = generateJsMarkup('particle_life', ['particle_life.js', 'HScrollbar.js', 'Button.js', 'Checkbox.js'])
    p = Markup('''
        <p>See the code: <a href="https://github.com/rmboyce/particle-life" title="Particle life code" rel="nofollow">https://github.com/rmboyce/particle-life</a></p>
        <p>Simulates forces between particles to create lifelike shapes. Note 
        that the forces don't follow the laws of physics.</p>
        <p>Particle interactions:</p>
        <ul>
            <li>The red particles are "mellow" and clump together</li>
            <li>The green particles repel each other, but are attracted to the blues and reds</li>
            <li>The blue particles are "energetic" and are repelled by reds and greens</li>
        </ul>
        <p>Inspired by CodeParade's video: <a href="https://www.youtube.com/watch?v=Z_zmZ23grXE" title="Particle life video" rel="nofollow">https://www.youtube.com/watch?v=Z_zmZ23grXE</a></p>
    ''')
    return render_template('jsDemoPage.html', title='Particle Life', pageJs=j, pageHtml=p)

@app.route('/javascript_demos/voronoi_generator')
def voronoi_generator():
    j = generateJsMarkup('voronoi_generator', ['voronoi_generator.js', 'Checkbox.js', 'Button.js'])
    p = Markup('''
        <p>See the code: <a href="https://github.com/rmboyce/voronoi-generator" title="Voronoi generator code" rel="nofollow">https://github.com/rmboyce/voronoi-generator</a></p>
        <p>Generates Voronoi diagrams (diagrams where each point in a colored 
        region is closer to the region's "seed point" than any other seed 
        point) and the Delaunay triangulation (a triangulation where the 
        circumcircle of each triangle contains no other points in the 
        triangulation). Click to place "seed points".</p>
        <p>More information:</p>
        <ul>
            <li><a href="https://en.wikipedia.org/wiki/Voronoi_diagram" title="Voronoi diagrams Wikipedia" rel="nofollow">https://en.wikipedia.org/wiki/Voronoi_diagram</a></li>
            <li><a href="https://en.wikipedia.org/wiki/Delaunay_triangulation" title="Delaunay triangulation Wikipedia" rel="nofollow">https://en.wikipedia.org/wiki/Delaunay_triangulation</a></li>
        </ul>
    ''')
    return render_template('jsDemoPage.html', title='Voronoi Generator', pageJs=j, pageHtml=p)
