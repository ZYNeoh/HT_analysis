import numpy as np

air_k = 0.02699
air_v = 1.75e-5
air_Pr = 0.7241

len = 6
d = 0.08
g = 9.81

Tamb = 20
Tso = 70
Tf = (Tamb + Tso)/2

beta = 1 / (Tf + 273)

Rad = g * beta * d * d * d * (Tso - Tamb) * air_Pr / air_v / air_v

Nu = (0.6 + 0.387 * np.power(Rad,1/6) / np.power(1 + np.power(0.559/air_Pr,9/16),8/27)) ** 2

h = air_k * Nu / d 
As = np.pi * d * len

q_dot = h * As * (Tso - Tamb)

print(q_dot)