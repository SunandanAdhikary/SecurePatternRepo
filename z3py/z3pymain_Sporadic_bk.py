# Controller type: PID
import os
import numpy as np
import errno
############################## inputs ############################
modelName = "powersystem"

################## attack length and position ###################
attackLen = 1
secPeriod = 5
pattern = 1
offset = 4
start = 0
isSat = 0
innerCircleDepth = 0.1
isDelayed = 0
####################################################################
if modelName == "tempControl":
    modelName= "tempControl"
    A= np.matrix('0.94648514795348381856143760160194 0.0018971440127071483982418298452899;0 0.000000000013887943864964020896356969649573')
    B= np.matrix('-0.046752721484125708828472056666214;-0.99999999998611222018496391683584')
    C= np.matrix('1 0')
    D= np.matrix('0')
    Gain= np.matrix('-0.3712408426327057364702000086254 -0.0007441187601164687840174516431091')
    L= np.matrix('0.60711740001928504728567759229918;0.39288259998275032458536770718638')
    safex = [30,30]
    tolerance = [1,1]
    th = 0.00001
elif modelName == "powersystem":
    A= np.matrix('0.66 0.53;-0.53 0.13')
    B= np.matrix('0.34;0.53')
    C= np.matrix('1 0;0 1')
    D= np.matrix('0;0')
    Gain= np.matrix('0.0556 0.3306')
    L= np.matrix('0.36 0.27;  -0.31 0.08')
    safex = [0.1,0.05]
    tolerance = [0.001,0.0001]
    # initialRange = np.matrix('0 0.35;-4 4')
    th = 0.03
elif modelName == "plant":
    A= np.matrix('2.6221    0.3197    1.8335   -1.0664; -0.2381    0.1872   -0.1361    0.2017; 0.1612    0.7888    0.2859    0.6064;-0.1035    0.7641    0.0886    0.7360')
    B= np.matrix('0.4654   -1.5495; 1.3138    0.0851; 2.0549   -0.6730; 2.0227   -0.1597')
    C= np.matrix('1     0     1    -1;0     1     0     0')
    D= np.matrix('0 0;0 0')
    Gain= np.matrix('-0.2580    0.3159   -0.1087    0.3982; -1.6195   -0.1314   -1.1232    0.7073')
    L= np.matrix('2.4701   -0.0499; -0.2144    0.0224; 0.2327    0.0946; -0.0192    0.1004')
    safex = [0.01,0.01,0.01,0.01]
    tolerance = [0.0001,0.0001,0.0001,0.0001]
    th = 0.0001
elif modelName == "powergrid":
    A= np.matrix('-1 -3;3 -5')
    B= np.matrix('2 -1;1 0')
    C= np.matrix('0.8 2.4;1.6 0.8')
    D= np.matrix('0 0; 0 0')
    Gain= np.matrix('2.9846   -4.9827;6.9635   -6.9599')
    L= np.matrix('-1.1751   -0.1412;-2.6599    2.2549')
    safex = [0.1,0.2]
    tolerance = [0.001,0.001]
    th = 0.01

################## creating the path to save results #################
path="../results/z3/"+modelName+"/"
try:
    os.makedirs(path)
except OSError as err:
    if err.errno!= errno.EEXIST:
        raise
#####################################################################
u_count=B.shape[1]
x_count=A.shape[1]
y_count=C.shape[0]

######### Configure which sensor/control input to attack ##########
u_attack_map = np.zeros(u_count,dtype=float)
y_attack_map = np.zeros(y_count,dtype=float)
u_attack_map[0] = 1
y_attack_map[0] = 1

######### Configure which sensor/control input to attack ##########
initialRange = np.zeros(shape=(x_count,2), dtype=float)
for i in range(x_count):
    initialRange[i,0] = (-1)*safex[i]*innerCircleDepth
    initialRange[i,1] = safex[i]*innerCircleDepth

#Compute pattern length
patternLen=len(str(pattern))

#Compute pattern array
patternArray = np.zeros((patternLen), dtype=int)
patternTemp = pattern
i = patternLen-1
while patternTemp>0:
    patternArray[i] = patternTemp%10
    patternTemp=patternTemp//10
    i = i-1

f0 = open(path+modelName+"_sporadic.z3result", "w+")
f0.write("0")
f0.close()

print("Finding minimum attack length for "+str(modelName)+" and pattern "+str(pattern)+" with sporadic security of period "+str(secPeriod))

while isSat == 0:  
    print("attack length:"+str(attackLen)+"\n")
    index = start
    while (index<patternLen) and (isSat == 0):
        # create drop pattern
        K = index + attackLen + offset
        dropPattern = np.ones((K), dtype=int)
        j=0
        if pattern!=1:
            for i in range(K):
                dropPattern[i] = patternArray[j]
                j = j + 1
                if j == patternLen:
                    j = 0
        print("drop pattern:")
        print(dropPattern)
        print("\n")
        fileName = modelName + "_sporadic_" + str(th) + "_" +str(index)+"_"+str(attackLen)+"_"+str(K)+"_"+str(pattern)+"_"+str(secPeriod)+".py"
        f = open(path+fileName, "w+")
        f.write("from z3 import *\n")
        f.write("import math\n")
        f.write("import numpy as np\n\n")
        f.write("s = Solver()\n")
        # f.write("set_option(precision=40)\n")
        f.write("set_option(rational_to_decimal=True)\n")

        for varcount in range(1,x_count+1):
            f.write("xabs"+str(varcount)+" = np.zeros("+str(K+1)+", dtype=float)\n")
            f.write("x"+str(varcount)+" = np.zeros("+str(K+1)+", dtype=float)\n")
            f.write("z"+str(varcount)+" = np.zeros("+str(K+1)+", dtype=float)\n")
        for varcount in range(1,y_count+1):
            f.write("y"+str(varcount)+" = np.zeros("+str(K+1)+", dtype=float)\n")
            f.write("attackOnY"+str(varcount)+" = np.zeros("+str(K+1)+", dtype=float)\n")
            f.write("r"+str(varcount)+" = np.zeros("+str(K+1)+", dtype=float)\n")
        for varcount in range(1,u_count+1):
            f.write("u"+str(varcount)+" = np.zeros("+str(K+1)+", dtype=float)\n")
            f.write("uattacked"+str(varcount)+" = np.zeros("+str(K+1)+", dtype=float)\n")
            f.write("attackOnU"+str(varcount)+" = np.zeros("+str(K+1)+", dtype=float)\n")
        f.write("r = np.zeros("+str(K+1)+", dtype=float)\n\n")
 
        for i in range(K+1):
            decl=""
            for varcount in range(1,y_count+1):
                decl+="y"+str(varcount)+"_"+str(i)+" = Real('y"+str(varcount)+"_"+str(i)+"')\n"
                decl+="r"+str(varcount)+"_"+str(i)+" = Real('r"+str(varcount)+"_"+str(i)+"')\n"
                decl+="rabs"+str(varcount)+"_"+str(i)+" = Real('rabs"+str(varcount)+"_"+str(i)+"')\n"

            for varcount in range(1,x_count+1):
                decl+="x"+str(varcount)+"_"+str(i)+" = Real('x"+str(varcount)+"_"+str(i)+"')\n"
                decl+="z"+str(varcount)+"_"+str(i)+" = Real('z"+str(varcount)+"_"+str(i)+"')\n"
                decl+="xabs"+str(varcount)+"_"+str(i)+" = Real('xabs"+str(varcount)+"_"+str(i)+"')\n"

            for varcount in range(1,u_count+1):
                decl+="u"+str(varcount)+"_"+str(i)+" = Real('u"+str(varcount)+"_"+str(i)+"')\n"
                decl+="uattacked"+str(varcount)+"_"+str(i)+" = Real('uattacked"+str(varcount)+"_"+str(i)+"')\n"

            decl+="r_"+str(i)+" = Real('r_"+str(i)+"')\n"
            f.write(decl)
            
        f.write("\n")
        for varcount in range(1,x_count+1):
            f.write("s.add(x"+str(varcount)+"_0 >= "+str(initialRange[varcount-1,0])+")\n")
            f.write("s.add(x"+str(varcount)+"_0 <= "+str(initialRange[varcount-1,1])+")\n")
            f.write("s.add(z"+str(varcount)+"_0 == 0)\n")
            f.write("s.add(xabs"+str(varcount)+"_0 == If(x"+str(varcount)+"_0<0,(-1)*x"+str(varcount)+"_0,x"+str(varcount)+"_0))\n")
        for varcount1 in range(1,y_count+1):
            f.write("s.add(y"+str(varcount1)+"_0 == 0)\n")
        for varcount2 in range(1,u_count+1): 
            f.write("s.add(u"+str(varcount2)+"_0 == 0)\n")
            f.write("s.add(uattacked"+str(varcount2)+"_0 == 0)\n")
        f.write("\n")

        j = 0
        for i in range(K):
            f.write("# pattern = "+str(dropPattern[i])+"\n")

            # Update r
            expr_r=""
            for varcount1 in range(1,y_count+1):
                expr_r+="s.add(r"+str(varcount1)+"_"+str(i)+" == y"+str(varcount1)+"_"+str(i)
                for varcount2 in range(1,x_count+1):
                    expr_r+=" - ("+str(C[varcount1-1,varcount2-1])+"*z"+str(varcount2)+"_"+str(i)+")"
                for varcount3 in range(1,u_count+1):       
                    expr_r+=" - ("+str(D[varcount1-1,varcount3-1])+"*u"+str(varcount3)+"_"+str(i)+")"   
                expr_r+=")\n"
            f.write(expr_r)

            # Compute 1-norm of r
            expr_rabs = ""
            expr_r = "s.add(r_"+str(i)+" ==" 
            for varcount1 in range(1,y_count+1):
                expr_rabs+= "s.add(rabs"+str(varcount1)+"_"+str(i)+" == If(r"+str(varcount1)+"_"+str(i)+"<0,(-1)*r"+str(varcount1)+"_"+str(i)+",r"+str(varcount1)+"_"+str(i)+"))\n"
                expr_r+="rabs"+str(varcount1)+"_"+str(i)+" +"
            expr_r = expr_r[:len(expr_r)-1] 
            expr_r+=")\n"
            f.write(expr_rabs)
            f.write(expr_r)

            # Threshold check
            f.write("s.add(r_{0}<{1})\n".format(i,th))

            # Update x and z
            expr_x=""
            expr_xabs=""
            expr_z=""
            for varcount1 in range(1,x_count+1):
                expr_x+="s.add(x"+str(varcount1)+"_"+str(i+1)+" == "                
                expr_z+="s.add(z"+str(varcount1)+"_"+str(i+1)+" == "
                for varcount2 in range(1,x_count+1):
                    expr_x+=" ("+str(A[varcount1-1,varcount2-1])+"*x"+str(varcount2)+"_"+str(i)+") +"
                    expr_z+=" ("+str(A[varcount1-1,varcount2-1])+"*z"+str(varcount2)+"_"+str(i)+") +"
                for varcount3 in range(1,u_count+1):
                    expr_z+=" ("+str(B[varcount1-1,varcount3-1])+"*u"+str(varcount3)+"_"+str(i)+") +"
                    expr_x+=" ("+str(B[varcount1-1,varcount3-1])+"*uattacked"+str(varcount3)+"_"+str(i)+") +"
                for varcount4 in range(1,y_count+1):
                    expr_z+=" ("+str(L[varcount1-1,varcount4-1])+"*r"+str(varcount4)+"_"+str(i)+") +"
                
                expr_xabs+="s.add(xabs"+str(varcount1)+"_"+str(i+1)+" == If(x"+str(varcount1)+"_"+str(i+1)+"<0,(-1)*x"+str(varcount1)+"_"+str(i+1)+",x"+str(varcount1)+"_"+str(i+1)+"))\n"

                expr_x=expr_x[:len(expr_x)-1] 
                expr_x = expr_x + ")\n"
                expr_z=expr_z[:len(expr_z)-1] 
                expr_z = expr_z + ")\n"            

            f.write(expr_z)
            f.write(expr_x)
            f.write(expr_xabs)            

            # Simulate dropping behavior
            if dropPattern[i]: #If there is a 1 in the pattern
                expr_u=""
                for varcount1 in range(1,u_count+1):
                    expr_u+="s.add(u"+str(varcount1)+"_"+str(i+1)+" == "
                    for varcount2 in range(1,x_count+1):
                        if isDelayed:
                            expr_u+=" - ("+str(Gain[varcount1-1,varcount2-1])+"*z"+str(varcount2)+"_"+str(i)+")"
                        else:
                            expr_u+=" - ("+str(Gain[varcount1-1,varcount2-1])+"*z"+str(varcount2)+"_"+str(i+1)+")"
                    expr_u+=")\n"
                f.write(expr_u)
                if (i == (j+index)) and (i%secPeriod!=0):      # If in this iteration we can give an attack      
                    expr_uatk=""
                    for varcount1 in range(1,u_count+1):
                        f.write("attackOnU"+str(varcount1)+"_"+str(i)+" = Real('attackOnU"+str(varcount1)+"_"+str(i)+"')\n")
                        expr_uatk+="s.add(uattacked"+str(varcount1)+"_"+str(i+1)+" == u"+str(varcount1)+"_"+str(i+1)+"+ ("+str(u_attack_map[varcount1-1])+"*attackOnU"+str(varcount1)+"_"+str(i)+"))\n"
                    f.write(expr_uatk)  

                else: # If attack len exhausted
                    expr_uatk=""
                    for varcount1 in range(1,u_count+1):
                        expr_uatk+="s.add(uattacked"+str(varcount1)+"_"+str(i+1)+" == u"+str(varcount1)+"_"+str(i+1)+")\n"
                    f.write(expr_uatk)
            else:
                expr_u=""
                for varcount1 in range(1,u_count+1):
                    expr_u+="s.add(u"+str(varcount1)+"_"+str(i+1)+" == u"+str(varcount1)+"_"+str(i)+")\n"
                    expr_u+="s.add(uattacked"+str(varcount1)+"_"+str(i+1)+" == uattacked"+str(varcount1)+"_"+str(i)+")\n"
                f.write(expr_u)

            # Update y
            if (i == (j+index)) and (i%secPeriod!=0):
                expr_y=""
                for varcount1 in range(1,y_count+1):
                    f.write("attackOnY"+str(varcount1)+"_"+str(i)+" = Real('attackOnY"+str(varcount1)+"_"+str(i)+"')\n")
                    expr_y+="s.add(y"+str(varcount1)+"_"+str(i+1)+" == ("+str(y_attack_map[varcount1-1])+"*attackOnY"+str(varcount1)+"_"+str(i)+")"
                    for varcount2 in range(1,x_count+1):
                        expr_y+=" + ("+str(C[varcount1-1,varcount2-1])+"*x"+str(varcount2)+"_"+str(i+1)+")"
                    for varcount3 in range(1,u_count+1):
                        expr_y+=" + ("+str(D[varcount1-1,varcount3-1])+"*uattacked"+str(varcount3)+"_"+str(i+1)+")" 
                    expr_y+=")\n"
                f.write(expr_y)
            if (i == (j+index)):
                j = j+1
                if j== attackLen:
                    j=0  
            else:
                expr_y=""
                for varcount1 in range(1,y_count+1):
                    expr_y+="s.add(y"+str(varcount1)+"_"+str(i+1)+" == "
                    for varcount2 in range(1,x_count+1):
                        expr_y+=" + ("+str(C[varcount1-1,varcount2-1])+"*x"+str(varcount2)+"_"+str(i+1)+")"
                    for varcount3 in range(1,u_count+1):
                        expr_y+=" + ("+str(D[varcount1-1,varcount3-1])+"*uattacked"+str(varcount3)+"_"+str(i+1)+")"         
                    expr_y+=")\n"
                f.write(expr_y)

        f.write("s.add(Or(")
        assertion=""
        for varcount in range(1,x_count+1):
            for i in range(K):
                assertion+="(xabs"+str(varcount)+"_"+str(i)+" - "+str(safex[varcount-1])+")>"+str(tolerance[varcount-1])+","
        assertion = assertion[:len(assertion)-1]
        f.write(assertion)
        f.write("))\n")

        # f.write("\nprint(s.sexpr())")
        f.write("\nif s.check() != sat:\n")
        f.write("\tprint(s.check())\n")
        f.write("\tisSat = 0\n")
        f.write("else:\n")
        f.write("\tprint(s.check())\n")
        f.write("\tisSat = 1\n")
        f.write("\tf0 = open(\""+path+modelName+"_sporadic.z3result\", \"w+\")\n")
        f.write("\tf0.write(\"1\")\n")
        f.write("\tf0.close()\n") 
        f.write("\tm = s.model()\n")
        f.write("\tfor d in m.decls():\n")
        # f.write("\t\tprint (\"%s = %s\" % (d.name(), m[d]))\n")
        for varcount in range(1,u_count+1): # Parsing u, attack on u and attacked u values from the z3 py output
            f.write("\t\tif \"attackOnU"+str(varcount)+"_\" in d.name():\n")
            f.write("\t\t\ti = int(d.name().split('_')[1])\n")
            f.write("\t\t\tx = str(m[d])\n")
            f.write("\t\t\tindex = x.find(\"?\")\n")
            f.write("\t\t\tif index != -1:\n")
            f.write("\t\t\t\ty = x[:-1]\n")
            f.write("\t\t\telse:\n")
            f.write("\t\t\t\ty = x\n")
            f.write("\t\t\tattackOnU"+str(varcount)+"[i] = float(y)\n")

            f.write("\t\tif \"uattacked"+str(varcount)+"_\" in d.name():\n")
            f.write("\t\t\ti = int(d.name().split('_')[1])\n")
            f.write("\t\t\tx = str(m[d])\n")
            f.write("\t\t\tindex = x.find(\"?\")\n")
            f.write("\t\t\tif index != -1:\n")
            f.write("\t\t\t\ty = x[:-1]\n")
            f.write("\t\t\telse:\n")
            f.write("\t\t\t\ty = x\n")
            f.write("\t\t\tuattacked"+str(varcount)+"[i] = float(y)\n")

            f.write("\t\tif \"u"+str(varcount)+"_\" in d.name():\n")
            f.write("\t\t\ti = int(d.name().split('_')[1])\n")
            f.write("\t\t\tx = str(m[d])\n")
            f.write("\t\t\tindex = x.find(\"?\")\n")
            f.write("\t\t\tif index != -1:\n")
            f.write("\t\t\t\ty = x[:-1]\n")
            f.write("\t\t\telse:\n")
            f.write("\t\t\t\ty = x\n")
            f.write("\t\t\tu"+str(varcount)+"[i] = float(y)\n")
        for varcount in range(1,x_count+1): # Parsing x, absolute x and z from z3 py output
            f.write("\t\tif \"z"+str(varcount)+"_\" in d.name():\n")
            f.write("\t\t\ti = int(d.name().split('_')[1])\n")
            f.write("\t\t\tx = str(m[d])\n")
            f.write("\t\t\tindex = x.find(\"?\")\n")
            f.write("\t\t\tif index != -1:\n")
            f.write("\t\t\t\ty = x[:-1]\n")
            f.write("\t\t\telse:\n")
            f.write("\t\t\t\ty = x\n")
            f.write("\t\t\tz"+str(varcount)+"[i] = float(y)\n")

            f.write("\t\tif \"xabs"+str(varcount)+"_\" in d.name():\n")
            f.write("\t\t\ti = int(d.name().split('_')[1])\n")
            f.write("\t\t\tx = str(m[d])\n")
            f.write("\t\t\tindex = x.find(\"?\")\n")
            f.write("\t\t\tif index != -1:\n")
            f.write("\t\t\t\ty = x[:-1]\n")
            f.write("\t\t\telse:\n")
            f.write("\t\t\t\ty = x\n")
            f.write("\t\t\txabs"+str(varcount)+"[i] = float(y)\n")

            f.write("\t\tif \"x"+str(varcount)+"_\" in d.name():\n")
            f.write("\t\t\ti = int(d.name().split('_')[1])\n")
            f.write("\t\t\tx = str(m[d])\n")
            f.write("\t\t\tindex = x.find(\"?\")\n")
            f.write("\t\t\tif index != -1:\n")
            f.write("\t\t\t\ty = x[:-1]\n")
            f.write("\t\t\telse:\n")
            f.write("\t\t\t\ty = x\n")
            f.write("\t\t\tx"+str(varcount)+"[i] = float(y)\n")
        for varcount in range(1,y_count+1): # Parsing y, attack on y and r from z3 py output
            f.write("\t\tif \"attackOnY"+str(varcount)+"_\" in d.name():\n")
            f.write("\t\t\ti = int(d.name().split('_')[1])\n")
            f.write("\t\t\tx = str(m[d])\n")
            f.write("\t\t\tindex = x.find(\"?\")\n")
            f.write("\t\t\tif index != -1:\n")
            f.write("\t\t\t\ty = x[:-1]\n")
            f.write("\t\t\telse:\n")
            f.write("\t\t\t\ty = x\n")
            f.write("\t\t\tattackOnY"+str(varcount)+"[i] = float(y)\n")

            f.write("\t\tif \"y"+str(varcount)+"_\" in d.name():\n")
            f.write("\t\t\ti = int(d.name().split('_')[1])\n")
            f.write("\t\t\tx = str(m[d])\n")
            f.write("\t\t\tindex = x.find(\"?\")\n")
            f.write("\t\t\tif index != -1:\n")
            f.write("\t\t\t\ty = x[:-1]\n")
            f.write("\t\t\telse:\n")
            f.write("\t\t\t\ty = x\n")
            f.write("\t\t\ty"+str(varcount)+"[i] = float(y)\n")
            
            f.write("\t\tif \"r"+str(varcount)+"_\" in d.name():\n")
            f.write("\t\t\ti = int(d.name().split('_')[1])\n")
            f.write("\t\t\tx = str(m[d])\n")
            f.write("\t\t\tindex = x.find(\"?\")\n")
            f.write("\t\t\tif index != -1:\n")
            f.write("\t\t\t\ty = x[:-1]\n")
            f.write("\t\t\telse:\n")
            f.write("\t\t\t\ty = x\n")
            f.write("\t\t\tr"+str(varcount)+"[i] = float(y)\n")
        
        f.write("\t\tif \"r_\" in d.name():\n")
        f.write("\t\t\ti = int(d.name().split('_')[1])\n")
        f.write("\t\t\tx = str(m[d])\n")
        f.write("\t\t\tindex = x.find(\"?\")\n")
        f.write("\t\t\tif index != -1:\n")
        f.write("\t\t\t\ty = x[:-1]\n")
        f.write("\t\t\telse:\n")
        f.write("\t\t\t\ty = x\n")
        f.write("\t\t\tr[i] = float(y)\n")

        # Printing the execution sequence
        f.write("\tfor i in range({0}):\n".format(K))
        for varcount in  range(1, x_count+1):
            f.write("\t\tprint(\"x"+str(varcount)+"_{0}={1}\".format(i,x"+str(varcount)+"[i]))\n") 
        for varcount in  range(1, x_count+1):
            f.write("\t\tprint(\"z"+str(varcount)+"_{0}={1}\".format(i,z"+str(varcount)+"[i]))\n") 
        for varcount in  range(1, x_count+1):
            f.write("\t\tprint(\"xabs"+str(varcount)+"_{0}={1}\".format(i,xabs"+str(varcount)+"[i]))\n") 
        for varcount in  range(1, u_count+1):
            f.write("\t\tprint(\"attackOnU"+str(varcount)+"_{0}={1}\".format(i,attackOnU"+str(varcount)+"[i]))\n")  
        for varcount in  range(1, u_count+1):
            f.write("\t\tprint(\"u"+str(varcount)+"_{0}={1}\".format(i,u"+str(varcount)+"[i]))\n")  
        for varcount in  range(1, u_count+1):
            f.write("\t\tprint(\"uattacked"+str(varcount)+"_{0}={1}\".format(i,uattacked"+str(varcount)+"[i]))\n")
        for varcount in  range(1, y_count+1):
            f.write("\t\tprint(\"attackOnY"+str(varcount)+"_{0}={1}\".format(i,attackOnY"+str(varcount)+"[i]))\n") 
        for varcount in  range(1, y_count+1):
            f.write("\t\tprint(\"y"+str(varcount)+"_{0}={1}\".format(i,y"+str(varcount)+"[i]))\n")
        for varcount in  range(1, y_count+1):
            f.write("\t\tprint(\"r"+str(varcount)+"_{0}={1}\".format(i,r"+str(varcount)+"[i]))\n")
        f.write("\t\tprint(\"r_{0}={1}\".format(i,r[i]))\n")
        
          
        # Printing attack vectors
        for varcount in  range(1, u_count+1):
            f.write("print(\"attack on control signal component {0}\")\n".format(varcount))
            f.write("print(attackOnU{0})\n".format(varcount))
        for varcount in  range(1, y_count+1):
            f.write("print(\"attack on sensor {0}\")\n".format(varcount))
            f.write("print(attackOnY{0})\n".format(varcount))
   
        f.write("if isSat==1:\n")
        f.write("\tf0 = open(\""+path+modelName+"_sporadic.z3result\", \"w+\")\n")
        f.write("\tf0.write(\"1\")\n")
        f.write("\tf0.close()\n")

        f.close()
        os.system("python "+path+fileName+">"+path+fileName+".z3out")
        f0 = open(path+modelName+"_sporadic.z3result", "r")
        if f0.mode == 'r':
            content = f0.read()
            isSat = int(content)
        f0.close()
        if isSat==0:
            os.system("rm -rf "+path+fileName+" "+path+fileName+".z3out")
        else:
            print("go to "+path+fileName+".z3out \n")
        index = index + 1
    attackLen = attackLen + 1