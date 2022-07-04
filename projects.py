from flask import Markup, url_for, render_template
from route_config import app

#===================================
#=            Projects             =
#===================================

@app.route('/projects')
def projects():
    p = Markup(f'''
        <h2 class="centered">Bigger Projects</h2>

        <h2><a href = "{url_for('serpent_fusion')}" title="Serpent Fusion">Serpent Fusion</a></h2>
        <p>A puzzle game created with the Unity engine and C#</p>

        <h2><a href = "{url_for('crossword_generator')}" title="Crossword Generator">Crossword Generator</a></h2>
        <p>A program that generates a new crossword puzzle each day</p>
        
        <h2><a href = "{url_for('arduino_autoclicker')}" title="Arduino autoclicker">Arduino Autoclicker</a></h2>
        <p>An Arduino shield to augment your mouse</p>
        
        <h2><a href = "{url_for('this_website')}" title="This website">This Website</a></h2>
        <p>A place for my projects using Flask, HTML, and Javascript</p>
        
        
        <h2 class="centered">Smaller Projects</h2>

        <h2><a href = "{url_for('image_rater')}" title="Image Rating Neural Network">Image Rating Neural Network</a></h2>
        <p>An image rater based on the average person's judgement</p>
        
        <h2><a href = "{url_for('cube_timer')}" title="Rubik's Cube timer">Rubik's Cube Timer</a></h2>
        <p>A speed tracker for the Rubik's Cube</p>
    
        <h2><a href = "{url_for('hp_tetris')}" title="HP Prime Tetris">HP Prime Tetris</a></h2>
        <p>A tetris clone for the HP Prime graphing calculator</p>
        
        
        <h2 class="centered">Other</h2>

        <h2><a href = "{url_for('rock_climbing')}" title="Outdoor Climbing Log">Outdoor Climbing Log</a></h2>
        <p>My outdoor rock climbing projects</p>
        
        <h2><a href = "{url_for('videogame_levels')}" title="Videogame levels">Videogame Levels</a></h2>
        <p>Levels I made for fun using games like Portal 2 and Super Meat Boy</p>
    ''')
    return render_template('customPage.html', title='My Projects', pageHtml=p)

@app.route('/projects/serpent_fusion')
def serpent_fusion():
    p = Markup(f'''
        <p class="smallDesc">A puzzle game created with the Unity engine and C#</p>
        
        <h2>Overview</h2>
        <p>I programmed the entirety of my puzzle game Serpent Fusion on my 
        own over about two years, and I regularly release updates. It is a 
        challenging sokoban-style game based on Snake.</p>
        <p>If you are interested, the game is here: <a href="https://store.steampowered.com/app/1126260/Serpent_Fusion/" title="Serpent Fusion" rel="nofollow">Serpent Fusion</a></p>
        <p>Note: This is an extremely challenging puzzle game. (Don't say I didn't warn you!)</p>
        
        <p>
            <img alt="Serpent Fusion" src="{url_for('static', filename='resources/serpent_fusion.png')}" width="635" height="308">
        </p>
        
        <h2>About Creation</h2>
        <p>Nearly all of the code is in C#, although I did tweak some 
        ShaderLab programming to use for visual effects. Rather than program a 
        level editor from scratch, which would take a long time, I decided to 
        make levels in a spreadsheet. This quicker approach proved to help 
        prototype levels faster and determine what would work sooner, aka 
        "fail faster". I made a program that would take my level designs in 
        the spreadsheet and convert them into JSON strings that I could plug 
        into my game to generate levels.</p>
        <p>The game was a learning project&mdash;I wanted to apply the 
        programming I had learned to a larger task. Before this project, I had 
        never programmed in C# (although I did have experience in Java), so I 
        was able to pick up a new language. I also had a lot of fun making 
        levels for other games, so I wanted to design my own puzzle game from 
        scratch.</p>
        <p>In recent updates I have been refactoring the code as I learn more, 
        to make it easier to understand and work on.</p>
    ''')
    return render_template('customPage.html', title='Serpent Fusion', pageHtml=p)

@app.route('/projects/arduino_autoclicker')
def arduino_autoclicker():
    p = Markup(f'''
        <p class="smallDesc">"The Clickotron-5000"</p>
        
        <h2>Overview</h2>
        <p>The Clickotron board is a shield for the Arduino Leonardo that I 
        designed which extends the capabilities of a normal mouse. The 
        Clickotron-5000 autoclicking device uses a Leonardo, a USB Host Shield 
        board, and the Clickotron board on top, with my code loaded on the 
        Arduino.</p>
        <p>The arduino can simulate mouse clicks on the computer, so other 
        input devices can be used to create mouse clicks. For example, I use 
        the Clickotron with two foot pedals as left and right click. The 
        device can also continuously click the mouse buttons when the 
        respective pedal is held down. I made the device because bad posture 
        was causing numbness in my hands and I had trouble using a regular 
        mouse (proper posture and exercises have fixed this!). I still use the 
        autoclicker to play League of Legends with my friends, since over the 
        Covid-19 pandemic it's the best way to stay in touch.</p>
        <p>Link to the code: <a href="https://github.com/rmboyce/arduino-autoclicker" title="Autoclicker code" rel="nofollow">https://github.com/rmboyce/arduino-autoclicker</a></p>
        <p>Link to the schematic: <a href="{url_for('static', filename='resources/clickotron_schematic.pdf')}" title="Autoclicker schematic">Autoclicker schematic</a></p>
        
        <p>
            <img alt="Autoclicker device" src="{url_for('static', filename='resources/clickotron_full.jpg')}" width="689" height="544">
        </p>
        
        <h2>About the Device</h2>
        <p>A normal USB mouse plugs into the USB Host board and the mouse 
        signals are passed through the device. This means that the mouse can 
        be used normally as if it was plugged into the computer without the 
        device (see footnote 1 for details). Then other input devices can be 
        soldered to the Clickotron to generate mouse clicks.</p>
        <p>In my current setup with two foot pedals, the Clickotron has two 
        modes, regular and autoclick. To switch between the modes, hold down 
        both pedals until the autoclick LED turns on or off.</p>
        <p>In regular mode the device will simulate a click for as long as a 
        foot pedal is held down. The left and right click indicator LEDs will 
        also turn on while the Clickotron holds the mouse button down. This 
        allows me to select text by holding the left foot pedal down to hold 
        left click and dragging the mouse across the text.</p>
        <p>In autoclick mode, while a foot pedal is held down the device will 
        constantly click at a speed that is set using a potentiometer soldered 
        to the device. The number of clicks per second is shown by the two 
        seven segment displays on the Clickotron. The click durations are 
        generated based on a normal distribution so that the Clickotron will 
        be indistinguishable from human clicking.</p>
        
        <p>
            <img alt="Autoclicker pcb" src="{url_for('static', filename='resources/clickotron_pcb.png')}" width="484" height="679">
        </p>
        
        <h2>Usage</h2>
        <p>Put together the circuit either using the Clickotron board or a 
        breadboard. If you do not use input devices that normally act as 
        closed switches, you will have to modify the program to click when a 
        "HIGH" voltage is read (basically just change all the "LOW"s into 
        "HIGH"s). Then load the program onto your arduino-make sure that you 
        have the "USB Host Shield Library 2.0" installed in the menu (Tools > 
        Manage Libraries). You will also need an Arduino Leonardo and a USB 
        Host Shield board. If your USB Host Shield board is not set up, you 
        will have to bridge the 5V pad and the 
        <a href="https://en.wikipedia.org/wiki/Serial_Peripheral_Interface" title="SPI (Wikipedia)" rel="nofollow">SPI</a> 
        (a communciation protocol) lines so that power and data go to the 
        circuits.</p>
        <p>Note that applies if your scroll wheel does not seem to be working 
        correctly: If it only works while the mouse is moved, making an edit 
        to the USB Host Shield library will fix it. On Windows you will have 
        to go to Documents > Arduino > libraries > USB_Host_Shield_Library_2.0 
        > hiduniversal.h and add "virtual" on line 60 before the 
        BuffersIdentical function so that it reads 
        "virtual bool BuffersIdentical". For other operating systems you will 
        have to figure out where the USB Host Shield Library is stored and 
        make the same change to the code.</p>
        <p>One place to buy the USB Host board: <a href="https://shop.tkjelectronics.dk/product_info.php?products_id=43" title="Purchase the board" rel="nofollow">https://shop.tkjelectronics.dk/product_info.php?products_id=43</a></p>
        <p>USB Host hardware manual: <a href="https://chome.nerpa.tech/usb-host-shield-hardware-manual/" title="Hardware manual" rel="nofollow">https://chome.nerpa.tech/usb-host-shield-hardware-manual/</a></p>
        <p>USB Host library documentation: <a href="https://github.com/felis/USB_Host_Shield_2.0" title="Library documentation" rel="nofollow">https://github.com/felis/USB_Host_Shield_2.0</a></p>
        
        <p>
            <img alt="Autoclicker pcb camera" src="{url_for('static', filename='resources/clickotron_pcb_camera.jpg')}" width="348" height="489">
        </p>
        
        <h2>Technical Details</h2>
        <p>Link to the schematic: <a href="{url_for('static', filename='resources/clickotron_schematic.pdf')}" title="Autoclicker schematic">Autoclicker schematic</a></p>
        <p>When the switches are closed, current runs from the 5V pin through 
        the 10 kiloohm resistor to ground and the input pins detect a voltage. 
        When the switches open, the resistor pulls down the voltage of the 
        input pins to ground. The foot pedals that I used have the switch 
        normally closed, and pressing the pedal down opens the switch inside. 
        Therefore, I made the program click when pins 12 or 13 read a "LOW" 
        voltage.</p>
        <p>In the LED circuit, the pins of the arduino are set to high when 
        the LED should turn on. There is also a resistor to limit the current 
        and stop the LED from burning out.</p>
        <p>The potentiometer is soldered onto the Clickotron using wires. The 
        device reads the value through pin A5 of the arduino and uses it to 
        set the click speed in autoclick mode.</p>
        <p>The MAX7221 chip is used to drive the two seven segment displays. 
        The arduino sends SPI signals to the chip through the 2x3 ICSP header 
        to control it. The two capacitors C1 and C2 keep the power stable for 
        the chip. I decided to add the capacitors because many websites say 
        that the MAX7221 is extremely sensitive to power fluctuation, although 
        the capacitors are not strictly necessary.</p>
        
        <h2>Notes</h2>
        <p>Note 1: The current code should work with normal USB mice, but some 
        functions may or may not work depending on the exact mouse you use. If 
        you use a more complicated mouse that reports input differently, you 
        will have to change the code so that the HID report the Clickotron 
        device sends to your computer is correct.</p>
    ''')
    return render_template('customPage.html', title='Arduino Autoclicker', pageHtml=p)

@app.route('/projects/this_website')
def this_website():
    p = Markup(f'''
        <p class="smallDesc">A place for my projects using Flask, HTML, and Javascript</p>
        
        <h2>Overview</h2>
        <p>This website is a place for me to put my projects when I complete 
        them. I thought that making a website would be fun, and as a bonus I 
        could share the stuff I've made.</p>
            
        <h2>Technical Details</h2>
        <p>I used Flask as a web framework along with HTML and CSS to make the 
        web pages. I programmed the interactive demos using Javascript.</p>
        <p>For tools, I used Google Cloud's App Engine to host the website.</p>
        
        <p>
            <img alt="Website code" src="{url_for('static', filename='resources/website_code.png')}" width="663" height="300">
        </p>
    ''')
    return render_template('customPage.html', title='This Website', pageHtml=p)

@app.route('/projects/crossword_generator')
def crossword_generator():
    p = Markup(f'''
        <p class="smallDesc">A program that generates crossword puzzles</p>

        <h2><a href="{url_for('daily_crossword')}" title="Daily computer-generated crossword">Try today's puzzle!</a></h2>
        
        <h2>Overview</h2>
        <p>This program generates crossword puzzles using a three step 
        process: first, generate the grid; second, fill the grid with words; 
        and third, clue the filled grid. To make a different puzzle available 
        on my website each day, I began using the web framework Flask so I 
        could do that in Python code.</p>

        <p>
            <img alt="Crossword" src="{url_for('static', filename='resources/crossword.png')}" width="392" height="393">
        </p>

        <h2>Generating the Puzzles</h2>
        <p>Step one, generating the grid, is fairly simple. At the moment my 
        code takes an empty grid, adds 1-2 rows and columns extending inwards 
        from the sides, and fills the middle randomly. Since crossword grids 
        must be rotationally symmetric, it only generates half of it and fills 
        in the rest using the first half.</p>
        <p>Step two, filling the grid with words, is the most complicated 
        step. Trying to fill a crossword grid by brute-force is nearly 
        impossible. The algorithm can be thought of as a tree search where the 
        root of the tree represents an empty grid. Then, somehow pick a slot 
        to fill with a word. For each word that fits in the slot, another 
        partially-filled grid is generated. Then, just repeat with each of the 
        newly generated grids. With enough time, this algorithm will generate 
        a valid filling of the grid; however, it takes hours or days to work, 
        and so it must be optimized. A few of the optimizations were:</p>
        <ul>
            <li>The first optimization was to keep track of the number of possible words that could fit in each slot of the crossword, and stop searching a branch of the tree if any of the numbers of possibilities dropped to zero. This sounds like a lot of extra work for the algorithm, and it is, but the time saved is more than worth it.</li>
            <li>The next improvement was to choose the next word to fill based on which slot in the crossword had the least number of possible words that could fill it. This will likely make it faster to find areas where no words fit a certain slot.</li>
            <li>The last change I made was for the algorithm to pick a word for a certain slot based on what would lead to the highest number of possibilities of words crossing that slot. This means that it's likelier for the algorithm to take profitable branches of the tree.</li>
        </ul>
        <p>With these optimizations, the filling process now usually takes 
        somewhere between 10 seconds and 3 minutes (with code written mostly 
        in Python, and some C++).</p>
        <p>Step three, clueing the filled grid, is also fairly simple. For 
        each word in the filled grid, my code looks at past crosswords and 
        randomly chooses a clue corresponding to that word. These generated 
        puzzles aren't completely original, but computationally generating 
        high-quality clues would be extremely hard or even impossible. This 
        approach is much simpler and works well enough for the time being.</p>

        <h2>Playing on my Website</h2>
        <p>To make a different crossword available on my website each day, I 
        had to use a web framework to make my site dynamic. I chose to use the 
        framework Flask as I already knew how to use Python and Flask seemed 
        good for small projects like this site. Python code selects which 
        crossword puzzle to play on a given day. After that, the puzzle is 
        loaded into a Javascript player that I got from Crossword Nexus, 
        allowing the puzzles to be played in the browser.
    ''')
    return render_template('customPage.html', title='Crossword Generator', pageHtml=p)

@app.route('/projects/image_rater')
def image_rater():
    p = Markup(f'''
        <p class="smallDesc">An image rater based on the average person's judgement</p>
        
        <h2>Overview</h2>
        <p>This is a Python program I made that builds and trains a neural 
        network which assigns aesthetic quality scores to images. The scores 
        are based on what the average person would say. It is trained on 
        images from the <a href="http://refbase.cvc.uab.es/files/MMP2012a.pdf" title="AVA dataset" rel="nofollow">AVA (Aesthetic Visual Analysis)</a> dataset, available <a href="https://academictorrents.com/details/71631f83b11d3d79d8f84efe0a7e12f0ac001460" title="Academictorrents AVA dataset" rel="nofollow">here</a>.</p>
        <p>Uses Jupyter Notebook. Download pdf version of notebook <a href="{url_for('static', filename='resources/Image_Rater_Transfer_Learning.pdf')}" title="Jupyter Notebook pdf">here</a>.</p>
        
        <p>
            <img alt="Network diagram" src="{url_for('static', filename='resources/network_visualization_two_hidden_layers.jpg')}" width="580" height="502">
        </p>
        
        <h2>Usage</h2>
        <p>Download pdf version of Jupyter notebook file <a href="{url_for('static', filename='resources/Image_Rater_Transfer_Learning.pdf')}" title="Jupyter Notebook pdf">here</a>.</p>
        <p>Get the code (an ipynb file): <a href="https://github.com/rmboyce/image_rater" title="Image rater code" rel="nofollow">https://github.com/rmboyce/image_rater</a></p>
        <p>The ipynb is a file you can run on your computer using Jupyter 
        Notebook. If you run the notebook, you will need the AVA dataset on 
        your local computer. Note the hardcoded location ("E:/AVA_dataset") 
        in the python code.</p>
        
        <p>
            <img alt="Transfer learning diagram" src="{url_for('static', filename='resources/transfer_learning.jpg')}" width="647" height="381">
        </p>
        
        <h2>Technical Details</h2>
        <p>The image rater first uses the <a href="https://github.com/machrisaa/tensorflow-vgg" title="VGG Github" rel="nofollow">VGG19</a> network to convert images from the AVA dataset into codes, then runs the codes through a fully-connected network with two hidden layers to return image ratings (see figure 1 above). The rating for an image is in the form of a probability distribution over the integers from 1 (lowest quality) to 10 (highest quality).</p>
        <p>The network achieves a correlation coefficient of 0.52 between the 
        predicted and actual ratings for a validation set of images. 
        Additionally, I do a factor analysis to determine which VGG19 codes 
        have the largest effect on image quality. The notebook includes 
        functions to show a selection of images with high values of any VGG19 
        code.</p>
    ''')
    return render_template('customPage.html', title='Image Rating Neural Network', pageHtml=p)

@app.route('/projects/cube_timer')
def cube_timer():
    p = Markup(f'''
        <p class="smallDesc">A speed tracker for the Rubik's Cube</p>
        
        <h2>Overview</h2>
        <p>This is a Rubik's Cube timer that I made with Python and PyQt to 
        track how fast the user can solve a cube. The program also saves every 
        past logged time in a text file with timestamps, so you can see your 
        improvement in the long run.</p>
        <p>Link to get it: <a href="https://github.com/rmboyce/cube-timer/releases/" title="Rubik's Cube timer releases" rel="nofollow">https://github.com/rmboyce/cube-timer/releases/</a></p>
        <p>Link to see the code: <a href="https://github.com/rmboyce/cube-timer" title="Rubik's Cube timer code" rel="nofollow">https://github.com/rmboyce/cube-timer</a></p>
        
        <p>
            <img alt="Cube timer" src="{url_for('static', filename='resources/cube_timer.png')}" width="663" height="546">
        </p>
            
        <h2>Usage</h2>
        <p>To operate the timer, press and release the spacebar to start (time 
        starts on release) and press the spacebar again to stop. Then you can 
        decide whether to log the time (by pressing space), clear the time, or 
        mark it as a DNF (did not finish: stopped the timer before the cube 
        was completely solved).</p>
        <p>The stats page shows statistics on the previous times in the 
        session (from when the program is opened). The PLL tab  shows some 
        algorithms to permute the last layer of the Rubik's cube.</p>
    ''')
    return render_template('customPage.html', title='Rubik\'s Cube Timer', pageHtml=p)

@app.route('/projects/hp_tetris')
def hp_tetris():
    p = Markup(f'''
        <p class="smallDesc">A tetris clone for the HP Prime graphing calculator</p>
        
        <h2>Overview</h2>
        <p>This is a tetris clone made for the HP Prime graphing calculator 
        written in its HP BASIC programming language. I made it by making a 
        bunch of improvements to Kevin Barbier's "BRICKS" game (you can see 
        the changes in the changelog).</p>
        
        <p>
            <img alt="HP Tetris game" src="{url_for('static', filename='resources/hp_tetris.jpg')}" width="198" height="388">
        </p>
        
        <h2>Getting the Game</h2>
        <p>The easiest way to get the program onto an HP Prime is to install 
        the HP Prime Connectivity Kit (<a href="http://www.hp-prime.de/en/category/15-software" title="HP Prime Connectivity Kit" rel="nofollow">http://www.hp-prime.de/en/category/15-software</a>) on your computer and to connect your computer and HP Prime with the charging cable. Then you can make a new file (call it "BLOCKS") and copy the program over. To run the game, use Shift + 1 to get to the programs menu and just run the "BLOCKS" program.</p>
        <p>Get the code here: <a href="https://github.com/rmboyce/hp-tetris" title="HP Prime Tetris code" rel="nofollow">https://github.com/rmboyce/hp-tetris</a></p>
            
        <h2>Controls</h2>
        <ul>
            <li>"Vars" and the toolbox key to move left/right</li>
            <li>"SIN" to drop the current piece</li>
            <li>"Enter" to hard drop the piece</li>
            <li>The delete key to rotate the piece</li>
            <li>"x<sup>y</sup>" (the power key) to hold the piece (you can only hold a piece once each time you get a new piece)</li>
            <li>"Apps" to pause</li>
            <li>"Esc" to quit</li>
            <li>"Help" for help</li>
            <li>"View" to choose custom keys</li>
            <li>"Menu" to set keys to default</li>
            <li>"CAS" to reset the game</li>
        </ul>
            
        <h2>Changelog</h2>
        <ul>
            <li>Added a grid in the back</li>
            <li>Changed the colors of the pieces to match the standard tetris color scheme</li>
            <li>Changed the way the program picks the next piece to make it feel more random (for example, made the chance of getting the same piece twice in a row much lower) </li>
            <li>Added the tetris super rotation system (makes the pieces rotate intuitively)</li>
            <li>Added the hold function to store a piece</li>
        </ul>
    ''')
    return render_template('customPage.html', title='HP Prime Tetris', pageHtml=p)

@app.route('/projects/rock_climbing')
def rock_climbing():
    p = Markup('''
        <p class="smallDesc">My outdoor rock climbing projects</p>
        
        <h2>Triple Crown, V6</h2>
        <p>Lake Tahoe, CA; Rainbow Boulders area</p>
        <p>This is my first outdoor V6! The rock is great quality. If you are 
        tall, try the left heel hook; it's incredible when you set it 
        right.</p>
        <div class="videoContainer">
            <iframe width="640" height="360" src="https://www.youtube.com/embed/utpF7Am3ZTg" title="Triple Crown rock climb"></iframe>
        </div>
        
        <h2>Ketron Classic, V4</h2>
        <p>Bishop, CA; Happy Boulders area</p>
        <p>A classic, and my first outdoor V4! The leap for the final hold 
        feels epic to stick.</p>
        <div class="videoContainer">
            <iframe width="640" height="360" src="https://www.youtube.com/embed/5OAm6z_8Pdw" title="Ketron Classic rock climb"></iframe>
        </div>
        
        <h2>Serengeti, V5</h2>
        <p>Bishop, CA; Happy Boulders area</p>
        <p>My first V5 outside. There are a lot of ways to do the bottom 
        section, it took a while to figure out the easiest approach for me.</p>
        <div class="videoContainer">
            <iframe width="640" height="360" src="https://www.youtube.com/embed/fzJA3p7K6dU" title="Serengeti rock climb"></iframe>
        </div>
        
        <p>This page is in progess. I'm planning to add the other climbs I've 
        done and my future projects (climbs I'm planning to do).</p>
    ''')
    return render_template('customPage.html', title='Outdoor Climbing Log', pageHtml=p)

@app.route('/projects/videogame_levels')
def videogame_levels():
    p = Markup(f'''
        <p class="smallDesc">Levels I made for fun using games like Portal 2 and Super Meat Boy</p>
        
        <h2>Portal 2</h2>
        <p>I made a lot of Portal 2 levels using Valve's editor and the 
        community-made extension tool BEEmod (<a href="https://github.com/BEEmod/BEE2.4/releases" title="BEE2" rel="nofollow">https://github.com/BEEmod/BEE2.4/releases</a>). 
        I had a lot of fun and learned a lot, but the levels aren't great 
        looking back since I was inexperienced and made most of it when I was 
        13 or 14. If you want to check out my levels, go to <a href="https://steamcommunity.com/profiles/76561198166141294/myworkshopfiles" title="Portal 2 levels" rel="nofollow">my Steam workshop</a>.</p>
        
        <p>
            <img alt="Portal 2 level" src="{url_for('static', filename='resources/portal_2.png')}" width="640" height="360">
        </p>
        
        <h2>Super Meat Boy</h2>
        <p>I also made Super Meat Boy levels around the same time, when I was 
        13-14 years old. The editor is pretty unintuitive so I had to find an 
        online tutorial before I could even use it. This was after Super Meat 
        World, the platform used to share Super Meat Boy levels, shut 
        down&mdash;I had no way of publishing my levels. Looking back this 
        might be a good thing, since a lot of my levels were highly 
        experimental&mdash;the only game I had played before was Minecraft. I 
        might upload the levels here someday, but know that they aren't great 
        (they are very very difficult though).</p>
    ''')
    return render_template('customPage.html', title='Videogame Levels', pageHtml=p)
