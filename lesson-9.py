class Camera:
    counter = 0

    def __init__(self):
        print('New camera added')
        self.counter = 0 #публичный
        self._is_on = False #защищенный
        self.__working_time = 10 #приватный
        Camera.counter += 1

    def turn(self, is_on : bool):
            self._is_on = is_on
    
    def define_working_hours(self, hours):
        if isinstance(hours, int):
            print('Time changed!')
            self.__working_time = hours
        else:
            print('Time not changed')
    
    def sent_data(self):
        print('Data send!')

class Recognizer:
    def __init__(self):
        self.model = 'NN'
        print('Recognizer!')

    def get_people_in_frame(self, frame=None):
        print('Someone detected!')



class HumanCamera(Recognizer, Camera):
    def __init__(self, model_type = "NN"):
        super().__init__(model_type)
        self._is_on = False #защищенный
        self.__working_time = 10 #приватный
        Camera.counter += 1
        self.human_counter = 0
        
    def recognize_drinkers(self):
        print('No one founded')

    def sent_data(self):
        print('Message: no one founded')


camera_Tverskaya_street= Camera()
camera_Pushkinshakay_street = HumanCamera()
camera_Lenina_square = HumanCamera()

#print(camera_Tverskaya_street._is_on)
#camera_Tverskaya_street.turn(True)
#camera_Pushkinshakay_street.turn(True)
#print(camera_Tverskaya_street._is_on)
#print(camera_Pushkinshakay_street._is_on)
#camera_Pushkinshakay_street.recognize_drinkers()
#camera_Tverskaya_street.sent_data()
#camera_Pushkinshakay_street.sent_data()
#print(camera_Tverskaya_street._Camera__working_time)
#print(Camera.counter)
#print(type(camera_Tverskaya_street))
#camera_Lenina_square.define_working_hours('10')

camera_Lenina_square.recognize_drinkers()