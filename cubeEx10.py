from cube import Cube

def main ():
    l_side = float(input("\nEnter the side-lenght of the cube in cm: "))
    cube = Cube(l_side)
    print ('Volume of the cube: {0:0.2f} cm3'.format(cube.volume()))
    print('Surface area: {0:0.2f} cm2'.format(cube.surfaceArea()))

if __name__=='__main__':
    main()