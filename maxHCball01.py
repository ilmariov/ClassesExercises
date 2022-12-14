from projectile import Projectile

def getInputs():
    a = float(input('Enter the launch angle (in deegres): '))
    v = float(input('Enter the initial velocity (in meters/sec): '))
    h = float(input('Enter the initial height (in meters): '))
    t = float(input('Enter the time interval between position calculations: '))
    return a, v, h, t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    hMax = 0
    while cball.getY() >= 0:
        cball.update(time)
        if cball.isHMax(time):
            hMax = cball.getY()

    print('\nDistance traveled: {0:0.1f} meters.'.format(cball.getX()))
    print('Max height: {0:0.1f} meters.'.format(hMax))


if __name__=='__main__':main()