#MacroClass.py
#
#
#
#Alex Klavens
#
#COM110
#23 December, 2015

class Macro:
    """Macro class provides mathmatical basis for macroeconomic manipulations

       the main method used is getGDP which calculates a gdp level

       other methods exist in this module but are not called upon in other
       modules assisting in the COM110 final project. These other methods will
       hopefully be used to enhance later, more advanced versions of this program
       """

    def __init__(self):

        #set default value for economic variables
        
        self.govSpending = 0
        self.investment = 1
        self.intRate = 0 
        self.mpc = 3
        self.initVal = 200
          #self._consumption() #a+bYd (a should probably be random number)

        self.taxes = 4 #adjust later for non-fixed taxes
        self.netExports = 2

        self.varList = [1000,600,100,.5,1000]
        self.multiplier= 1/(1-self.varList[self.mpc]) #adjust later for non-fixed taxes



        
        self.GDP = self.getGDP() #getGDP function




    def getGDP(self):
        """accounting for the multiplier effect, getGDP() uses the formula

           Y = a+mpc(Y-T) + G + I + NX to output a GDP"""

        
        self.multiplier = 1/(1-self.varList[self.mpc])
        self.GDP = self.multiplier*(self.initVal - (self.varList[self.mpc] * self.varList[self.taxes]) + self.varList[self.govSpending] + self.varList[self.investment] + self.varList[self.netExports])
        return self.GDP


    """Function to return any given value of a variable """

    def getEcoVar(self,kind):
        self.kind = kind
        return self.kind


    """Function to set the full Employment level"""
    def setFullEmployment(self,fullVal):
        self.FullEmployment = fullVal
        return self.FullEmployment

    """ Function to determine recessionary or inflationary gap """

    def determineGap(self):
        self.gap = self.FullEmployment - self.GDP
        if self.GDP < self.FullEmployment:
            return "Recessionary Gap"
        elif self.GDP > self.FullEmployment:
            return "Inflationary Gap"
        else:
            return "We are at full employment"

    """Function to change any given thing in Economy
        kind   -  user shoul d type "self.gov" to change gov
        change -  should be entered as negative or positive value"""

    def changeEco(self,kind,change):
        self.kind = kind + change
        self.GDP = self.GDP + (self.multiplier * change)
        return self.kind

    def destroy_the_Economy(self):
        """The single most important method #2008 #occupy"""
        self.GDP = self.GDP - self.GDP
        return "All is lost. The GDP is now " + str(self.GDP)

    """Function to suggest fiscal policy"""
    def fiscal(self):
        if self.gap > 0:
            print("implement fiscal to cure recession")
        else:
            print("cure inflation")
        


def main():
    myEco = Macro()
    print("G: ",myEco.govSpending)
    print("I: ",myEco.investment)
    print("NX: ",myEco.netExports)
    print("MPC: ",myEco.mpc)
    print("Multiplier",myEco.multiplier)
    print()
    GDP = myEco.getGDP()
    print("GDP: ",GDP)
    myFull = myEco.setFullEmployment(300)
    print("Gap: ",myEco.determineGap())
    print("\n\n")
    print("changeEco() test (increase G by 100): ",myEco.changeEco(myEco.investment,-50))
    print("getEcoVar() test (with mpc): ",myEco.getEcoVar(myEco.mpc))
    print()
    print("tryna use the multiplier: ",myEco.GDP)
    print()
    myEco.fiscal()
##    print(myEco.destroy_the_Economy())
    
if __name__ == "__main__":
    main()
