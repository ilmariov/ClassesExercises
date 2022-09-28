from sphere import Sphere

def main ():
    radius = float(input("\nEnter the radius of the sphere in cm: "))
    sphere = Sphere(radius)
    print ('Volume of the sphere: {0:0.2f} cm3'.format(sphere.volume()))
    print('Surface area: {0:0.2f} cm2'.format(sphere.surfaceArea()))

if __name__=='__main__':
    main()