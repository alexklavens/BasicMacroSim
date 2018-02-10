#ADGraph.py
#
#
#
#Alex Klavens
#
#COM110
#23 December, 2015

from graphics import*
import time
from DemandGraphClass import*


class ADGraph:

    """ADGraph class sets up an aggregate demand levels graph

       takes parameters of a GraphWin and an mpc that will determine slope

       methods allow graphical vertical and angular movement of lines,
       labels of intersection points"""

    def __init__(self,win,mpc):
        self.win = win

        self.initMPC = mpc
        self.mpc = 0

        self.myGeoList = [self.initMPC]
        self.equoMarker = 6

        self.initVal = 20
        self.ax1 = 0
        self.ay1 = 0
        self.ax2 = 100
        self.ay2 = 100



        #Axis
        self.xAxis = Line(Point(self.ax1,self.ay1),Point(self.ax1,self.ay2))
        self.yAxis = Line(Point(self.ax1,self.ay1),Point(self.ax2,self.ay1))
        self.xAxis.draw(self.win)
        self.xAxis.setWidth(3)
        self.yAxis.draw(self.win)
        self.yAxis.setWidth(3)

        #45˚ Line
        self.middleLine = Line(Point(self.ax1,self.ay1),Point(85,85))
        self.middleLine.draw(self.win)
        self.middleLine.setFill("green4")
        self.middleLine.setWidth(3)
        self.middleLineText = Text(Point((self.middleLine.p2.x + 5),self.middleLine.p2.y),"45˚")
        self.middleLineText.draw(self.win)


    
        self.initLine = Demand(self.win,self.initMPC)
        self.getGeoEquo()


    def drawADLine(self,rid = False):
        
        #start line
        self.ADLine = Line(Point(self.ax1,self.ady1),Point(self.adx2,self.ady2))
        if rid == True:
            print("trying to undraw")
            print(type(self.ADLine))
            self.ADLine.undraw()
##            return False
        else:
            self.myGeoList[self.mpc] = .9
            self.ADLine.setFill('red')
            self.ADLine.draw(self.win)
            print("tried here")




    def getGeoEquo(self):

        """establishes label at initial intersection point"""
        self.sectVal = self.initLine.ady1/(1-self.initLine.slope)

        #draw Ye1 text
        self.ye1x = self.sectVal
        self.ye1y = self.ax1 - self.equoMarker
        self.ye1 = Text(Point(self.ye1x,self.ye1y),"Ye1")
        self.ye1.draw(self.win)
        
        return self.sectVal

    def getRunningEquo(self):
        """ establishes lable at manipulated intersection point"""
        try:
            self.yE.undraw()
        except AttributeError:
            pass
            
        self.sectRunVal = self.initLine.activeLine.p1.y/(1-self.initLine.myGeoList[self.initLine.runningSlope])

        self.ye1x = self.sectRunVal
        self.ye1y = self.ay1 - self.equoMarker
        self.yE = Text(Point(self.ye1x,self.ye1y),"Ye2")
        self.yE.draw(self.win)
        return self.sectRunVal

    def changeMPC(self,change):
        """employs a method from the Demand class to change slope"""
        self.initLine.changeMPC(change)
        self.getRunningEquo() #updates intersection point

    def changeExo(self,change):
        """moves line"""
        self.initLine.moveLine(change)
        self.getRunningEquo() #intersection point


    
    
def main():
    print("Initialize\n---------")
    myGraph = ADGraph()
    myGraph.changeExo(20)
##    myGraph.changeMPC(.2)
    myGraph.changeExo(-30)
##    myGraph.changeMPC(.9)
    myGraph.changeExo(25)




if __name__ == "__main__":
    main()
    
