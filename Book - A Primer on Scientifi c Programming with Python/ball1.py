print ("Normal:",  5*0.6 - 0.5*9.81*0.6**2)	

def ball1(v0, g, t):
    y = v0*t - 0.5*g*t**2
    return print(y)

ball1(5, 9.81, 0.6) # 5 m/s, g = 9.81 m/s^2, t = 0.6 s

