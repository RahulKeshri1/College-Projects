#_____________________________________________________________________________________
#   Write a Program to define a class Point with coordinates x and y as attributes.
#   Create relevant methods and print the objects. Also define a method distance to 
#   calculate the distance between any two point objects.
#_____________________________________________________________________________________

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def distance(P1,P2):
        dis=((P1.x-P2.x)**2+(P1.y-P2.y)**2)**0.5
        print(dis)
        return ""
def main():
    P1=Point(4,6)
    P2=Point(1,2)
    print(f"Distance betweeen =\t",end="")
    distance(P1,P2)

main() 