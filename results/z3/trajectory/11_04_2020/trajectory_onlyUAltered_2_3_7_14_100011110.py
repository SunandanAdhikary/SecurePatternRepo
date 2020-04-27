from z3 import *
import math
import numpy as np

s = Solver()
set_option(rational_to_decimal=True)
xabs1 = np.zeros(15, dtype=float)
x1 = np.zeros(15, dtype=float)
z1 = np.zeros(15, dtype=float)
xabs2 = np.zeros(15, dtype=float)
x2 = np.zeros(15, dtype=float)
z2 = np.zeros(15, dtype=float)
y1 = np.zeros(15, dtype=float)
attackOnY1 = np.zeros(15, dtype=float)
r1 = np.zeros(15, dtype=float)
u1 = np.zeros(15, dtype=float)
uattacked1 = np.zeros(15, dtype=float)
attackOnU1 = np.zeros(15, dtype=float)
r = np.zeros(15, dtype=float)

y1_0 = Real('y1_0')
r1_0 = Real('r1_0')
rabs1_0 = Real('rabs1_0')
x1_0 = Real('x1_0')
z1_0 = Real('z1_0')
xabs1_0 = Real('xabs1_0')
x2_0 = Real('x2_0')
z2_0 = Real('z2_0')
xabs2_0 = Real('xabs2_0')
u1_0 = Real('u1_0')
uattacked1_0 = Real('uattacked1_0')
r_0 = Real('r_0')
y1_1 = Real('y1_1')
r1_1 = Real('r1_1')
rabs1_1 = Real('rabs1_1')
x1_1 = Real('x1_1')
z1_1 = Real('z1_1')
xabs1_1 = Real('xabs1_1')
x2_1 = Real('x2_1')
z2_1 = Real('z2_1')
xabs2_1 = Real('xabs2_1')
u1_1 = Real('u1_1')
uattacked1_1 = Real('uattacked1_1')
r_1 = Real('r_1')
y1_2 = Real('y1_2')
r1_2 = Real('r1_2')
rabs1_2 = Real('rabs1_2')
x1_2 = Real('x1_2')
z1_2 = Real('z1_2')
xabs1_2 = Real('xabs1_2')
x2_2 = Real('x2_2')
z2_2 = Real('z2_2')
xabs2_2 = Real('xabs2_2')
u1_2 = Real('u1_2')
uattacked1_2 = Real('uattacked1_2')
r_2 = Real('r_2')
y1_3 = Real('y1_3')
r1_3 = Real('r1_3')
rabs1_3 = Real('rabs1_3')
x1_3 = Real('x1_3')
z1_3 = Real('z1_3')
xabs1_3 = Real('xabs1_3')
x2_3 = Real('x2_3')
z2_3 = Real('z2_3')
xabs2_3 = Real('xabs2_3')
u1_3 = Real('u1_3')
uattacked1_3 = Real('uattacked1_3')
r_3 = Real('r_3')
y1_4 = Real('y1_4')
r1_4 = Real('r1_4')
rabs1_4 = Real('rabs1_4')
x1_4 = Real('x1_4')
z1_4 = Real('z1_4')
xabs1_4 = Real('xabs1_4')
x2_4 = Real('x2_4')
z2_4 = Real('z2_4')
xabs2_4 = Real('xabs2_4')
u1_4 = Real('u1_4')
uattacked1_4 = Real('uattacked1_4')
r_4 = Real('r_4')
y1_5 = Real('y1_5')
r1_5 = Real('r1_5')
rabs1_5 = Real('rabs1_5')
x1_5 = Real('x1_5')
z1_5 = Real('z1_5')
xabs1_5 = Real('xabs1_5')
x2_5 = Real('x2_5')
z2_5 = Real('z2_5')
xabs2_5 = Real('xabs2_5')
u1_5 = Real('u1_5')
uattacked1_5 = Real('uattacked1_5')
r_5 = Real('r_5')
y1_6 = Real('y1_6')
r1_6 = Real('r1_6')
rabs1_6 = Real('rabs1_6')
x1_6 = Real('x1_6')
z1_6 = Real('z1_6')
xabs1_6 = Real('xabs1_6')
x2_6 = Real('x2_6')
z2_6 = Real('z2_6')
xabs2_6 = Real('xabs2_6')
u1_6 = Real('u1_6')
uattacked1_6 = Real('uattacked1_6')
r_6 = Real('r_6')
y1_7 = Real('y1_7')
r1_7 = Real('r1_7')
rabs1_7 = Real('rabs1_7')
x1_7 = Real('x1_7')
z1_7 = Real('z1_7')
xabs1_7 = Real('xabs1_7')
x2_7 = Real('x2_7')
z2_7 = Real('z2_7')
xabs2_7 = Real('xabs2_7')
u1_7 = Real('u1_7')
uattacked1_7 = Real('uattacked1_7')
r_7 = Real('r_7')
y1_8 = Real('y1_8')
r1_8 = Real('r1_8')
rabs1_8 = Real('rabs1_8')
x1_8 = Real('x1_8')
z1_8 = Real('z1_8')
xabs1_8 = Real('xabs1_8')
x2_8 = Real('x2_8')
z2_8 = Real('z2_8')
xabs2_8 = Real('xabs2_8')
u1_8 = Real('u1_8')
uattacked1_8 = Real('uattacked1_8')
r_8 = Real('r_8')
y1_9 = Real('y1_9')
r1_9 = Real('r1_9')
rabs1_9 = Real('rabs1_9')
x1_9 = Real('x1_9')
z1_9 = Real('z1_9')
xabs1_9 = Real('xabs1_9')
x2_9 = Real('x2_9')
z2_9 = Real('z2_9')
xabs2_9 = Real('xabs2_9')
u1_9 = Real('u1_9')
uattacked1_9 = Real('uattacked1_9')
r_9 = Real('r_9')
y1_10 = Real('y1_10')
r1_10 = Real('r1_10')
rabs1_10 = Real('rabs1_10')
x1_10 = Real('x1_10')
z1_10 = Real('z1_10')
xabs1_10 = Real('xabs1_10')
x2_10 = Real('x2_10')
z2_10 = Real('z2_10')
xabs2_10 = Real('xabs2_10')
u1_10 = Real('u1_10')
uattacked1_10 = Real('uattacked1_10')
r_10 = Real('r_10')
y1_11 = Real('y1_11')
r1_11 = Real('r1_11')
rabs1_11 = Real('rabs1_11')
x1_11 = Real('x1_11')
z1_11 = Real('z1_11')
xabs1_11 = Real('xabs1_11')
x2_11 = Real('x2_11')
z2_11 = Real('z2_11')
xabs2_11 = Real('xabs2_11')
u1_11 = Real('u1_11')
uattacked1_11 = Real('uattacked1_11')
r_11 = Real('r_11')
y1_12 = Real('y1_12')
r1_12 = Real('r1_12')
rabs1_12 = Real('rabs1_12')
x1_12 = Real('x1_12')
z1_12 = Real('z1_12')
xabs1_12 = Real('xabs1_12')
x2_12 = Real('x2_12')
z2_12 = Real('z2_12')
xabs2_12 = Real('xabs2_12')
u1_12 = Real('u1_12')
uattacked1_12 = Real('uattacked1_12')
r_12 = Real('r_12')
y1_13 = Real('y1_13')
r1_13 = Real('r1_13')
rabs1_13 = Real('rabs1_13')
x1_13 = Real('x1_13')
z1_13 = Real('z1_13')
xabs1_13 = Real('xabs1_13')
x2_13 = Real('x2_13')
z2_13 = Real('z2_13')
xabs2_13 = Real('xabs2_13')
u1_13 = Real('u1_13')
uattacked1_13 = Real('uattacked1_13')
r_13 = Real('r_13')
y1_14 = Real('y1_14')
r1_14 = Real('r1_14')
rabs1_14 = Real('rabs1_14')
x1_14 = Real('x1_14')
z1_14 = Real('z1_14')
xabs1_14 = Real('xabs1_14')
x2_14 = Real('x2_14')
z2_14 = Real('z2_14')
xabs2_14 = Real('xabs2_14')
u1_14 = Real('u1_14')
uattacked1_14 = Real('uattacked1_14')
r_14 = Real('r_14')

s.add(x1_0 >= -2.5)
s.add(x1_0 <= 2.5)
s.add(z1_0 == 0)
s.add(xabs1_0 == If(x1_0<0,(-1)*x1_0,x1_0))
s.add(x2_0 >= -3.0)
s.add(x2_0 <= 3.0)
s.add(z2_0 == 0)
s.add(xabs2_0 == If(x2_0<0,(-1)*x2_0,x2_0))
s.add(y1_0 == 0)
s.add(u1_0 == 0)
s.add(uattacked1_0 == 0)

# pattern = 1
s.add(r1_0 == y1_0 - (1*z1_0) - (0*z2_0) - (0*u1_0))
s.add(rabs1_0 == If(r1_0<0,(-1)*r1_0,r1_0))
s.add(r_0 ==rabs1_0 )
s.add(r_0<2)
s.add(z1_1 ==  (1.0*z1_0) + (0.1*z2_0) + (0.005*u1_0) + (0.9902*r1_0) )
s.add(z2_1 ==  (0.0*z1_0) + (1.0*z2_0) + (0.1*u1_0) + (0.9892*r1_0) )
s.add(x1_1 ==  (1.0*x1_0) + (0.1*x2_0) + (0.005*uattacked1_0) )
s.add(x2_1 ==  (0.0*x1_0) + (1.0*x2_0) + (0.1*uattacked1_0) )
s.add(xabs1_1 == If(x1_1<0,(-1)*x1_1,x1_1))
s.add(xabs2_1 == If(x2_1<0,(-1)*x2_1,x2_1))
s.add(u1_1 ==  - (16.0302*z1_1) - (5.6622*z2_1))
s.add(uattacked1_1 == u1_1)
s.add(y1_1 ==  + (1*x1_1) + (0*x2_1) + (0*uattacked1_1))
s.add(And(y1_1>-30,y1_1<30))
# pattern = 0
s.add(r1_1 == y1_1 - (1*z1_1) - (0*z2_1) - (0*u1_1))
s.add(rabs1_1 == If(r1_1<0,(-1)*r1_1,r1_1))
s.add(r_1 ==rabs1_1 )
s.add(r_1<2)
s.add(z1_2 ==  (1.0*z1_1) + (0.1*z2_1) + (0.005*u1_1) + (0.9902*r1_1) )
s.add(z2_2 ==  (0.0*z1_1) + (1.0*z2_1) + (0.1*u1_1) + (0.9892*r1_1) )
s.add(x1_2 ==  (1.0*x1_1) + (0.1*x2_1) + (0.005*uattacked1_1) )
s.add(x2_2 ==  (0.0*x1_1) + (1.0*x2_1) + (0.1*uattacked1_1) )
s.add(xabs1_2 == If(x1_2<0,(-1)*x1_2,x1_2))
s.add(xabs2_2 == If(x2_2<0,(-1)*x2_2,x2_2))
s.add(u1_2 == u1_1)
s.add(uattacked1_2 == uattacked1_1)
s.add(y1_2 ==  + (1*x1_2) + (0*x2_2) + (0*uattacked1_2))
s.add(And(y1_2>-30,y1_2<30))
# pattern = 0
s.add(r1_2 == y1_2 - (1*z1_2) - (0*z2_2) - (0*u1_2))
s.add(rabs1_2 == If(r1_2<0,(-1)*r1_2,r1_2))
s.add(r_2 ==rabs1_2 )
s.add(r_2<2)
s.add(z1_3 ==  (1.0*z1_2) + (0.1*z2_2) + (0.005*u1_2) + (0.9902*r1_2) )
s.add(z2_3 ==  (0.0*z1_2) + (1.0*z2_2) + (0.1*u1_2) + (0.9892*r1_2) )
s.add(x1_3 ==  (1.0*x1_2) + (0.1*x2_2) + (0.005*uattacked1_2) )
s.add(x2_3 ==  (0.0*x1_2) + (1.0*x2_2) + (0.1*uattacked1_2) )
s.add(xabs1_3 == If(x1_3<0,(-1)*x1_3,x1_3))
s.add(xabs2_3 == If(x2_3<0,(-1)*x2_3,x2_3))
s.add(u1_3 == u1_2)
s.add(uattacked1_3 == uattacked1_2)
s.add(y1_3 ==  + (1*x1_3) + (0*x2_3) + (0*uattacked1_3))
s.add(And(y1_3>-30,y1_3<30))
# pattern = 0
s.add(r1_3 == y1_3 - (1*z1_3) - (0*z2_3) - (0*u1_3))
s.add(rabs1_3 == If(r1_3<0,(-1)*r1_3,r1_3))
s.add(r_3 ==rabs1_3 )
s.add(r_3<2)
s.add(z1_4 ==  (1.0*z1_3) + (0.1*z2_3) + (0.005*u1_3) + (0.9902*r1_3) )
s.add(z2_4 ==  (0.0*z1_3) + (1.0*z2_3) + (0.1*u1_3) + (0.9892*r1_3) )
s.add(x1_4 ==  (1.0*x1_3) + (0.1*x2_3) + (0.005*uattacked1_3) )
s.add(x2_4 ==  (0.0*x1_3) + (1.0*x2_3) + (0.1*uattacked1_3) )
s.add(xabs1_4 == If(x1_4<0,(-1)*x1_4,x1_4))
s.add(xabs2_4 == If(x2_4<0,(-1)*x2_4,x2_4))
s.add(u1_4 == u1_3)
s.add(uattacked1_4 == uattacked1_3)
attackOnY1_3 = Real('attackOnY1_3')
s.add(y1_4 == (1.0*attackOnY1_3) + (1*x1_4) + (0*x2_4) + (0*uattacked1_4))
s.add(And(y1_4>-30,y1_4<30))
# pattern = 1
s.add(r1_4 == y1_4 - (1*z1_4) - (0*z2_4) - (0*u1_4))
s.add(rabs1_4 == If(r1_4<0,(-1)*r1_4,r1_4))
s.add(r_4 ==rabs1_4 )
s.add(r_4<2)
s.add(z1_5 ==  (1.0*z1_4) + (0.1*z2_4) + (0.005*u1_4) + (0.9902*r1_4) )
s.add(z2_5 ==  (0.0*z1_4) + (1.0*z2_4) + (0.1*u1_4) + (0.9892*r1_4) )
s.add(x1_5 ==  (1.0*x1_4) + (0.1*x2_4) + (0.005*uattacked1_4) )
s.add(x2_5 ==  (0.0*x1_4) + (1.0*x2_4) + (0.1*uattacked1_4) )
s.add(xabs1_5 == If(x1_5<0,(-1)*x1_5,x1_5))
s.add(xabs2_5 == If(x2_5<0,(-1)*x2_5,x2_5))
s.add(u1_5 ==  - (16.0302*z1_5) - (5.6622*z2_5))
attackOnU1_4 = Real('attackOnU1_4')
s.add(uattacked1_5 == u1_5+ (0.0*attackOnU1_4))
attackOnY1_4 = Real('attackOnY1_4')
s.add(y1_5 == (1.0*attackOnY1_4) + (1*x1_5) + (0*x2_5) + (0*uattacked1_5))
s.add(And(y1_5>-30,y1_5<30))
# pattern = 1
s.add(r1_5 == y1_5 - (1*z1_5) - (0*z2_5) - (0*u1_5))
s.add(rabs1_5 == If(r1_5<0,(-1)*r1_5,r1_5))
s.add(r_5 ==rabs1_5 )
s.add(r_5<2)
s.add(z1_6 ==  (1.0*z1_5) + (0.1*z2_5) + (0.005*u1_5) + (0.9902*r1_5) )
s.add(z2_6 ==  (0.0*z1_5) + (1.0*z2_5) + (0.1*u1_5) + (0.9892*r1_5) )
s.add(x1_6 ==  (1.0*x1_5) + (0.1*x2_5) + (0.005*uattacked1_5) )
s.add(x2_6 ==  (0.0*x1_5) + (1.0*x2_5) + (0.1*uattacked1_5) )
s.add(xabs1_6 == If(x1_6<0,(-1)*x1_6,x1_6))
s.add(xabs2_6 == If(x2_6<0,(-1)*x2_6,x2_6))
s.add(u1_6 ==  - (16.0302*z1_6) - (5.6622*z2_6))
attackOnU1_5 = Real('attackOnU1_5')
s.add(uattacked1_6 == u1_6+ (0.0*attackOnU1_5))
attackOnY1_5 = Real('attackOnY1_5')
s.add(y1_6 == (1.0*attackOnY1_5) + (1*x1_6) + (0*x2_6) + (0*uattacked1_6))
s.add(And(y1_6>-30,y1_6<30))
# pattern = 1
s.add(r1_6 == y1_6 - (1*z1_6) - (0*z2_6) - (0*u1_6))
s.add(rabs1_6 == If(r1_6<0,(-1)*r1_6,r1_6))
s.add(r_6 ==rabs1_6 )
s.add(r_6<2)
s.add(z1_7 ==  (1.0*z1_6) + (0.1*z2_6) + (0.005*u1_6) + (0.9902*r1_6) )
s.add(z2_7 ==  (0.0*z1_6) + (1.0*z2_6) + (0.1*u1_6) + (0.9892*r1_6) )
s.add(x1_7 ==  (1.0*x1_6) + (0.1*x2_6) + (0.005*uattacked1_6) )
s.add(x2_7 ==  (0.0*x1_6) + (1.0*x2_6) + (0.1*uattacked1_6) )
s.add(xabs1_7 == If(x1_7<0,(-1)*x1_7,x1_7))
s.add(xabs2_7 == If(x2_7<0,(-1)*x2_7,x2_7))
s.add(u1_7 ==  - (16.0302*z1_7) - (5.6622*z2_7))
attackOnU1_6 = Real('attackOnU1_6')
s.add(uattacked1_7 == u1_7+ (0.0*attackOnU1_6))
attackOnY1_6 = Real('attackOnY1_6')
s.add(y1_7 == (1.0*attackOnY1_6) + (1*x1_7) + (0*x2_7) + (0*uattacked1_7))
s.add(And(y1_7>-30,y1_7<30))
# pattern = 1
s.add(r1_7 == y1_7 - (1*z1_7) - (0*z2_7) - (0*u1_7))
s.add(rabs1_7 == If(r1_7<0,(-1)*r1_7,r1_7))
s.add(r_7 ==rabs1_7 )
s.add(r_7<2)
s.add(z1_8 ==  (1.0*z1_7) + (0.1*z2_7) + (0.005*u1_7) + (0.9902*r1_7) )
s.add(z2_8 ==  (0.0*z1_7) + (1.0*z2_7) + (0.1*u1_7) + (0.9892*r1_7) )
s.add(x1_8 ==  (1.0*x1_7) + (0.1*x2_7) + (0.005*uattacked1_7) )
s.add(x2_8 ==  (0.0*x1_7) + (1.0*x2_7) + (0.1*uattacked1_7) )
s.add(xabs1_8 == If(x1_8<0,(-1)*x1_8,x1_8))
s.add(xabs2_8 == If(x2_8<0,(-1)*x2_8,x2_8))
s.add(u1_8 ==  - (16.0302*z1_8) - (5.6622*z2_8))
attackOnU1_7 = Real('attackOnU1_7')
s.add(uattacked1_8 == u1_8+ (0.0*attackOnU1_7))
attackOnY1_7 = Real('attackOnY1_7')
s.add(y1_8 == (1.0*attackOnY1_7) + (1*x1_8) + (0*x2_8) + (0*uattacked1_8))
s.add(And(y1_8>-30,y1_8<30))
# pattern = 0
s.add(r1_8 == y1_8 - (1*z1_8) - (0*z2_8) - (0*u1_8))
s.add(rabs1_8 == If(r1_8<0,(-1)*r1_8,r1_8))
s.add(r_8 ==rabs1_8 )
s.add(r_8<2)
s.add(z1_9 ==  (1.0*z1_8) + (0.1*z2_8) + (0.005*u1_8) + (0.9902*r1_8) )
s.add(z2_9 ==  (0.0*z1_8) + (1.0*z2_8) + (0.1*u1_8) + (0.9892*r1_8) )
s.add(x1_9 ==  (1.0*x1_8) + (0.1*x2_8) + (0.005*uattacked1_8) )
s.add(x2_9 ==  (0.0*x1_8) + (1.0*x2_8) + (0.1*uattacked1_8) )
s.add(xabs1_9 == If(x1_9<0,(-1)*x1_9,x1_9))
s.add(xabs2_9 == If(x2_9<0,(-1)*x2_9,x2_9))
s.add(u1_9 == u1_8)
s.add(uattacked1_9 == uattacked1_8)
attackOnY1_8 = Real('attackOnY1_8')
s.add(y1_9 == (1.0*attackOnY1_8) + (1*x1_9) + (0*x2_9) + (0*uattacked1_9))
s.add(And(y1_9>-30,y1_9<30))
# pattern = 1
s.add(r1_9 == y1_9 - (1*z1_9) - (0*z2_9) - (0*u1_9))
s.add(rabs1_9 == If(r1_9<0,(-1)*r1_9,r1_9))
s.add(r_9 ==rabs1_9 )
s.add(r_9<2)
s.add(z1_10 ==  (1.0*z1_9) + (0.1*z2_9) + (0.005*u1_9) + (0.9902*r1_9) )
s.add(z2_10 ==  (0.0*z1_9) + (1.0*z2_9) + (0.1*u1_9) + (0.9892*r1_9) )
s.add(x1_10 ==  (1.0*x1_9) + (0.1*x2_9) + (0.005*uattacked1_9) )
s.add(x2_10 ==  (0.0*x1_9) + (1.0*x2_9) + (0.1*uattacked1_9) )
s.add(xabs1_10 == If(x1_10<0,(-1)*x1_10,x1_10))
s.add(xabs2_10 == If(x2_10<0,(-1)*x2_10,x2_10))
s.add(u1_10 ==  - (16.0302*z1_10) - (5.6622*z2_10))
attackOnU1_9 = Real('attackOnU1_9')
s.add(uattacked1_10 == u1_10+ (0.0*attackOnU1_9))
attackOnY1_9 = Real('attackOnY1_9')
s.add(y1_10 == (1.0*attackOnY1_9) + (1*x1_10) + (0*x2_10) + (0*uattacked1_10))
s.add(And(y1_10>-30,y1_10<30))
# pattern = 0
s.add(r1_10 == y1_10 - (1*z1_10) - (0*z2_10) - (0*u1_10))
s.add(rabs1_10 == If(r1_10<0,(-1)*r1_10,r1_10))
s.add(r_10 ==rabs1_10 )
s.add(r_10<2)
s.add(z1_11 ==  (1.0*z1_10) + (0.1*z2_10) + (0.005*u1_10) + (0.9902*r1_10) )
s.add(z2_11 ==  (0.0*z1_10) + (1.0*z2_10) + (0.1*u1_10) + (0.9892*r1_10) )
s.add(x1_11 ==  (1.0*x1_10) + (0.1*x2_10) + (0.005*uattacked1_10) )
s.add(x2_11 ==  (0.0*x1_10) + (1.0*x2_10) + (0.1*uattacked1_10) )
s.add(xabs1_11 == If(x1_11<0,(-1)*x1_11,x1_11))
s.add(xabs2_11 == If(x2_11<0,(-1)*x2_11,x2_11))
s.add(u1_11 == u1_10)
s.add(uattacked1_11 == uattacked1_10)
s.add(y1_11 ==  + (1*x1_11) + (0*x2_11) + (0*uattacked1_11))
s.add(And(y1_11>-30,y1_11<30))
# pattern = 0
s.add(r1_11 == y1_11 - (1*z1_11) - (0*z2_11) - (0*u1_11))
s.add(rabs1_11 == If(r1_11<0,(-1)*r1_11,r1_11))
s.add(r_11 ==rabs1_11 )
s.add(r_11<2)
s.add(z1_12 ==  (1.0*z1_11) + (0.1*z2_11) + (0.005*u1_11) + (0.9902*r1_11) )
s.add(z2_12 ==  (0.0*z1_11) + (1.0*z2_11) + (0.1*u1_11) + (0.9892*r1_11) )
s.add(x1_12 ==  (1.0*x1_11) + (0.1*x2_11) + (0.005*uattacked1_11) )
s.add(x2_12 ==  (0.0*x1_11) + (1.0*x2_11) + (0.1*uattacked1_11) )
s.add(xabs1_12 == If(x1_12<0,(-1)*x1_12,x1_12))
s.add(xabs2_12 == If(x2_12<0,(-1)*x2_12,x2_12))
s.add(u1_12 == u1_11)
s.add(uattacked1_12 == uattacked1_11)
s.add(y1_12 ==  + (1*x1_12) + (0*x2_12) + (0*uattacked1_12))
s.add(And(y1_12>-30,y1_12<30))
# pattern = 0
s.add(r1_12 == y1_12 - (1*z1_12) - (0*z2_12) - (0*u1_12))
s.add(rabs1_12 == If(r1_12<0,(-1)*r1_12,r1_12))
s.add(r_12 ==rabs1_12 )
s.add(r_12<2)
s.add(z1_13 ==  (1.0*z1_12) + (0.1*z2_12) + (0.005*u1_12) + (0.9902*r1_12) )
s.add(z2_13 ==  (0.0*z1_12) + (1.0*z2_12) + (0.1*u1_12) + (0.9892*r1_12) )
s.add(x1_13 ==  (1.0*x1_12) + (0.1*x2_12) + (0.005*uattacked1_12) )
s.add(x2_13 ==  (0.0*x1_12) + (1.0*x2_12) + (0.1*uattacked1_12) )
s.add(xabs1_13 == If(x1_13<0,(-1)*x1_13,x1_13))
s.add(xabs2_13 == If(x2_13<0,(-1)*x2_13,x2_13))
s.add(u1_13 == u1_12)
s.add(uattacked1_13 == uattacked1_12)
s.add(y1_13 ==  + (1*x1_13) + (0*x2_13) + (0*uattacked1_13))
s.add(And(y1_13>-30,y1_13<30))
# pattern = 1
s.add(r1_13 == y1_13 - (1*z1_13) - (0*z2_13) - (0*u1_13))
s.add(rabs1_13 == If(r1_13<0,(-1)*r1_13,r1_13))
s.add(r_13 ==rabs1_13 )
s.add(r_13<2)
s.add(z1_14 ==  (1.0*z1_13) + (0.1*z2_13) + (0.005*u1_13) + (0.9902*r1_13) )
s.add(z2_14 ==  (0.0*z1_13) + (1.0*z2_13) + (0.1*u1_13) + (0.9892*r1_13) )
s.add(x1_14 ==  (1.0*x1_13) + (0.1*x2_13) + (0.005*uattacked1_13) )
s.add(x2_14 ==  (0.0*x1_13) + (1.0*x2_13) + (0.1*uattacked1_13) )
s.add(xabs1_14 == If(x1_14<0,(-1)*x1_14,x1_14))
s.add(xabs2_14 == If(x2_14<0,(-1)*x2_14,x2_14))
s.add(u1_14 ==  - (16.0302*z1_14) - (5.6622*z2_14))
s.add(uattacked1_14 == u1_14)
s.add(y1_14 ==  + (1*x1_14) + (0*x2_14) + (0*uattacked1_14))
s.add(And(y1_14>-30,y1_14<30))
s.add(Or((xabs1_0 - 25)>1,(xabs1_1 - 25)>1,(xabs1_2 - 25)>1,(xabs1_3 - 25)>1,(xabs1_4 - 25)>1,(xabs1_5 - 25)>1,(xabs1_6 - 25)>1,(xabs1_7 - 25)>1,(xabs1_8 - 25)>1,(xabs1_9 - 25)>1,(xabs1_10 - 25)>1,(xabs1_11 - 25)>1,(xabs1_12 - 25)>1,(xabs1_13 - 25)>1,(xabs2_0 - 30)>1,(xabs2_1 - 30)>1,(xabs2_2 - 30)>1,(xabs2_3 - 30)>1,(xabs2_4 - 30)>1,(xabs2_5 - 30)>1,(xabs2_6 - 30)>1,(xabs2_7 - 30)>1,(xabs2_8 - 30)>1,(xabs2_9 - 30)>1,(xabs2_10 - 30)>1,(xabs2_11 - 30)>1,(xabs2_12 - 30)>1,(xabs2_13 - 30)>1))

if s.check() != sat:
	print(s.check())
	isSat = 0
else:
	print(s.check())
	isSat = 1
	f0 = open("../results/z3/trajectory/trajectory_downtime.z3result", "w+")
	f0.write("1")
	f0.close()
	m = s.model()
	for d in m.decls():
		if "attackOnU1_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			attackOnU1[i] = float(y)
		if "uattacked1_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			uattacked1[i] = float(y)
		if "u1_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			u1[i] = float(y)
		if "z1_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			z1[i] = float(y)
		if "xabs1_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			xabs1[i] = float(y)
		if "x1_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			x1[i] = float(y)
		if "z2_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			z2[i] = float(y)
		if "xabs2_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			xabs2[i] = float(y)
		if "x2_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			x2[i] = float(y)
		if "attackOnY1_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			attackOnY1[i] = float(y)
		if "y1_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			y1[i] = float(y)
		if "r1_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			r1[i] = float(y)
		if "r_" in d.name():
			i = int(d.name().split('_')[1])
			x = str(m[d])
			index = x.find("?")
			if index != -1:
				y = x[:-1]
			else:
				y = x
			r[i] = float(y)
	for i in range(14):
		print("x1_{0}={1}".format(i,x1[i]))
		print("x2_{0}={1}".format(i,x2[i]))
		print("z1_{0}={1}".format(i,z1[i]))
		print("z2_{0}={1}".format(i,z2[i]))
		print("xabs1_{0}={1}".format(i,xabs1[i]))
		print("xabs2_{0}={1}".format(i,xabs2[i]))
		print("attackOnU1_{0}={1}".format(i,attackOnU1[i]))
		print("u1_{0}={1}".format(i,u1[i]))
		print("uattacked1_{0}={1}".format(i,uattacked1[i]))
		print("attackOnY1_{0}={1}".format(i,attackOnY1[i]))
		print("y1_{0}={1}".format(i,y1[i]))
		print("r1_{0}={1}".format(i,r1[i]))
		print("r_{0}={1}".format(i,r[i]))
print("attack on control signal component 1")
print(attackOnU1)
print("attack on sensor 1")
print(attackOnY1)
if isSat==1:
	f0 = open("../results/z3/trajectory/trajectory_downtime.z3result", "w+")
	f0.write("1")
	f0.close()
