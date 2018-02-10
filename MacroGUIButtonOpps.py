#MacroGUIButtonOps.py
#
#
#
#Alex Klavens
#
#COM110
#23 December, 2015

from graphics import*
from MacroClass import*
from ButtonAdder import*
from buttonclass import*
from ADGraph3 import*
from ADASGraph import*

class MacroGUI:
    """MacroGUI class is the main GUI for the macroeconomic simmulation program

       This takes no parameters and has methods allowing for user manipulation
       of macroeconomic variables"""

    def __init__(self):
        self.win = GraphWin("MacroGUIButtonTest",600*1.5,480*1.5)
        self.win.setCoords(-20,-20,100*3,60*4)

        #MacroClass
        self.eco = Macro()

        x = 10
        y = 40*4+10
        w = 10*4
        h = 20*4
        z = 12*4

        #quitButton
        self.quit = Button(self.win,Point(265,225),w,20,"Quit")

        #info
        self.info = Text(Point(265,110),"This is a simulator of \na macro economy.\n\n\nG: \nGovernment Expenditures\n\nI: \nInvestment\n\nNX: \nNet Exports\n\nMPC: \nMarginal Propensity \nto Consume\n\nT: \nTaxes\n\nGDP:\nGross Domestic\nProduct\n\nAD:\nAggregate Demand\n\nAS:\nAggregate Supply\n\nP:\nPrice Level\n\nYe:\nEquilibrium GDP")
        self.info.setSize(14)
        self.info.draw(self.win)

        #header
        self.header = Text(Point(x+z*2,225),"MacroEcon: Simulator")
        self.header.setSize(39)
        self.header.setFill("purple4")
        self.header.draw(self.win)

        #GDP Display
        self.dispGDP = Button(self.win,Point(x+z*2,y-55),h+20,w/3,"")
        self._updateDispGDP()
##        self.dispGDP.draw

        #GOV Button
        self.govButton = EcoButton(self.win,Point(x,y),w,h,self.eco.varList[self.eco.govSpending],"govSpending",25,"G")

        #Investment Button
        self.invButton = EcoButton(self.win,Point(x+z,y),w,h,self.eco.varList[self.eco.investment],"self.investment",25,"I")

        #Export Button
        self.nxButton = EcoButton(self.win,Point(x+z*2,y),w,h,self.eco.varList[self.eco.netExports],"self.netExports",25,"NX")

        #mpc button
        self.mpcButton = EcoButton(self.win,Point(x+z*3,y),w,h,self.eco.varList[self.eco.mpc],"self.mpc",.05,"MPC")

        #taxes button
        self.taxesButton = EcoButton(self.win,Point(x+z*4,y),w,h,self.eco.varList[self.eco.taxes],"self.taxes",25,"T")                                  

        #List of Buttons for manipulation
        self.myList = [self.govButton,self.invButton,self.nxButton,self.mpcButton,self.taxesButton]


        #instances of the ADGraph and ASADGraph classes
        self.myADGraph = ADGraph(self.win,self.eco.varList[self.eco.mpc])
        self.myASGraph = ADASGraph(self.win,130)
##        myADGraph.changeMPC(self.eco.varList[self.eco.mpc])

    def _updateDispGDP(self):
        """is called in the update() method and wil update the display of GDP"""
        self.dispGDP.label.setText("")
        newGDPDisp = str(self.eco.GDP)
        newGDPDisp = newGDPDisp.split(".")
        self.dispGDP.label.setText("GDP: "+ newGDPDisp[0])
##        self.dispGDP.label.setText("GDP: "+str(self.eco.GDP))

    def _updateGraph(self,pt,changer):
        """is called in the update() method and calls upon the
           ADGraph and ADASGraph classes to make graphical changes"""
        if self.govButton.ALL.clicked(pt) or self.invButton.ALL.clicked(pt) or self.nxButton.ALL.clicked(pt) or self.taxesButton.ALL.clicked(pt):
            self.myADGraph.changeExo(changer)
            self.myASGraph.moveADLine(changer)
        elif self.mpcButton.ALL.clicked(pt):
##            self.myADGraph.changeMPC(self.eco.varList[self.eco.mpc])
            self.myADGraph.changeMPC(changer)
##            self.myASGraph.moveADLine(self.gdpChange/200)

        


    def update(self):
        """running in a while loop, this method is the main running method
           for the program. It checks for user interaction and calls for the
           appropriate changes. This while loop will break at the click of the quit button"""
  

        changer = 5
        pt = self.win.getMouse()
        while not self.quit.clicked(pt):
            for i in range(len(self.myList)):
                if self.myList[i].ALL.clicked(pt) and self.myList[i].runButton(pt) != False:


                    preGDP = self.eco.getGDP()                                                  
                    newVal = self.myList[i].runButton(pt)

                    difVal = self.eco.varList[i] - newVal #if positive, negative change, if negative, positive change
                    self.eco.varList[i] = newVal
                    gdpChange = 2
                    postGDP = self.eco.getGDP()
                    self.gdpChange = postGDP - preGDP

                    if self.myList[i] == self.govButton or self.myList[i] == self.invButton or self.myList[i] == self.nxButton:
                        if difVal > 0:
                            self._updateGraph(pt,-changer)
                        elif difVal < 0:
                            self._updateGraph(pt,changer)

                        
                    elif self.myList[i] == self.mpcButton:

                        self._updateGraph(pt,self.eco.varList[i])


                    elif self.myList[i] == self.taxesButton:
                        myTaxesChange = postGDP-preGDP
                        self._updateGraph(pt,myTaxesChange*.1)


            self._updateDispGDP()
            pt = self.win.getMouse()
        self.win.close()
                    
                


def main():
    myGUI = MacroGUI()
    myGUI.update()

if __name__ == "__main__":
    main()

