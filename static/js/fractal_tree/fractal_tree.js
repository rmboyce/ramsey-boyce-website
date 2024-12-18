// Angle
var angle;

// Branch
var numBranches = 0;
var reduct = 0;
var depth = 0;

// Test number of operations
const initLen = 150;
const max_op = 3000;

// Input
var hs1;
var hs2;
var hs3;
var hs4;

function setup() {
  let cnv = createCanvas(750, 450);
  cnv.parent("p5-container");
  strokeWeight(2);
  stroke(10);
  
  angle = radians(90);
	
  hs1 = new HScrollbar(500, 75, 200, 10, 3, false);
  hs2 = new HScrollbar(500, 175, 200, 10, 3, false);
  hs3 = new HScrollbar(500, 275, 200, 10, 3, false);
  hs4 = new HScrollbar(500, 375, 200, 10, 3, true);
  hs4.rollingUp = true;
  hs4.rollingSpeed = 0.5;
}

// hs: HScrollbar, s: title above, lowVal: low value of the scrollbar, highVal: high value of the scrollbar, per: percentage text below
function textHScrollbar(hs, s, lowVal, highVal, per) {
  hs.update();
  hs.display();
  fill(255, 255, 255);
  textSize(20);
  text(s, hs.xpos, hs.ypos - 25);
  textSize(15);
  text(lowVal, hs.xpos, hs.ypos - 7.5);
  text(highVal, hs.xpos + hs.swidth - 7.5, hs.ypos - 7.5);
  text(per, hs.xpos, hs.ypos + 25);
}

function draw() {
  background(0, 0, 0);
  
  // Input
  numBranches = (int) (2.5 + hs1.normalPos * 3);
  textHScrollbar(hs1, "Number of branches", 2, 5, numBranches);
  
  reduct = hs2.normalPos;
  textHScrollbar(hs2, "Fractional branch length", 0, 1, round(reduct, 3));
  
  depth = (int) (1.5 + hs3.normalPos * 7);
  textHScrollbar(hs3, "Depth", 1, 8, depth);
  
  angle = hs4.normalPos * TWO_PI;
  textHScrollbar(hs4, "Branch angle", 0, round(TWO_PI, 3), round(angle, 3));
  
  // Drawing the tree
  stroke(255, 255, 255);
  translate(height / 2.0, 0);
  
  // Count number of operations
  let operations = operationsCount();
  if (operations >= max_op) {
    noStroke();
    text("Too many operations (" + operations + "), " + max_op + " is the max", 50 - height/2, 50);
  }
  else {
    // Else if the number of operations is okay draw the tree
    if (numBranches % 2 == 0) {
      branchEven(initLen, 0);
    }
    else {
      branchOdd(initLen, 0);
    }
  }
}

function branchEven(len, level) {
  if (level > depth) {
    return;
  }
  line(0, 0, 0, len);
  translate(0, len);
  rotate(angle/2);
  for (let i = 0; i < numBranches/2; i++) {
    push();
    rotate(angle * i);
    branchEven(len * reduct, level + 1);
    pop();
  }
  rotate(-angle);
  for (let i = 0; i < numBranches/2; i++) {
    push();
    rotate(-angle * i);
    branchEven(len * reduct, level + 1);
    pop();
  }
}

function branchOdd(len, level) {
  if (level > depth) {
    return;
  }
  line(0, 0, 0, len);
  translate(0, len);
  for (let i = 0; i <= numBranches/2; i++) {
    push();
    rotate(angle * i);
    branchOdd(len * reduct, level + 1);
    pop();
    push();
    rotate(-angle * i);
    branchOdd(len * reduct, level + 1);
    pop();
  }
}

// Count number of operations drawing a tree would take
function operationsCount() {
  return Math.pow(numBranches, depth);
}
