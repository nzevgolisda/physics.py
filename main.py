from Physics import Object
## (mass = 1, height = 0, initialVeloc = 0, acceleration = 0, resistance = 0, time = 0)
self = Object(1, 0, 0, 0, 0, 0)
self.createTframe()
for frame in self.tFrame:
    print(frame.v)
    print(frame.findEnergy())
print('###')
objStop = Object(1, 0, 10, -1, 0, 0).getStopped()
print(objStop.x,' m of space passed while ',objStop.findEnergy(),' Joule were spent')