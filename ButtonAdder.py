#ButtonAdder.py
#
#
#
#Alex Klavens
#
#COM110
#23 December, 2015

from buttonclass import*
from graphics import*
class EcoButton:

    """Class for a set of two buttons that manipulate value

       Takes parameters for GraphWin, centerpoint,size,start value,
       mathmatical manipulator, change interval, and label
       """

    def __init__(self,win,center,width,height,value,ecoType,interval,label,):
        self.win = win
        self.value = value
        self.ecoType = str(ecoType)
        self.interval = interval
        self.label = label
        
        self.ALL = Button(self.win,center,width,height,"")
        x,y = center.getX(),center.getY()
        w,h = width/2.0, height/2.0
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        self.yL_Third = (y+self.ymin)/2
        self.yU_Third = (y+self.ymax)/2

        subWidth = width/1.1

        self.upButton = Button(self.win,Point(x,y),subWidth,height/4,"+")
        self.downButton = Button(self.win,Point(x,self.yL_Third),subWidth,height/4,"-")
        self.buttonLabel = Text(Point(x,self.yU_Third),label)
        self.buttonLabel.setSize(35)
        self.buttonLabel.draw(self.win)


        self._updateValText()
        
        self.displayValue = Text(Point(x,self.ymin+5),self.displayString)        

        self.displayValue.draw(self.win)

        
    def _updateValText(self):

        """Update value display"""
        self.displayString = str(self.value)
        if "." in self.displayString:
            self.displayString = self.displayString[:4]
        
        
    def _increaseVal(self):
        """Increase value"""
        self.value = self.value + self.interval
        if self.interval < 1 and self.value + self.interval >=.99:
                self.value = .99
##                self.interval = .09
                
    def _decreaseVal(self):
        """decrease value"""
        if self.value - self.interval <= 0:
            self.value = 0
        
        else:
            
            self.value = self.value - self.interval

    def runButton(self,pt):
        """takes clicked pt, checks to see if up or down buttons were clicked
           and adjusts appropriate values"""
        if self.upButton.clicked(pt):
            self._increaseVal()
            self.displayValue.setText("")
            self._updateValText()
            self.displayValue.setText(self.displayString)
            return self.value

        elif self.downButton.clicked(pt):
            self._decreaseVal()
            self.displayValue.setText("")
            self._updateValText()
            self.displayValue.setText(self.displayString)
            return self.value
        else:
            return False
        



    def _testButton(self,other):
        """test button"""
        while True:
            print(self.changeValue(),"---",other)

def main():
    #testing changeValue()
    win = GraphWin("Button Test",200,400)
    win.setCoords(0,0,100,200)
    govButton = EcoButton(win,Point(50,100),50,100,1000,50,"G")
    govButton.runButton()
##    while True:
##        govButton.changeValue()

if __name__ == "__main__":
    main()
        
        
        
