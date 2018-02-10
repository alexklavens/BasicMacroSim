#ADASGraph.py
#
#Alex Klavens
#
#COM110
#
#23 December, 2015


from graphics import*
from linedata import*

class ADASGraph:

    """ADASGraph class establishes a graph representing the relationship between
       aggregate demand and supply in the economy

       methods allow for movment and labeling at intersection points"""

    def __init__(self,win,s):
        self.s = s
        self.win = win
        self.equoMarker = 6
        self.ax1 = 0 + s
        self.ay1 = 0
        self.ax2 = 100 + s
        self.ay2 = 100


 

        self.myIntList = [0,100]

        #Axis
        self.xAxis = Line(Point(self.ax1,self.ay1),Point(self.ax1,self.ay2))
        self.yAxis = Line(Point(self.ax1,self.ay1),Point(self.ax2,self.ay1))
        self.xAxis.draw(self.win)
        self.yAxis.draw(self.win)
        self.xAxis.setWidth(3)
        self.yAxis.setWidth(3)

        self.x15 = 15 + s
        self.y85 = 85
        self.x85 = 85 + s
        self.y15 = 15


        self.asX1 = self.x15
        self.asY1 = self.y15
        self.asX2 = self.x85
        self.asY2 = self.y85

        self.adX1 = self.x15
        self.adY1 = self.y85
        self.adX2 = self.x85
        self.adY2 = self.y15

        lw = 4 #line width

        #AS Line
        self.ASLine = Line(Point(self.asX1,self.asY1),Point(self.asX2,self.asY2))
        self.ASLine.setFill("darkorange")
        self.ASLine.setWidth(lw)
        self.ASLine.draw(self.win)

        self.ASLineText = Text(Point((self.ASLine.p2.x + 5),self.ASLine.p2.y),"AS")
        self.ASLineText.draw(self.win)

        #AD Line
        self.ADLine = Line(Point(self.adX1,self.adY1),Point(self.adX2,self.adY2))
        self.ADLine.draw(self.win)
        self.ADLine.setFill("purple3")
        self.ADLine.setWidth(lw)
        self.ADLineText = Text(Point((self.ADLine.p2.x + 5),self.ADLine.p2.y),"AD")
        self.ADLineText.draw(self.win)

        self.getGeoEquo()


        self.activeLine = self._cloneLine()
        self.activeLine.setFill("purple3")
        self.activeLine.setWidth(lw)

    def _cloneLine(self):
        self.activeLine = self.ADLine.clone()
        self.activeLine.draw(self.win)
        return self.activeLine



    def getGeoEquo(self):
        """establishes an initial intersection marker """

        self.geoInterX = getInter(self.ASLine,self.ADLine)
        self.ye1X = self.geoInterX
        self.ye1y = self.ay1 - self.equoMarker

        self.ye1 = Text(Point(self.geoInterX,self.ye1y),"Ye1")
        self.ye1.draw(self.win)

        self.Pe1x = self.ax1 - self.equoMarker
        self.Pe1y = self.ASLine.getLineVal(self.geoInterX)
        self.Pe1 = Text(Point(self.Pe1x,self.Pe1y),"P1")
        self.Pe1.draw(self.win)

        
        return self.geoInterX



    def getRunningEquo(self):
        """establishes an manipulated intersection marker """

        try:
            self.yE.undraw()
            self.pE.undraw()
            self.checkLine.undraw()
        except AttributeError:
            pass

        self.myInterX = getInter(self.ASLine,self.activeLine)
        self.ye1X = self.myInterX
        self.ye1y = self.ay1 - self.equoMarker

        self.Pe2x = self.ax1 - self.equoMarker
        self.Pe2y = self.activeLine.getLineVal(self.myInterX)
        self.pE = Text(Point(self.Pe2x,self.Pe2y),"P2")
        self.pE.draw(self.win)

        self.yE = Text(Point(self.myInterX,self.ye1y),"Ye2")
        self.yE.draw(self.win)

        
        #self.checkLine was used to make sure intersection points were appropriate
##        self.checkLine = Line(Point(self.ye1X,0),Point(self.ye1X,100))
##        self.checkLine.draw(self.win)
        return self.myInterX


    def moveADLine(self,dX):
        """moves the aggregate demand line. takes the parameter of amount of movement"""
        dR = 10
        for i in range(dR):
            self.activeLine.move(dX/dR,0)
        
        self.getRunningEquo() #intersection point


    
def main():
    win = GraphWin('ADASGraph Test',300,300)
    win.setCoords(-10,-10,110,110)
    myGraph = ADASGraph(win,10)
    time.sleep(1)
    myGraph.moveADLine(-30)

    #printing slopes of the lines
    getInter(myGraph.ASLine,myGraph.activeLine)

if __name__ == "__main__":
    main()
