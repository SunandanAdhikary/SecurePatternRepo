from z3 import *
import math
import numpy as np

s = Solver()
set_option(rational_to_decimal=True)

x1_0 = Real('x1_0')
z1_0 = Real('z1_0')
xabs1_0 = Real('xabs1_0')
x2_0 = Real('x2_0')
z2_0 = Real('z2_0')
xabs2_0 = Real('xabs2_0')
y1_0 = Real('y1_0')
r1_0 = Real('r1_0')
rabs1_0 = Real('rabs1_0')
y2_0 = Real('y2_0')
r2_0 = Real('r2_0')
rabs2_0 = Real('rabs2_0')
u1_0 = Real('u1_0')
r_0 = Real('r_0')

x1_1 = Real('x1_1')
z1_1 = Real('z1_1')
xabs1_1 = Real('xabs1_1')
x2_1 = Real('x2_1')
z2_1 = Real('z2_1')
xabs2_1 = Real('xabs2_1')
y1_1 = Real('y1_1')
r1_1 = Real('r1_1')
rabs1_1 = Real('rabs1_1')
y2_1 = Real('y2_1')
r2_1 = Real('r2_1')
rabs2_1 = Real('rabs2_1')
u1_1 = Real('u1_1')
r_1 = Real('r_1')

x1_2 = Real('x1_2')
z1_2 = Real('z1_2')
xabs1_2 = Real('xabs1_2')
x2_2 = Real('x2_2')
z2_2 = Real('z2_2')
xabs2_2 = Real('xabs2_2')
y1_2 = Real('y1_2')
r1_2 = Real('r1_2')
rabs1_2 = Real('rabs1_2')
y2_2 = Real('y2_2')
r2_2 = Real('r2_2')
rabs2_2 = Real('rabs2_2')
u1_2 = Real('u1_2')
r_2 = Real('r_2')

x1_3 = Real('x1_3')
z1_3 = Real('z1_3')
xabs1_3 = Real('xabs1_3')
x2_3 = Real('x2_3')
z2_3 = Real('z2_3')
xabs2_3 = Real('xabs2_3')
y1_3 = Real('y1_3')
r1_3 = Real('r1_3')
rabs1_3 = Real('rabs1_3')
y2_3 = Real('y2_3')
r2_3 = Real('r2_3')
rabs2_3 = Real('rabs2_3')
u1_3 = Real('u1_3')
r_3 = Real('r_3')

x1_4 = Real('x1_4')
z1_4 = Real('z1_4')
xabs1_4 = Real('xabs1_4')
x2_4 = Real('x2_4')
z2_4 = Real('z2_4')
xabs2_4 = Real('xabs2_4')
y1_4 = Real('y1_4')
r1_4 = Real('r1_4')
rabs1_4 = Real('rabs1_4')
y2_4 = Real('y2_4')
r2_4 = Real('r2_4')
rabs2_4 = Real('rabs2_4')
u1_4 = Real('u1_4')
r_4 = Real('r_4')

x1_5 = Real('x1_5')
z1_5 = Real('z1_5')
xabs1_5 = Real('xabs1_5')
x2_5 = Real('x2_5')
z2_5 = Real('z2_5')
xabs2_5 = Real('xabs2_5')
y1_5 = Real('y1_5')
r1_5 = Real('r1_5')
rabs1_5 = Real('rabs1_5')
y2_5 = Real('y2_5')
r2_5 = Real('r2_5')
rabs2_5 = Real('rabs2_5')
u1_5 = Real('u1_5')
r_5 = Real('r_5')

x1_6 = Real('x1_6')
z1_6 = Real('z1_6')
xabs1_6 = Real('xabs1_6')
x2_6 = Real('x2_6')
z2_6 = Real('z2_6')
xabs2_6 = Real('xabs2_6')
y1_6 = Real('y1_6')
r1_6 = Real('r1_6')
rabs1_6 = Real('rabs1_6')
y2_6 = Real('y2_6')
r2_6 = Real('r2_6')
rabs2_6 = Real('rabs2_6')
u1_6 = Real('u1_6')
r_6 = Real('r_6')

s.add(Or(And(x1_0 < 0.1,x1_0 > 0.01),And(x1_0 > -0.1,x1_0 < -0.01)))
s.add(xabs1_0 == If(x1_0<0,(-1)*x1_0,x1_0))
s.add(Or(And(x2_0 < 0.05,x2_0 > 0.005),And(x2_0 > -0.05,x2_0 < -0.005)))
s.add(xabs2_0 == If(x2_0<0,(-1)*x2_0,x2_0))
s.add(y1_0 == 0)
s.add(y2_0 == 0)
s.add(u1_0 == 0)

# pattern = 1
s.add(r1_0 == y1_0 - (1*z1_0) - (0*z2_0) - (0*u1_0))
s.add(r2_0 == y2_0 - (0*z1_0) - (1*z2_0) - (0*u1_0))
s.add(rabs1_0 == If(r1_0<0,(-1)*r1_0,r1_0))
s.add(rabs2_0 == If(r2_0<0,(-1)*r2_0,r2_0))
s.add(r_0 ==rabs1_0 +rabs2_0 )
s.add(r_0<0.03)
s.add(z1_1 ==  (0.66*z1_0) + (0.53*z2_0) + (0.34*u1_0) + (0.36*r1_0) + (0.27*r2_0) )
s.add(z2_1 ==  (-0.53*z1_0) + (0.13*z2_0) + (0.53*u1_0) + (-0.31*r1_0) + (0.08*r2_0) )
s.add(x1_1 ==  (0.66*x1_0) + (0.53*x2_0) + (0.34*u1_0) )
s.add(x2_1 ==  (-0.53*x1_0) + (0.13*x2_0) + (0.53*u1_0) )
s.add(xabs1_1 == If(x1_1<0,(-1)*x1_1,x1_1))
s.add(xabs2_1 == If(x2_1<0,(-1)*x2_1,x2_1))
s.add(u1_1 ==  - (0.0556*z1_1) - (0.3306*z2_1))
s.add(y1_1 ==  + (1*x1_1) + (0*x2_1) + (0*u1_1))
s.add(y2_1 ==  + (0*x1_1) + (1*x2_1) + (0*u1_1))
# pattern = 1
s.add(r1_1 == y1_1 - (1*z1_1) - (0*z2_1) - (0*u1_1))
s.add(r2_1 == y2_1 - (0*z1_1) - (1*z2_1) - (0*u1_1))
s.add(rabs1_1 == If(r1_1<0,(-1)*r1_1,r1_1))
s.add(rabs2_1 == If(r2_1<0,(-1)*r2_1,r2_1))
s.add(r_1 ==rabs1_1 +rabs2_1 )
s.add(z1_2 ==  (0.66*z1_1) + (0.53*z2_1) + (0.34*u1_1) + (0.36*r1_1) + (0.27*r2_1) )
s.add(z2_2 ==  (-0.53*z1_1) + (0.13*z2_1) + (0.53*u1_1) + (-0.31*r1_1) + (0.08*r2_1) )
s.add(x1_2 ==  (0.66*x1_1) + (0.53*x2_1) + (0.34*u1_1) )
s.add(x2_2 ==  (-0.53*x1_1) + (0.13*x2_1) + (0.53*u1_1) )
s.add(xabs1_2 == If(x1_2<0,(-1)*x1_2,x1_2))
s.add(xabs2_2 == If(x2_2<0,(-1)*x2_2,x2_2))
s.add(u1_2 ==  - (0.0556*z1_2) - (0.3306*z2_2))
s.add(y1_2 ==  + (1*x1_2) + (0*x2_2) + (0*u1_2))
s.add(y2_2 ==  + (0*x1_2) + (1*x2_2) + (0*u1_2))
# pattern = 1
s.add(r1_2 == y1_2 - (1*z1_2) - (0*z2_2) - (0*u1_2))
s.add(r2_2 == y2_2 - (0*z1_2) - (1*z2_2) - (0*u1_2))
s.add(rabs1_2 == If(r1_2<0,(-1)*r1_2,r1_2))
s.add(rabs2_2 == If(r2_2<0,(-1)*r2_2,r2_2))
s.add(r_2 ==rabs1_2 +rabs2_2 )
s.add(z1_3 ==  (0.66*z1_2) + (0.53*z2_2) + (0.34*u1_2) + (0.36*r1_2) + (0.27*r2_2) )
s.add(z2_3 ==  (-0.53*z1_2) + (0.13*z2_2) + (0.53*u1_2) + (-0.31*r1_2) + (0.08*r2_2) )
s.add(x1_3 ==  (0.66*x1_2) + (0.53*x2_2) + (0.34*u1_2) )
s.add(x2_3 ==  (-0.53*x1_2) + (0.13*x2_2) + (0.53*u1_2) )
s.add(xabs1_3 == If(x1_3<0,(-1)*x1_3,x1_3))
s.add(xabs2_3 == If(x2_3<0,(-1)*x2_3,x2_3))
s.add(u1_3 ==  - (0.0556*z1_3) - (0.3306*z2_3))
s.add(y1_3 ==  + (1*x1_3) + (0*x2_3) + (0*u1_3))
s.add(y2_3 ==  + (0*x1_3) + (1*x2_3) + (0*u1_3))
# pattern = 1
s.add(r1_3 == y1_3 - (1*z1_3) - (0*z2_3) - (0*u1_3))
s.add(r2_3 == y2_3 - (0*z1_3) - (1*z2_3) - (0*u1_3))
s.add(rabs1_3 == If(r1_3<0,(-1)*r1_3,r1_3))
s.add(rabs2_3 == If(r2_3<0,(-1)*r2_3,r2_3))
s.add(r_3 ==rabs1_3 +rabs2_3 )
s.add(z1_4 ==  (0.66*z1_3) + (0.53*z2_3) + (0.34*u1_3) + (0.36*r1_3) + (0.27*r2_3) )
s.add(z2_4 ==  (-0.53*z1_3) + (0.13*z2_3) + (0.53*u1_3) + (-0.31*r1_3) + (0.08*r2_3) )
s.add(x1_4 ==  (0.66*x1_3) + (0.53*x2_3) + (0.34*u1_3) )
s.add(x2_4 ==  (-0.53*x1_3) + (0.13*x2_3) + (0.53*u1_3) )
s.add(xabs1_4 == If(x1_4<0,(-1)*x1_4,x1_4))
s.add(xabs2_4 == If(x2_4<0,(-1)*x2_4,x2_4))
s.add(u1_4 ==  - (0.0556*z1_4) - (0.3306*z2_4))
s.add(y1_4 ==  + (1*x1_4) + (0*x2_4) + (0*u1_4))
s.add(y2_4 ==  + (0*x1_4) + (1*x2_4) + (0*u1_4))
# pattern = 0
s.add(r1_4 == y1_4 - (1*z1_4) - (0*z2_4) - (0*u1_4))
s.add(r2_4 == y2_4 - (0*z1_4) - (1*z2_4) - (0*u1_4))
s.add(rabs1_4 == If(r1_4<0,(-1)*r1_4,r1_4))
s.add(rabs2_4 == If(r2_4<0,(-1)*r2_4,r2_4))
s.add(r_4 ==rabs1_4 +rabs2_4 )
s.add(z1_5 ==  (0.66*z1_4) + (0.53*z2_4) + (0.34*u1_4) + (0.36*r1_4) + (0.27*r2_4) )
s.add(z2_5 ==  (-0.53*z1_4) + (0.13*z2_4) + (0.53*u1_4) + (-0.31*r1_4) + (0.08*r2_4) )
s.add(x1_5 ==  (0.66*x1_4) + (0.53*x2_4) + (0.34*u1_4) )
s.add(x2_5 ==  (-0.53*x1_4) + (0.13*x2_4) + (0.53*u1_4) )
s.add(xabs1_5 == If(x1_5<0,(-1)*x1_5,x1_5))
s.add(xabs2_5 == If(x2_5<0,(-1)*x2_5,x2_5))
s.add(u1_5 == u1_4)
s.add(y1_5 ==  + (1*x1_5) + (0*x2_5) + (0*u1_5))
s.add(y2_5 ==  + (0*x1_5) + (1*x2_5) + (0*u1_5))
# pattern = 0
s.add(r1_5 == y1_5 - (1*z1_5) - (0*z2_5) - (0*u1_5))
s.add(r2_5 == y2_5 - (0*z1_5) - (1*z2_5) - (0*u1_5))
s.add(rabs1_5 == If(r1_5<0,(-1)*r1_5,r1_5))
s.add(rabs2_5 == If(r2_5<0,(-1)*r2_5,r2_5))
s.add(r_5 ==rabs1_5 +rabs2_5 )
s.add(z1_6 ==  (0.66*z1_5) + (0.53*z2_5) + (0.34*u1_5) + (0.36*r1_5) + (0.27*r2_5) )
s.add(z2_6 ==  (-0.53*z1_5) + (0.13*z2_5) + (0.53*u1_5) + (-0.31*r1_5) + (0.08*r2_5) )
s.add(x1_6 ==  (0.66*x1_5) + (0.53*x2_5) + (0.34*u1_5) )
s.add(x2_6 ==  (-0.53*x1_5) + (0.13*x2_5) + (0.53*u1_5) )
s.add(xabs1_6 == If(x1_6<0,(-1)*x1_6,x1_6))
s.add(xabs2_6 == If(x2_6<0,(-1)*x2_6,x2_6))
s.add(u1_6 == u1_5)
s.add(y1_6 ==  + (1*x1_6) + (0*x2_6) + (0*u1_6))
s.add(y2_6 ==  + (0*x1_6) + (1*x2_6) + (0*u1_6))
s.add(Or((xabs1_6>0.01),(xabs2_6>0.005)))

if s.check() != sat:
	print(s.check())
	isSat = 0
else:
	print(s.check())
	isSat = 1
if isSat==0:
	f0 = open("../results/z3/powersystem/powersystem.z3result", "w+")
	f0.write("0")
	f0.close()
