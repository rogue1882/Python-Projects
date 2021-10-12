class vehicle:
    #engin type
    engine = ''
    # number of doors
    doors = ''
    # body style
    body = ''
    # tire and rim style
    wheels = ''

#child 1 of class vehicle

class motorcycle(vehicle):
    #type of drive line
    drive = ''
    # amount of cc's for motor
    CC = ''
    # exhaust cutom or standard
    exhaust = ''

# child 2 of class vehicle
class truck(vehicle):
    # bed size
    bed = ''
    # weight class 
    weight = ''
    # standard, off road, extreme 4X4
    ground_clearence = 0
