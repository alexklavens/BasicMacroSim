#ADLineClass
#
#
#
#Alex Klavens
#
#COM110
#23 December, 2015
from graphics import*

class Demand:


    """the Demand class establishes lines for an aggregate demand graph

       these lines will be manipulated by the methods:

       changeMPC and _changeMPC will both be used to alter the slope of a line

       _cloneLine creates a duplicate that will act as the manipulated line

       moveLine will move a line"""

    def __init__(self,win,mpc):
        self.win = win

        self.mpc = 0

        self.lineWidth = 4

        self.initVal = 22 #initial value
        self.ax1 = 0
        self.ay1 = 0
        self.ax2 = 100
        self.ay2 = 100
        
        self.runningSlope = 1
        self.macroMPC = mpc
        self.myGeoList = [self.macroMPC,self.macroMPC]

        self.slope = self.myGeoList[self.mpc]/2
        self.ady1 = self.initVal
        self.adx2 = 90
        self.ady2 = (self.adx2*self.slope)+self.ady1
##        print(self.slope,self.ady2)
##        self.adY2 = 1



        #Initial line
##        self.ADLine = self.drawLine
        self.ADLine = Line(Point(self.ax1,self.ady1),Point(self.adx2,self.ady2))
        self.ADLine.setWidth(self.lineWidth)
        self.ADLine.setFill('brown')
        self.ADLine.draw(self.win)

        self.activeLine = self._cloneLine()
        self.activeLine.setWidth(self.lineWidth)
        self.activeLine.setFill("blue")


        self.ADLineText = Text(Point((self.ADLine.p2.x + 10),self.ADLine.p2.y),"AD1")
        self.ADLineText.draw(self.win)

        self.activeLineText = Text(Point((self.activeLine.p2.x+10),self.activeLine.p2.y),"AD2")
        self.activeLineText.draw(self.win)
    def changeMPC(self,newMPC):
        self.activeLine.undraw()
        newY = self._changeMPC(newMPC)
        self.activeLine.p2.y = newY
        self.activeLine.draw(self.win)
        self.myGeoList[self.runningSlope] = (self.activeLine.p2.y - self.activeLine.p1.y)/self.adx2
        

    
    def _changeMPC(self,newMPC):
        newY = self.adx2*(newMPC/2)+self.activeLine.p1.y
        return newY
                

    def _cloneLine(self):
        self.activeLine = self.ADLine.clone()
        self.activeLine.draw(self.win)
        return self.activeLine

    def moveLine(self,dY):
        dR = 10
        for i in range(dR):
            self.activeLine.move(0,dY/dR)
            self.activeLineText.move(0,dY/dR)
        self.myGeoList[self.runningSlope] = (self.activeLine.p2.y - self.activeLine.p1.y)/self.adx2
        
