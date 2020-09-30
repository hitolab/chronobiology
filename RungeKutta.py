import numpy as np
import matplotlib.pyplot as plt

dt = 0.01 # delta t
stepNO = 3000 # how many times do you repeat Runge-Kutta
x = np.asarray([1.0,1.0])
timecourse_x = x
def f(x):
    f1 = x[1]
    f2 = (1-x[0]*x[0])*x[1]-x[0]
    return np.asarray([f1,f2])

# Algorithm for Runge-Kutta
for i in range(stepNO):
    k1 = f(x) * dt
    k2 = f(x + k1/2) * dt
    k3 = f(x + k2/2) * dt
    k4 = f(x + k3) * dt
    x = x + (k1 + 2*k2 + 2*k3 + k4)/6
    timecourse_x = np.vstack((timecourse_x,x))

time = np.asarray(list(range(stepNO+1))) * dt
plt.plot(time,timecourse_x[:,0])
plt.show()
