class HScrollbar {
  constructor(xp, yp, sw, sh, l, loop) {
    this.swidth = sw;
    this.sheight = sh;
    this.widthtoheight = sw - sh;
    this.ratio = sw / this.widthtoheight;
    this.xpos = xp;
    this.ypos = yp-this.sheight/2;
    this.spos = this.xpos + this.swidth/2 - this.sheight/2;
    this.newspos = this.spos;
    this.sposMin = this.xpos;
    this.sposMax = this.xpos + this.swidth - this.sheight;
    this.loose = l;
    this.normalPos = (this.spos - this.sposMin) / (this.sposMax - this.sposMin);
    this.over = false;
    this.locked = false;
    this.looping = loop;
    this.rollingUp = false;
    this.rollingDown = false;
    this.rollingSpeed = 0;
  }

  update() {
    if (this.overEvent()) {
      this.over = true;
    } else {
      this.over = false;
    }
    if (mouseIsPressed && this.over) {
      this.locked = true;
    }
    if (!mouseIsPressed) {
      this.locked = false;
    }
    if (this.locked) {
      this.newspos = this.constrain(mouseX-this.sheight/2, this.sposMin, this.sposMax);
      if (this.looping) {
        if (this.newspos > this.spos) {
          this.rollingUp = true;
          this.rollingDown = false;
          this.rollingSpeed = (this.newspos - this.spos)/5;
        }
        else if (this.newspos < this.spos) {
          this.rollingDown = true;
          this.rollingUp = false;
          this.rollingSpeed = (this.spos - this.newspos)/5;
        }
        if (this.rollingSpeed < 0.5) {
          this.rollingDown = false;
          this.rollingUp = false;
        }
      }
    }
    if (this.rollingUp) {
      this.newspos += this.rollingSpeed;
      if (this.newspos > this.sposMax) {
        this.spos = this.sposMin + (this.newspos % this.sposMax);
        this.newspos = this.spos + this.rollingSpeed;
      }
    }
    else if (this.rollingDown) {
      this.newspos -= this.rollingSpeed;
      if (this.newspos < this.sposMin) {
        this.spos = this.sposMax - (this.sposMin % this.newspos);
        this.newspos = this.spos - this.rollingSpeed;
      }
    }
    if (abs(this.newspos - this.spos) > 1) {
      this.spos = this.spos + (this.newspos-this.spos)/this.loose;
      this.normalPos = (this.spos - this.sposMin) / (this.sposMax - this.sposMin);
    }
  }

  constrain(val, minv, maxv) {
    return min(max(val, minv), maxv);
  }

  overEvent() {
    if (mouseX > this.xpos && mouseX < this.xpos+this.swidth &&
       mouseY > this.ypos && mouseY < this.ypos+this.sheight) {
      return true;
    } else {
      return false;
    }
  }

  display() {
    noStroke();
    fill(255);
    rect(this.xpos, this.ypos, this.swidth, this.sheight);
    if (this.over || this.locked) {
      fill(0, 0, 0);
    } else {
      fill(102, 102, 102);
    }
    rect(this.spos, this.ypos, this.sheight, this.sheight);
  }

  getPos() {
    // Convert spos to be values between
    // 0 and the total width of the scrollbar
    return this.spos * this.ratio;
  }
  
  setPos(value) {
    this.spos = value;
    this.newspos = value;
    this.normalPos = (value - this.sposMin) / (this.sposMax - this.sposMin);
  }
  
  setNormalPos(value) {
    this.normalPos = value;
    this.spos = value * (this.sposMax - this.sposMin) + this.sposMin;
    this.newspos = this.spos;
  }
}
