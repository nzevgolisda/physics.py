class Object:
    def __init__(self, mass = 1, height = 0, initialVeloc = 0, acceleration = 0, resistance = 0, time = 0):
        self.g = 9.81
        self.m = mass
        self.h = height
        self.v0 = initialVeloc
        self.a = acceleration
        self.T = resistance
        self.t = time
        self.initMovement()
    def initMovement(self):
        self.aY = 0
        self.v = self.v0 + self.a * self.t
        self.p = self.m * self.v
        self.x = self.v0 * self.t + (1/2.0) * self.a * (self.t ** 2)
    
    def findForceY(self):
        SFy = self.m * self.aY
        # N - m * g = m * a
        N = self.m * (self.g + self.aY)
        return N
    def findForceX(self):
        SFx = self.m * self.a
        # Fx - T = m * a
        Fx = self.m * self.a + self.T
        return Fx
    def findEnergy(self):
        self.energyMotion = 0.5 * self.m * (self.v ** 2) # v0 was put in order to run the programm 
        self.energyDynamic = self.m * self.g * self.h
        return self.energyDynamic + self.energyMotion
    def createTframe(self):        
        tFrame = []
        for index in range(100):
            tFrame.append(Object(1, 0, 10, 0, 0, index))
        self.tFrame = tFrame
    def getStopped(self):
        if self.a < 0:
            tStop = - self.v0 / self.a
            return Object(self.m, self.h, self.v, self.a, self.T, tStop)
        else:
            return 'It will not stop by time'