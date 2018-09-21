import redcar as car

#try:
car.init() # do automatically on load
#car.testAllOutputs()
car.setCmd("F",0.2)
car.go()

#finally:
#    car.finish()
