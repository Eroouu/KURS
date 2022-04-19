class PID:
    def __init__(self, neededlevel):
        self.Kp = 0.52
        self.Ki = 0.0559
        self.Kd = 0.054
        self.lastError = 0
        self.P = 0
        self.I = 0
        self.D = 0
        self.neededlevel = neededlevel;

    def update(self, newLevel, dt):
        error = self.neededlevel - newLevel
        self.P = error
        self.I += error * dt
        self.D = (error - self.lastError) / dt
        self.lastError = error

        rez = self.P * self.Kp + self.I * self.Ki + self.D * self.Kd
        return rez

