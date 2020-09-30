dt <- 0.01 # delta t
STEPNO <- 3000 # how many times do you repeat Runge-Kutta
x <- c(1,1) # initial values
timecourse_x = x
f <- function(x){
  f1 = x[2]
  f2 = (1-x[1]^2)*x[2]-x[1]
  return (c(f1,f2))
}
# Algorithm for Runge-Kutta
for (i in 1:STEPNO){
  k1 <- f(x) * dt
  k2 <- f(x + k1/2) * dt
  k3 <- f(x + k2/2) * dt
  k4 <- f(x + k3) * dt
  x <- x + (k1 + 2*k2 + 2*k3 + k4)/6
  timecourse_x = rbind(timecourse_x,x)
}
time = 0:STEPNO * dt
plot(time,timecourse_x[,1])
