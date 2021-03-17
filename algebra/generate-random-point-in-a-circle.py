import random
import numpy as np

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x_center = x_center
        self.y_center = y_center
        

    def randPoint(self) -> List[float]:
        angle = random.random()*2*np.pi
        r = self.r * random.random()**.5
        return [self.x_center + r*np.cos(angle), self.y_center + r*np.sin(angle)]
