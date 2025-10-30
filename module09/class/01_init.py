

# type == class: int, str, list, set, dict, User, Cat, Site
# instance, object, example, variable -> 12, True, Cat Murchyk, Site Instagram


# абстракція ->  це вибіркове незнання
# self => this

# public, protected, private

class SpeedMonitor:
    def __init__(self, speed, max_speed):
        # property, attributes
        self.speed = speed
        self.max_speed = max_speed
        self.__vincode = "133212321321"
    
    def is_limit_reached(self):
        return self.speed >= self.max_speed
    
    def was_in_car_accident(self):
        pass
    
    def print_warning(self, raise_exc=False):
        limit_reached = self.is_limit_reached()
        if limit_reached:
            print("You better slow down")
        
        if raise_exc:
            raise StopIteration("Stoping the car")


volvo_speed = SpeedMonitor(90, 220)

print(volvo_speed._SpeedMonitor__vincode)
print(volvo_speed.__vincode)
