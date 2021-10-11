from math import *
import matplotlib.pyplot as pt

R = 6.37 * 10**6
G = 6.67 * 10 **(-11)

def calc_g(y, M):
    return G * M /(R+y)**2

def calc_speed(ax, ay, t):
    return sqrt((ax*t)**2 + (ay*t)**2)

def calc_accel_x(fullmass, gas_speed, burn_rate, alpha):
    return (gas_speed * burn_rate * cos(alpha)) / fullmass

def calc_accel_y(fullmass, y, gas_speed, burn_rate, M, alpha):
    return (gas_speed * burn_rate * sin(alpha))/fullmass - calc_g(y, M)

def calc_coord(a, t):
    return (a * t ** 2)/2

def calc_fuel(t, fuel, burn_rate):
    return fuel - t * burn_rate

print("Угол старта:")
alpha = float(input()) * pi / 180
print("Масса Земли,кг*10^(-24):")
M = float(input())*10**24
print("Масса топлива,т:")
fuel = float(input()) * 1000
print("Масса ракеты,т:")
rocketmass = float(input())
print("Скорость истечения газа,м/с:")
gasspeed = float(input())
print("Скорость сжигания топлива,т/c:")
burnrate = float(input()) * 1000
burntime = int(fuel / burnrate)
print(burntime)
coordx = [0]
coordy = [0]
ax = 0
ay = 0
curr_x = 0
curr_y = 0
speedx = 0
speedy = 0
speed = 0
currfuel = fuel
for t in range (burntime+1):
    if t > 0:
        currfuel = calc_fuel(t, fuel, burnrate)
        currmass = rocketmass + currfuel
        ax = calc_accel_x(currmass ,gasspeed, burnrate, alpha)
        ay = calc_accel_y(currmass ,curr_y, gasspeed, burnrate, M, alpha)
        coordx.append(calc_coord(ax, t))
        curr_y = calc_coord(ay, t)
        coordy.append(curr_y)
        speed = calc_speed(ax,ay,t)
        speedx = speed * cos(alpha)
        speedy = speed * sin(alpha)
    print("Скорость по x:", speedx)
    print("Скорость по y:", speedy)
    print("Скорость:", speed)
    print("Масса топлива:", currfuel)
pt.title("Траектория ракеты")
pt.plot(coordx,coordy)
pt.show()
