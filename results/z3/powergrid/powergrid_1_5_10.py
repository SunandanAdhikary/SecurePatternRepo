from z3 import *
import math
import numpy as np

s = Solver()
set_option(rational_to_decimal=True)
attack1 = np.zeros(11, dtype=float)
attack2 = np.zeros(11, dtype=float)
x1_abs = np.zeros(11, dtype=float)
x1 = np.zeros(11, dtype=float)
z1 = np.zeros(11, dtype=float)
x2_abs = np.zeros(11, dtype=float)
x2 = np.zeros(11, dtype=float)
z2 = np.zeros(11, dtype=float)
y1 = np.zeros(11, dtype=float)
attackOnY1 = np.zeros(11, dtype=float)
r1 = np.zeros(11, dtype=float)
y2 = np.zeros(11, dtype=float)
attackOnY2 = np.zeros(11, dtype=float)
r2 = np.zeros(11, dtype=float)
u1 = np.zeros(11, dtype=float)
attackOnU1 = np.zeros(11, dtype=float)
u2 = np.zeros(11, dtype=float)
attackOnU2 = np.zeros(11, dtype=float)
r = np.zeros(11, dtype=float)
y1_0 = Real('y1_0')
r1_0 = Real('r1_0')
rabs1_0 = Real('rabs1_0')
y2_0 = Real('y2_0')
r2_0 = Real('r2_0')
rabs2_0 = Real('rabs2_0')
x1_0 = Real('x1_0')
z1_0 = Real('z1_0')
x1_abs_0 = Real('x1_abs_0')
x2_0 = Real('x2_0')
z2_0 = Real('z2_0')
x2_abs_0 = Real('x2_abs_0')
u1_0 = Real('u1_0')
u1_attacked_0 = Real('u1_attacked_0')
u2_0 = Real('u2_0')
u2_attacked_0 = Real('u2_attacked_0')
r_0 = Real('r_0')
y1_1 = Real('y1_1')
r1_1 = Real('r1_1')
rabs1_1 = Real('rabs1_1')
y2_1 = Real('y2_1')
r2_1 = Real('r2_1')
rabs2_1 = Real('rabs2_1')
x1_1 = Real('x1_1')
z1_1 = Real('z1_1')
x1_abs_1 = Real('x1_abs_1')
x2_1 = Real('x2_1')
z2_1 = Real('z2_1')
x2_abs_1 = Real('x2_abs_1')
u1_1 = Real('u1_1')
u1_attacked_1 = Real('u1_attacked_1')
u2_1 = Real('u2_1')
u2_attacked_1 = Real('u2_attacked_1')
r_1 = Real('r_1')
y1_2 = Real('y1_2')
r1_2 = Real('r1_2')
rabs1_2 = Real('rabs1_2')
y2_2 = Real('y2_2')
r2_2 = Real('r2_2')
rabs2_2 = Real('rabs2_2')
x1_2 = Real('x1_2')
z1_2 = Real('z1_2')
x1_abs_2 = Real('x1_abs_2')
x2_2 = Real('x2_2')
z2_2 = Real('z2_2')
x2_abs_2 = Real('x2_abs_2')
u1_2 = Real('u1_2')
u1_attacked_2 = Real('u1_attacked_2')
u2_2 = Real('u2_2')
u2_attacked_2 = Real('u2_attacked_2')
r_2 = Real('r_2')
y1_3 = Real('y1_3')
r1_3 = Real('r1_3')
rabs1_3 = Real('rabs1_3')
y2_3 = Real('y2_3')
r2_3 = Real('r2_3')
rabs2_3 = Real('rabs2_3')
x1_3 = Real('x1_3')
z1_3 = Real('z1_3')
x1_abs_3 = Real('x1_abs_3')
x2_3 = Real('x2_3')
z2_3 = Real('z2_3')
x2_abs_3 = Real('x2_abs_3')
u1_3 = Real('u1_3')
u1_attacked_3 = Real('u1_attacked_3')
u2_3 = Real('u2_3')
u2_attacked_3 = Real('u2_attacked_3')
r_3 = Real('r_3')
y1_4 = Real('y1_4')
r1_4 = Real('r1_4')
rabs1_4 = Real('rabs1_4')
y2_4 = Real('y2_4')
r2_4 = Real('r2_4')
rabs2_4 = Real('rabs2_4')
x1_4 = Real('x1_4')
z1_4 = Real('z1_4')
x1_abs_4 = Real('x1_abs_4')
x2_4 = Real('x2_4')
z2_4 = Real('z2_4')
x2_abs_4 = Real('x2_abs_4')
u1_4 = Real('u1_4')
u1_attacked_4 = Real('u1_attacked_4')
u2_4 = Real('u2_4')
u2_attacked_4 = Real('u2_attacked_4')
r_4 = Real('r_4')
y1_5 = Real('y1_5')
r1_5 = Real('r1_5')
rabs1_5 = Real('rabs1_5')
y2_5 = Real('y2_5')
r2_5 = Real('r2_5')
rabs2_5 = Real('rabs2_5')
x1_5 = Real('x1_5')
z1_5 = Real('z1_5')
x1_abs_5 = Real('x1_abs_5')
x2_5 = Real('x2_5')
z2_5 = Real('z2_5')
x2_abs_5 = Real('x2_abs_5')
u1_5 = Real('u1_5')
u1_attacked_5 = Real('u1_attacked_5')
u2_5 = Real('u2_5')
u2_attacked_5 = Real('u2_attacked_5')
r_5 = Real('r_5')
y1_6 = Real('y1_6')
r1_6 = Real('r1_6')
rabs1_6 = Real('rabs1_6')
y2_6 = Real('y2_6')
r2_6 = Real('r2_6')
rabs2_6 = Real('rabs2_6')
x1_6 = Real('x1_6')
z1_6 = Real('z1_6')
x1_abs_6 = Real('x1_abs_6')
x2_6 = Real('x2_6')
z2_6 = Real('z2_6')
x2_abs_6 = Real('x2_abs_6')
u1_6 = Real('u1_6')
u1_attacked_6 = Real('u1_attacked_6')
u2_6 = Real('u2_6')
u2_attacked_6 = Real('u2_attacked_6')
r_6 = Real('r_6')
y1_7 = Real('y1_7')
r1_7 = Real('r1_7')
rabs1_7 = Real('rabs1_7')
y2_7 = Real('y2_7')
r2_7 = Real('r2_7')
rabs2_7 = Real('rabs2_7')
x1_7 = Real('x1_7')
z1_7 = Real('z1_7')
x1_abs_7 = Real('x1_abs_7')
x2_7 = Real('x2_7')
z2_7 = Real('z2_7')
x2_abs_7 = Real('x2_abs_7')
u1_7 = Real('u1_7')
u1_attacked_7 = Real('u1_attacked_7')
u2_7 = Real('u2_7')
u2_attacked_7 = Real('u2_attacked_7')
r_7 = Real('r_7')
y1_8 = Real('y1_8')
r1_8 = Real('r1_8')
rabs1_8 = Real('rabs1_8')
y2_8 = Real('y2_8')
r2_8 = Real('r2_8')
rabs2_8 = Real('rabs2_8')
x1_8 = Real('x1_8')
z1_8 = Real('z1_8')
x1_abs_8 = Real('x1_abs_8')
x2_8 = Real('x2_8')
z2_8 = Real('z2_8')
x2_abs_8 = Real('x2_abs_8')
u1_8 = Real('u1_8')
u1_attacked_8 = Real('u1_attacked_8')
u2_8 = Real('u2_8')
u2_attacked_8 = Real('u2_attacked_8')
r_8 = Real('r_8')
y1_9 = Real('y1_9')
r1_9 = Real('r1_9')
rabs1_9 = Real('rabs1_9')
y2_9 = Real('y2_9')
r2_9 = Real('r2_9')
rabs2_9 = Real('rabs2_9')
x1_9 = Real('x1_9')
z1_9 = Real('z1_9')
x1_abs_9 = Real('x1_abs_9')
x2_9 = Real('x2_9')
z2_9 = Real('z2_9')
x2_abs_9 = Real('x2_abs_9')
u1_9 = Real('u1_9')
u1_attacked_9 = Real('u1_attacked_9')
u2_9 = Real('u2_9')
u2_attacked_9 = Real('u2_attacked_9')
r_9 = Real('r_9')
y1_10 = Real('y1_10')
r1_10 = Real('r1_10')
rabs1_10 = Real('rabs1_10')
y2_10 = Real('y2_10')
r2_10 = Real('r2_10')
rabs2_10 = Real('rabs2_10')
x1_10 = Real('x1_10')
z1_10 = Real('z1_10')
x1_abs_10 = Real('x1_abs_10')
x2_10 = Real('x2_10')
z2_10 = Real('z2_10')
x2_abs_10 = Real('x2_abs_10')
u1_10 = Real('u1_10')
u1_attacked_10 = Real('u1_attacked_10')
u2_10 = Real('u2_10')
u2_attacked_10 = Real('u2_attacked_10')
r_10 = Real('r_10')

s.add(u1_0 == 0)
s.add(u2_0 == 0)
s.add(x1_0 == 0)
s.add(z1_0 == 0)
s.add(x1_abs_0 == 0)
s.add(x2_0 == 0)
s.add(z2_0 == 0)
s.add(x2_abs_0 == 0)

# pattern = 1
s.add(u1_0 ==  - (2.9846*z1_0) - (-4.9827*z2_0))
s.add(u2_0 ==  - (6.9635*z1_0) - (-6.9599*z2_0))
s.add(u1_attacked_0 == u1_0)
s.add(u2_attacked_0 == u2_0)
s.add(y1_0 ==  + (0.8*x1_0) + (2.4*x2_0) + (0*u1_0) + (0*u2_0))
s.add(y2_0 ==  + (1.6*x1_0) + (0.8*x2_0) + (0*u1_0) + (0*u2_0))
s.add(r1_0 == y1_0 - (0.8*z1_0) - (2.4*z2_0) - (0*u1_attacked_0) - (0*u2_attacked_0))
s.add(r2_0 == y2_0 - (1.6*z1_0) - (0.8*z2_0) - (0*u1_attacked_0) - (0*u2_attacked_0))
s.add(rabs1_0 == If(r1_0<0,(-1)*r1_0,r1_0))
s.add(rabs2_0 == If(r2_0<0,(-1)*r2_0,r2_0))
s.add(r_0 ==rabs1_0 +rabs2_0 )
s.add(r_0<0.03)
s.add(z1_1 ==  (-1*z1_0) + (-3*z2_0) + (2*u1_0) + (-1*u2_0) + (-1.1751*r1_0) + (-0.1412*r2_0) )
s.add(z2_1 ==  (3*z1_0) + (-5*z2_0) + (1*u1_0) + (0*u2_0) + (-2.6599*r1_0) + (2.2549*r2_0) )
s.add(x1_1 ==  (-1*x1_0) + (-3*x2_0) + (2*u1_attacked_0) + (-1*u2_attacked_0) )
s.add(x2_1 ==  (3*x1_0) + (-5*x2_0) + (1*u1_attacked_0) + (0*u2_attacked_0) )
# pattern = 0
s.add(u1_1 == u1_0)
s.add(u1_attacked_1 == u1_attacked_0)
s.add(u2_1 == u2_0)
s.add(u2_attacked_1 == u2_attacked_0)
s.add(r1_1 == 0)
s.add(r2_1 == 0)
s.add(z1_2 ==  (-1*z1_1) + (-3*z2_1) + (2*u1_1) + (-1*u2_1) + (-1.1751*r1_1) + (-0.1412*r2_1) )
s.add(z2_2 ==  (3*z1_1) + (-5*z2_1) + (1*u1_1) + (0*u2_1) + (-2.6599*r1_1) + (2.2549*r2_1) )
s.add(x1_2 ==  (-1*x1_1) + (-3*x2_1) + (2*u1_attacked_1) + (-1*u2_attacked_1) )
s.add(x2_2 ==  (3*x1_1) + (-5*x2_1) + (1*u1_attacked_1) + (0*u2_attacked_1) )
# pattern = 1
s.add(u1_2 ==  - (2.9846*z1_2) - (-4.9827*z2_2))
s.add(u2_2 ==  - (6.9635*z1_2) - (-6.9599*z2_2))
s.add(u1_attacked_2 == u1_2)
s.add(u2_attacked_2 == u2_2)
s.add(y1_2 ==  + (0.8*x1_2) + (2.4*x2_2) + (0*u1_2) + (0*u2_2))
s.add(y2_2 ==  + (1.6*x1_2) + (0.8*x2_2) + (0*u1_2) + (0*u2_2))
s.add(r1_2 == y1_2 - (0.8*z1_2) - (2.4*z2_2) - (0*u1_attacked_2) - (0*u2_attacked_2))
s.add(r2_2 == y2_2 - (1.6*z1_2) - (0.8*z2_2) - (0*u1_attacked_2) - (0*u2_attacked_2))
s.add(rabs1_2 == If(r1_2<0,(-1)*r1_2,r1_2))
s.add(rabs2_2 == If(r2_2<0,(-1)*r2_2,r2_2))
s.add(r_2 ==rabs1_2 +rabs2_2 )
s.add(r_2<0.03)
s.add(z1_3 ==  (-1*z1_2) + (-3*z2_2) + (2*u1_2) + (-1*u2_2) + (-1.1751*r1_2) + (-0.1412*r2_2) )
s.add(z2_3 ==  (3*z1_2) + (-5*z2_2) + (1*u1_2) + (0*u2_2) + (-2.6599*r1_2) + (2.2549*r2_2) )
s.add(x1_3 ==  (-1*x1_2) + (-3*x2_2) + (2*u1_attacked_2) + (-1*u2_attacked_2) )
s.add(x2_3 ==  (3*x1_2) + (-5*x2_2) + (1*u1_attacked_2) + (0*u2_attacked_2) )
# pattern = 1
s.add(u1_3 ==  - (2.9846*z1_3) - (-4.9827*z2_3))
s.add(u2_3 ==  - (6.9635*z1_3) - (-6.9599*z2_3))
s.add(u1_attacked_3 == u1_3)
s.add(u2_attacked_3 == u2_3)
s.add(y1_3 ==  + (0.8*x1_3) + (2.4*x2_3) + (0*u1_3) + (0*u2_3))
s.add(y2_3 ==  + (1.6*x1_3) + (0.8*x2_3) + (0*u1_3) + (0*u2_3))
s.add(r1_3 == y1_3 - (0.8*z1_3) - (2.4*z2_3) - (0*u1_attacked_3) - (0*u2_attacked_3))
s.add(r2_3 == y2_3 - (1.6*z1_3) - (0.8*z2_3) - (0*u1_attacked_3) - (0*u2_attacked_3))
s.add(rabs1_3 == If(r1_3<0,(-1)*r1_3,r1_3))
s.add(rabs2_3 == If(r2_3<0,(-1)*r2_3,r2_3))
s.add(r_3 ==rabs1_3 +rabs2_3 )
s.add(r_3<0.03)
s.add(z1_4 ==  (-1*z1_3) + (-3*z2_3) + (2*u1_3) + (-1*u2_3) + (-1.1751*r1_3) + (-0.1412*r2_3) )
s.add(z2_4 ==  (3*z1_3) + (-5*z2_3) + (1*u1_3) + (0*u2_3) + (-2.6599*r1_3) + (2.2549*r2_3) )
s.add(x1_4 ==  (-1*x1_3) + (-3*x2_3) + (2*u1_attacked_3) + (-1*u2_attacked_3) )
s.add(x2_4 ==  (3*x1_3) + (-5*x2_3) + (1*u1_attacked_3) + (0*u2_attacked_3) )
# pattern = 0
s.add(u1_4 == u1_3)
s.add(u1_attacked_4 == u1_attacked_3)
s.add(u2_4 == u2_3)
s.add(u2_attacked_4 == u2_attacked_3)
s.add(r1_4 == 0)
s.add(r2_4 == 0)
s.add(z1_5 ==  (-1*z1_4) + (-3*z2_4) + (2*u1_4) + (-1*u2_4) + (-1.1751*r1_4) + (-0.1412*r2_4) )
s.add(z2_5 ==  (3*z1_4) + (-5*z2_4) + (1*u1_4) + (0*u2_4) + (-2.6599*r1_4) + (2.2549*r2_4) )
s.add(x1_5 ==  (-1*x1_4) + (-3*x2_4) + (2*u1_attacked_4) + (-1*u2_attacked_4) )
s.add(x2_5 ==  (3*x1_4) + (-5*x2_4) + (1*u1_attacked_4) + (0*u2_attacked_4) )
# pattern = 1
s.add(u1_5 ==  - (2.9846*z1_5) - (-4.9827*z2_5))
s.add(u2_5 ==  - (6.9635*z1_5) - (-6.9599*z2_5))
s.add(u1_attacked_5 == u1_5)
s.add(u2_attacked_5 == u2_5)
s.add(y1_5 ==  + (0.8*x1_5) + (2.4*x2_5) + (0*u1_5) + (0*u2_5))
s.add(y2_5 ==  + (1.6*x1_5) + (0.8*x2_5) + (0*u1_5) + (0*u2_5))
s.add(r1_5 == y1_5 - (0.8*z1_5) - (2.4*z2_5) - (0*u1_attacked_5) - (0*u2_attacked_5))
s.add(r2_5 == y2_5 - (1.6*z1_5) - (0.8*z2_5) - (0*u1_attacked_5) - (0*u2_attacked_5))
s.add(rabs1_5 == If(r1_5<0,(-1)*r1_5,r1_5))
s.add(rabs2_5 == If(r2_5<0,(-1)*r2_5,r2_5))
s.add(r_5 ==rabs1_5 +rabs2_5 )
s.add(r_5<0.03)
s.add(z1_6 ==  (-1*z1_5) + (-3*z2_5) + (2*u1_5) + (-1*u2_5) + (-1.1751*r1_5) + (-0.1412*r2_5) )
s.add(z2_6 ==  (3*z1_5) + (-5*z2_5) + (1*u1_5) + (0*u2_5) + (-2.6599*r1_5) + (2.2549*r2_5) )
s.add(x1_6 ==  (-1*x1_5) + (-3*x2_5) + (2*u1_attacked_5) + (-1*u2_attacked_5) )
s.add(x2_6 ==  (3*x1_5) + (-5*x2_5) + (1*u1_attacked_5) + (0*u2_attacked_5) )
# pattern = 1
s.add(u1_6 ==  - (2.9846*z1_6) - (-4.9827*z2_6))
s.add(u2_6 ==  - (6.9635*z1_6) - (-6.9599*z2_6))
s.add(u1_attacked_6 == u1_6)
s.add(u2_attacked_6 == u2_6)
s.add(y1_6 ==  + (0.8*x1_6) + (2.4*x2_6) + (0*u1_6) + (0*u2_6))
s.add(y2_6 ==  + (1.6*x1_6) + (0.8*x2_6) + (0*u1_6) + (0*u2_6))
s.add(r1_6 == y1_6 - (0.8*z1_6) - (2.4*z2_6) - (0*u1_attacked_6) - (0*u2_attacked_6))
s.add(r2_6 == y2_6 - (1.6*z1_6) - (0.8*z2_6) - (0*u1_attacked_6) - (0*u2_attacked_6))
s.add(rabs1_6 == If(r1_6<0,(-1)*r1_6,r1_6))
s.add(rabs2_6 == If(r2_6<0,(-1)*r2_6,r2_6))
s.add(r_6 ==rabs1_6 +rabs2_6 )
s.add(r_6<0.03)
s.add(z1_7 ==  (-1*z1_6) + (-3*z2_6) + (2*u1_6) + (-1*u2_6) + (-1.1751*r1_6) + (-0.1412*r2_6) )
s.add(z2_7 ==  (3*z1_6) + (-5*z2_6) + (1*u1_6) + (0*u2_6) + (-2.6599*r1_6) + (2.2549*r2_6) )
s.add(x1_7 ==  (-1*x1_6) + (-3*x2_6) + (2*u1_attacked_6) + (-1*u2_attacked_6) )
s.add(x2_7 ==  (3*x1_6) + (-5*x2_6) + (1*u1_attacked_6) + (0*u2_attacked_6) )
# pattern = 0
s.add(u1_7 == u1_6)
s.add(u1_attacked_7 == u1_attacked_6)
s.add(u2_7 == u2_6)
s.add(u2_attacked_7 == u2_attacked_6)
s.add(r1_7 == 0)
s.add(r2_7 == 0)
s.add(z1_8 ==  (-1*z1_7) + (-3*z2_7) + (2*u1_7) + (-1*u2_7) + (-1.1751*r1_7) + (-0.1412*r2_7) )
s.add(z2_8 ==  (3*z1_7) + (-5*z2_7) + (1*u1_7) + (0*u2_7) + (-2.6599*r1_7) + (2.2549*r2_7) )
s.add(x1_8 ==  (-1*x1_7) + (-3*x2_7) + (2*u1_attacked_7) + (-1*u2_attacked_7) )
s.add(x2_8 ==  (3*x1_7) + (-5*x2_7) + (1*u1_attacked_7) + (0*u2_attacked_7) )
# pattern = 1
s.add(u1_8 ==  - (2.9846*z1_8) - (-4.9827*z2_8))
s.add(u2_8 ==  - (6.9635*z1_8) - (-6.9599*z2_8))
s.add(u1_attacked_8 == u1_8)
s.add(u2_attacked_8 == u2_8)
s.add(y1_8 ==  + (0.8*x1_8) + (2.4*x2_8) + (0*u1_8) + (0*u2_8))
s.add(y2_8 ==  + (1.6*x1_8) + (0.8*x2_8) + (0*u1_8) + (0*u2_8))
s.add(r1_8 == y1_8 - (0.8*z1_8) - (2.4*z2_8) - (0*u1_attacked_8) - (0*u2_attacked_8))
s.add(r2_8 == y2_8 - (1.6*z1_8) - (0.8*z2_8) - (0*u1_attacked_8) - (0*u2_attacked_8))
s.add(rabs1_8 == If(r1_8<0,(-1)*r1_8,r1_8))
s.add(rabs2_8 == If(r2_8<0,(-1)*r2_8,r2_8))
s.add(r_8 ==rabs1_8 +rabs2_8 )
s.add(r_8<0.03)
s.add(z1_9 ==  (-1*z1_8) + (-3*z2_8) + (2*u1_8) + (-1*u2_8) + (-1.1751*r1_8) + (-0.1412*r2_8) )
s.add(z2_9 ==  (3*z1_8) + (-5*z2_8) + (1*u1_8) + (0*u2_8) + (-2.6599*r1_8) + (2.2549*r2_8) )
s.add(x1_9 ==  (-1*x1_8) + (-3*x2_8) + (2*u1_attacked_8) + (-1*u2_attacked_8) )
s.add(x2_9 ==  (3*x1_8) + (-5*x2_8) + (1*u1_attacked_8) + (0*u2_attacked_8) )
# pattern = 1
s.add(u1_9 ==  - (2.9846*z1_9) - (-4.9827*z2_9))
s.add(u2_9 ==  - (6.9635*z1_9) - (-6.9599*z2_9))
s.add(u1_attacked_9 == u1_9)
s.add(u2_attacked_9 == u2_9)
s.add(y1_9 ==  + (0.8*x1_9) + (2.4*x2_9) + (0*u1_9) + (0*u2_9))
s.add(y2_9 ==  + (1.6*x1_9) + (0.8*x2_9) + (0*u1_9) + (0*u2_9))
s.add(r1_9 == y1_9 - (0.8*z1_9) - (2.4*z2_9) - (0*u1_attacked_9) - (0*u2_attacked_9))
s.add(r2_9 == y2_9 - (1.6*z1_9) - (0.8*z2_9) - (0*u1_attacked_9) - (0*u2_attacked_9))
s.add(rabs1_9 == If(r1_9<0,(-1)*r1_9,r1_9))
s.add(rabs2_9 == If(r2_9<0,(-1)*r2_9,r2_9))
s.add(r_9 ==rabs1_9 +rabs2_9 )
s.add(r_9<0.03)
s.add(z1_10 ==  (-1*z1_9) + (-3*z2_9) + (2*u1_9) + (-1*u2_9) + (-1.1751*r1_9) + (-0.1412*r2_9) )
s.add(z2_10 ==  (3*z1_9) + (-5*z2_9) + (1*u1_9) + (0*u2_9) + (-2.6599*r1_9) + (2.2549*r2_9) )
s.add(x1_10 ==  (-1*x1_9) + (-3*x2_9) + (2*u1_attacked_9) + (-1*u2_attacked_9) )
s.add(x2_10 ==  (3*x1_9) + (-5*x2_9) + (1*u1_attacked_9) + (0*u2_attacked_9) )
s.add(Or(x1_abs_0>0.05,x1_abs_1>0.05,x1_abs_2>0.05,x1_abs_3>0.05,x1_abs_4>0.05,x1_abs_5>0.05,x1_abs_6>0.05,x1_abs_7>0.05,x1_abs_8>0.05,x1_abs_9>0.05,x2_abs_0>0.15,x2_abs_1>0.15,x2_abs_2>0.15,x2_abs_3>0.15,x2_abs_4>0.15,x2_abs_5>0.15,x2_abs_6>0.15,x2_abs_7>0.15,x2_abs_8>0.15,x2_abs_9>0.15))

if s.check() != sat:
	print(s.check())
	isSat = 0
else:
	print( "sat")
	print(s.check())
	isSat = 1
	m = s.model()
	for d in m.decls():
		print ("%s = %s" % (d.name(), m[d]))
if isSat==1:
	f0 = open("../results/z3/powergrid/powergrid.z3result", "w+")
	f0.write("1")
	f0.close()
