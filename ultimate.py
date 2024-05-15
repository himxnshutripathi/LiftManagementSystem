class Person:
    def __init__(self, personFloor, personDesti):
        self.persFloor = personFloor
        self.persDest = personDesti
    
    def getPersonDirect(self):
        if self.persFloor > self.persDest:
            return 'Down'
        else: 
            return 'Up'

class Lift:
    def __init__(self,name,currFloor,state,destiFloor):
        self.name = name
        self.currFloor = currFloor
        self.state = state
        self.destiFloor = destiFloor
    
    def calculate_time(self, person_floor, person_direction):
            
            #Lift Stopped
            if self.state == "Stopped":
                return abs(self.currFloor - person_floor)
            
            #Lift moving Upwards
            elif self.state == "Moving" and self.currFloor < self.destiFloor:
                if person_direction == "Up":
                    return abs(person_floor - self.currFloor)
                elif person_direction == "Down" :
                    return abs(self.destiFloor + self.currFloor) + abs(self.destiFloor - person_floor)
                
            
            # Lift Moving Downwards
            elif self.state == "Moving" and self.currFloor > self.destiFloor:
                if person_direction == "Up":
                    return abs(self.destiFloor - self.currFloor) + abs(self.destiFloor - person_floor)
                elif person_direction == "Down" :
                    return abs(self.currFloor - person_floor)
            
            else:
                return abs(self.destiFloor - self.currFloor) +abs(self.destiFloor - person_floor)

def choose_lift(person_floor, persDir, lA, lB):
    time_a = lA.calculate_time(person_floor, persDir)
    time_b = lB.calculate_time(person_floor, persDir)

    if time_a < time_b:
        return lA
    elif time_b < time_a:
        return lB
    else:
        # If both lifts take the same time, choose the one that is closer
        if abs(person_floor - lA.currFloor) < abs(person_floor - lB.currFloor):
            return lA
        else:
            return lB