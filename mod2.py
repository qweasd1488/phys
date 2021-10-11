from math import *
import matplotlib.pyplot as pt

e = -1.6 * 1 ** (-19)
m = 9.1 * 1 ** (-31)
freq = 10**6

def calc_a(y, U, R, r):
    r_inner = R - r
    return (e * U / (y * log(R / r_inner))) / m
print("U,В:")
U = float(input())
print("Радиус внешнего цилиндра, см:")
R = float(input()) / 100
print("Расстояние между обкладками, см:")
r = float(input()) / 100
print("Длина конденсатора, см:")
l = float(input()) / 100
print("Диэл.проницаемость:")
eps = float(input())
print("Скорость,м/c:")
v0 = float(input())

r_inner = R - r
v = [v0]
v_x, v_y = [v0], [0]
a = [0]
x, y = [0], [r_inner + r/2]
t = [0]
dt = 1
while x[-1] < l and r_inner < y[-1] < R:
    v.append(sqrt(v_x[-1] ** 2 + v_y[-1] ** 2))
    t.append(dt / freq)
    a.append(calc_a(y[-1], U, R, r))
    v_y.append(a[-1] * dt)
    v_x.append(v0)
    y.append(r_inner + r/2 + (a[-1] * dt**2)/(2 * freq))
    x.append(v0 * dt / freq)
    dt += 1
    print("x:", x[-1])
    print("y:", y[-1])
    print("Скорость по y:", v_y[-1])
    print("Скорость:", v[-1])
    print("Ускорение:", a[-1])
pt.title("y(x)")
pt.plot(x, y)
pt.show()
pt.title("y(t)")
pt.plot(t, y)
pt.show()
pt.title("v(t)")
pt.plot(t, v)
pt.show()
pt.title("a(t)")
pt.plot(t,a)
pt.show()
