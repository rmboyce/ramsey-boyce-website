var changedText = false;
var space = false;
var c;
var hs1;
const elements = [ "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
                   "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", 
                   "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", 
                   "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", 
                   "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", 
                   "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", 
                   "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", 
                   "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", 
                   "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", 
                   "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", 
                   "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", 
                   "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og" ];

var displayCase = 2;

const TEXT_X_START = 30;
const TEXT_Y_START = 90;
const TEXT_X_OFFSET_BOXES = 35;
const TEXT_Y_OFFSET = 30;

function setup() {
  let cnv = createCanvas(600, 400);
  cnv.parent("p5Container");
	
  hs1 = new HScrollbar(480, 50, 100, 20, 3);
  hs1.setNormalPos(0.9);
  displayCase = 0;
	
  c = new Console(30, 50, 30);
  c.activate();
  c.chars = "princess";
  c.numChars = 8;
}

function matchNextSingleCharElement(prev, target) {
  if (prev.length >= target.length) {
    return prev;
  }
  for (let i = 0; i < elements.length; i++) {
    let element = elements[i];
    if (element.length != 1) {
      continue;
    }
    if (target.substring(prev.length, prev.length + 1).toLowerCase() === element.toLowerCase()) {
      prev += element;
      return prev;
    }
  }
  return "$" + prev;
}

function matchNextDoubleCharElement(prev, target) {
  if (prev.length >= target.length) {
    return prev;
  }
  if (prev.length + 1 >= target.length) {
    return "$" + prev;
  }
  for (let i = 0; i < elements.length; i++) {
    let element = elements[i];
    if (element.length != 2) {
      continue;
    }
    if (target.substring(prev.length, prev.length + 2).toLowerCase() === element.toLowerCase()) {
      prev += element;
      return prev;
    }
  }
  return "$" + prev;
}

// Outputs array of elements
function splitElements(input) {
  let output = [];
  let temp = "";
  for (let i = 0; i < input.length; i++) {
    let c = input.charAt(i);
    if (c >= 'A' && c <= 'Z') {
      if (temp.length > 0) {
        output.push(temp);
      }
      temp = c;
    }
    else {
      temp += c;
    }
  }
  output.push(temp);
  return output;
}

function draw() {
  hs1.update();
  hs1.display();
  
  let oldDisplayCase = displayCase;
  displayCase = (int)(hs1.normalPos * 2 + 0.5);
  if (oldDisplayCase != displayCase) {
    changedText = true;
  }
  
  if (changedText) {
    changedText = false;
    
    background(200, 200, 200);
    
    // Draw HUD
    hs1.update();
    hs1.display();
    fill(0, 0, 0);
    textSize(20);
    noStroke();
    text("Word to Elementize", 30, 25);
    text("Display Mode", 465, 25);
		
    c.display();
    
    // Elementize word
    let targetWord = c.chars;
    let allFailed = true;
    let potentialList = [];
    let tempList = [];
    potentialList.push("");
    while (true) {
      for (let i = 0; i < potentialList.length; i++) {
        tempList.push(matchNextSingleCharElement(potentialList[i], targetWord));
        tempList.push(matchNextDoubleCharElement(potentialList[i], targetWord));
      }
      
      // Count number of failures
      allFailed = true;
      for (let i = 0; i < tempList.length; i++) {
        let word = tempList[i];
        if (word[0] !== "$") {
          allFailed = false;
        }
      }

      potentialList = [];
      if (allFailed) {
        // Add failures to potential list and exit
        for (let i = 0; i < tempList.length; i++) {
          let word = tempList[i];
          word = word.substring(1, word.length);
          potentialList.push(word);
        }
        break;
      }
      else {
        // Continue with non-failures
        let allRightLength = true;
        for (let j = 0; j < tempList.length; j++) {
          let word = tempList[j];
          if (word[0] !== "$") {
            potentialList.push(word);
            if (word.length < targetWord.length) {
              allRightLength = false;
            }
          }
        }
        // If all potential words are the right length, break
        if (allRightLength) {
          break;
        }
      }
      
      tempList = [];
    }
    
    // Remove duplicates
    potentialList = [...new Set(potentialList)];
    
    // ---------------DISPLAY SPELLINGS---------------
    // Show working spelling(s), if any
    textSize(20);
    noStroke();
    strokeWeight(1);
    if (!allFailed) {
      //console.log(potentialList);
      displayWords(displayCase, potentialList, [0, 0, 0]);
    }
    // Else show failed spellings
    else {
      if (potentialList.length > 0) {
        displayWords(displayCase, potentialList, [255, 0, 0]);
      }
      else {
        text("Nothing found", TEXT_X_START, TEXT_Y_START);
      }
      fill(0, 0, 0);
    }
  }
}

function displayWords(displayCase, list, color) {
  fill(...color);
  list = sort(list);
  for (let i = 0; i < list.length; i++) {
    if (displayCase == 0) {
      // Without spaces
      text(list[i], TEXT_X_START, TEXT_Y_START + TEXT_Y_OFFSET * i);
    }
    else if (displayCase == 1) {
      // With spaces
      text(splitElements(list[i]).join(" "), TEXT_X_START, TEXT_Y_START + TEXT_Y_OFFSET * i);
    }
    else if (displayCase == 2) {
      // Boxes
      let oneWord = splitElements(list[i]);
      if (oneWord != null) {
        for (let x = 0; x < oneWord.length; x++) {
          noStroke();
          if (oneWord[x].length == 1) {
            text(oneWord[x], TEXT_X_START + TEXT_X_OFFSET_BOXES * x + 5, TEXT_Y_START + TEXT_Y_OFFSET * i);
          }
          else {
            text(oneWord[x], TEXT_X_START + TEXT_X_OFFSET_BOXES * x, TEXT_Y_START + TEXT_Y_OFFSET * i);
          }
          stroke(...color);
          noFill();
          rect(TEXT_X_START - 2 + TEXT_X_OFFSET_BOXES * x, TEXT_Y_START - 20 + TEXT_Y_OFFSET * i, TEXT_X_OFFSET_BOXES - 4, TEXT_Y_OFFSET - 2);
          fill(...color);
        }
      }
    }
  }
}

function keyPressed() {
  if (keyCode == BACKSPACE) {
    c.deleteChar();
  }
  else if (keyCode == 32) {
    space = true;
  }
}

function keyTyped() {
  if (!space && c.numChars < 17) {
    c.addChar(key);
  }
  space = false;
}
