import time


class TrafficLight:
    # attr
    __light_color = ['red', 'yellow', 'green']

    # mthds
    def running(self):
        print('\033[31mLight is', TrafficLight.__light_color[0])
        time.sleep(7)
        print('\033[33mLight is', TrafficLight.__light_color[1])
        time.sleep(2)
        print('\033[32mLight is', TrafficLight.__light_color[2])
        time.sleep(7)

a = TrafficLight()
a.running()