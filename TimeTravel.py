import matplotlib.pyplot as plt
import numpy as np

# Synthetic data
time = np.linspace(0, 10, 1000)
normal_age = time


class TimeTravel:
    def __init__(self, time):
        self.time = time
        self.normal_age = time

    def plot(self, travel_age, label):
        plt.plot(self.time, self.normal_age, label="Normal Age")
        plt.plot(self.time, travel_age, label=label + " Travel")
        plt.legend()
        plt.show()

    def EndersGame(self):
        travel_age = np.sqrt(self.time)
        self.plot(travel_age, "Ender's Game")

    def BackToFuture(self):
        travel_age = np.piecewise(self.time, [self.time < 5, self.time >= 5], [lambda time: time, lambda time: time - 3])
        self.plot(travel_age, "Back to the Future")

    def GroundhogDay(self):
        travel_age = np.piecewise(self.time, [self.time < 2, self.time >= 2], [lambda time: time, lambda time: 2])
        self.plot(travel_age, "Groundhog Day")

    def HarryPotter(self):
        travel_age = np.piecewise(self.time, [self.time < 2, self.time < 5, self.time >= 5],
                                  [lambda time: time, lambda time: 2, lambda time: time - 3])
        self.plot(travel_age, "Harry Potter")

    def Interstellar(self):
        travel_age = np.piecewise(self.time, [self.time < 5, self.time < 7, self.time >= 7],
                                  [lambda time: time, lambda time: time*2, lambda time: time + 2])
        self.plot(travel_age, "Interstellar")

    def Arrival(self):
        travel_age = np.piecewise(self.time, [self.time < 5, self.time >= 5],
                                  [lambda time: time, lambda time: 5 + np.sin(time)])
        self.plot(travel_age, "Arrival")

    def Inception(self):
        travel_age = np.piecewise(self.time, [self.time < 3, self.time < 7, self.time >= 7],
                                  [lambda time: time, lambda time: time*0.5, lambda time: time*0.33])
        self.plot(travel_age, "Inception")



time_travel = TimeTravel(time)

time_travel.EndersGame()
time_travel.BackToFuture()
time_travel.GroundhogDay()
time_travel.HarryPotter()
time_travel.Interstellar()
time_travel.Arrival()
time_travel.Inception()
