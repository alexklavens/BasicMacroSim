#line data methods.py
#
#
#
#Alex Klavens
#
#COM110
#23 December, 2015

from graphics import*

#this module returns the x value of the point at which
#two lines intersect"""

def getInter(line1,line2):
    #return intersection point

    #line 1 p1
    line1X1 = line2.p1.x
    line1Y1 = line2.p1.y

    #line1 p2
    line1X2 = line2.p2.x
    line1X2 = line2.p2.y

    #line2 p1
    line2X1 = line2.p1.x
    line2Y1 = line2.p1.y

    #line2 p2
    line2X2 = line2.p2.x
    line2X2 = line2.p2.y

    m1 = line1.getSlope()
    m2 = line2.getSlope()



    #geting a given coordinate
    myLine1Int = line1.getLineVal(0,y=False)
    myLine1Slope = m1
    
    myLine2Int = line2.getLineVal(0,y=False)
    myLine2Slope = m2

    myInterX = (myLine2Int - myLine1Int)/(myLine1Slope-myLine2Slope)

    


    return myInterX






    


 




    
