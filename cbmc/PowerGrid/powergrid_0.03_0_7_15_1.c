#include<stdio.h>
#include<math.h>
#include<inttypes.h>
#include "library.h"
float nondet_float();
int8_t nondet_int8();
int const K =15,attackLen = 7, startpoint = 0;
int main()
	{
		float r[K], u_attack[2][15], y_attack[2][15], x1_abs[K],x2_abs[K],r1[K],r2[K],x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,u2_0 = 0, u2_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,u2_1 = 0, u2_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,u2_2 = 0, u2_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,u2_3 = 0, u2_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,u2_4 = 0, u2_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,u2_5 = 0, u2_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,u2_6 = 0, u2_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,u2_7 = 0, u2_attacked_7 = 0,y1_7 = 0, y2_7 = 0, x1_8 = 0, z1_8 = 0,x1next_8 = 0, z1next_8 = 0,x2_8 = 0, z2_8 = 0,x2next_8 = 0, z2next_8 = 0,u1_8 = 0, u1_attacked_8 = 0,u2_8 = 0, u2_attacked_8 = 0,y1_8 = 0, y2_8 = 0, x1_9 = 0, z1_9 = 0,x1next_9 = 0, z1next_9 = 0,x2_9 = 0, z2_9 = 0,x2next_9 = 0, z2next_9 = 0,u1_9 = 0, u1_attacked_9 = 0,u2_9 = 0, u2_attacked_9 = 0,y1_9 = 0, y2_9 = 0, x1_10 = 0, z1_10 = 0,x1next_10 = 0, z1next_10 = 0,x2_10 = 0, z2_10 = 0,x2next_10 = 0, z2next_10 = 0,u1_10 = 0, u1_attacked_10 = 0,u2_10 = 0, u2_attacked_10 = 0,y1_10 = 0, y2_10 = 0, x1_11 = 0, z1_11 = 0,x1next_11 = 0, z1next_11 = 0,x2_11 = 0, z2_11 = 0,x2next_11 = 0, z2next_11 = 0,u1_11 = 0, u1_attacked_11 = 0,u2_11 = 0, u2_attacked_11 = 0,y1_11 = 0, y2_11 = 0, x1_12 = 0, z1_12 = 0,x1next_12 = 0, z1next_12 = 0,x2_12 = 0, z2_12 = 0,x2next_12 = 0, z2next_12 = 0,u1_12 = 0, u1_attacked_12 = 0,u2_12 = 0, u2_attacked_12 = 0,y1_12 = 0, y2_12 = 0, x1_13 = 0, z1_13 = 0,x1next_13 = 0, z1next_13 = 0,x2_13 = 0, z2_13 = 0,x2next_13 = 0, z2next_13 = 0,u1_13 = 0, u1_attacked_13 = 0,u2_13 = 0, u2_attacked_13 = 0,y1_13 = 0, y2_13 = 0, x1_14 = 0, z1_14 = 0,x1next_14 = 0, z1next_14 = 0,x2_14 = 0, z2_14 = 0,x2next_14 = 0, z2next_14 = 0,u1_14 = 0, u1_attacked_14 = 0,u2_14 = 0, u2_attacked_14 = 0,y1_14 = 0, y2_14 = 0, x1_15 = 0, z1_15 = 0,x1next_15 = 0, z1next_15 = 0,x2_15 = 0, z2_15 = 0,x2next_15 = 0, z2next_15 = 0,u1_15 = 0, u1_attacked_15 = 0,u2_15 = 0, u2_attacked_15 = 0,y1_15 = 0, y2_15 = 0;
		int8_t syn = 0;

		//pattern=1.0;
		u_attack[0][0] = 0;
		u_attack[1][0] = 0;
		y_attack[0][0] = AttackFormat2(syn);
		y_attack[1][0] = AttackFormat2(syn);
		u1_0 =  - (2.9846*z1_0) - (-4.9827*z2_0);
		u2_0 =  - (6.9635*z1_0) - (-6.9599*z2_0);
		u1_attacked_0 = u1_0 + u_attack[0][0];
		u2_attacked_0 = u2_0 + u_attack[1][0];
		y1_0 = y_attack[0][0] + (0.8*x1_0) + (2.4*x2_0) + (0*u1_0) + (0*u2_0);
		y2_0 = y_attack[1][0] + (1.6*x1_0) + (0.8*x2_0) + (0*u1_0) + (0*u2_0);
		r1[0] = y1_0 - (0.8*z1_0) - (2.4*z2_0) - (0*u1_attacked_0) - (0*u2_attacked_0);
		r2[0] = y2_0 - (1.6*z1_0) - (0.8*z2_0) - (0*u1_attacked_0) - (0*u2_attacked_0);
		r[0] = max(absolute(r1[0]),absolute(r2[0]));
		z1_1 =  (-1*z1_0) + (-3*z2_0) + (2*u1_0) + (-1*u2_0) + (-1.1751*r1[0]) + (-0.1412*r2[0]) ;
		z2_1 =  (3*z1_0) + (-5*z2_0) + (1*u1_0) + (0*u2_0) + (-2.6599*r1[0]) + (2.2549*r2[0]) ;
		x1_1 =  (-1*x1_0) + (-3*x2_0) + (2*u1_attacked_0) + (-1*u2_attacked_0) ;
		x2_1 =  (3*x1_0) + (-5*x2_0) + (1*u1_attacked_0) + (0*u2_attacked_0) ;
		x1_abs[0] = absolute(x1_1);
		x2_abs[0] = absolute(x2_1);
		//pattern=1.0;
		u_attack[0][1] = 0;
		u_attack[1][1] = 0;
		y_attack[0][1] = AttackFormat2(syn);
		y_attack[1][1] = AttackFormat2(syn);
		u1_1 =  - (2.9846*z1_1) - (-4.9827*z2_1);
		u2_1 =  - (6.9635*z1_1) - (-6.9599*z2_1);
		u1_attacked_1 = u1_1 + u_attack[0][1];
		u2_attacked_1 = u2_1 + u_attack[1][1];
		y1_1 = y_attack[0][1] + (0.8*x1_1) + (2.4*x2_1) + (0*u1_1) + (0*u2_1);
		y2_1 = y_attack[1][1] + (1.6*x1_1) + (0.8*x2_1) + (0*u1_1) + (0*u2_1);
		r1[1] = y1_1 - (0.8*z1_1) - (2.4*z2_1) - (0*u1_attacked_1) - (0*u2_attacked_1);
		r2[1] = y2_1 - (1.6*z1_1) - (0.8*z2_1) - (0*u1_attacked_1) - (0*u2_attacked_1);
		r[1] = max(absolute(r1[1]),absolute(r2[1]));
		z1_2 =  (-1*z1_1) + (-3*z2_1) + (2*u1_1) + (-1*u2_1) + (-1.1751*r1[1]) + (-0.1412*r2[1]) ;
		z2_2 =  (3*z1_1) + (-5*z2_1) + (1*u1_1) + (0*u2_1) + (-2.6599*r1[1]) + (2.2549*r2[1]) ;
		x1_2 =  (-1*x1_1) + (-3*x2_1) + (2*u1_attacked_1) + (-1*u2_attacked_1) ;
		x2_2 =  (3*x1_1) + (-5*x2_1) + (1*u1_attacked_1) + (0*u2_attacked_1) ;
		x1_abs[1] = absolute(x1_2);
		x2_abs[1] = absolute(x2_2);
		//pattern=1.0;
		u_attack[0][2] = 0;
		u_attack[1][2] = 0;
		y_attack[0][2] = AttackFormat2(syn);
		y_attack[1][2] = AttackFormat2(syn);
		u1_2 =  - (2.9846*z1_2) - (-4.9827*z2_2);
		u2_2 =  - (6.9635*z1_2) - (-6.9599*z2_2);
		u1_attacked_2 = u1_2 + u_attack[0][2];
		u2_attacked_2 = u2_2 + u_attack[1][2];
		y1_2 = y_attack[0][2] + (0.8*x1_2) + (2.4*x2_2) + (0*u1_2) + (0*u2_2);
		y2_2 = y_attack[1][2] + (1.6*x1_2) + (0.8*x2_2) + (0*u1_2) + (0*u2_2);
		r1[2] = y1_2 - (0.8*z1_2) - (2.4*z2_2) - (0*u1_attacked_2) - (0*u2_attacked_2);
		r2[2] = y2_2 - (1.6*z1_2) - (0.8*z2_2) - (0*u1_attacked_2) - (0*u2_attacked_2);
		r[2] = max(absolute(r1[2]),absolute(r2[2]));
		z1_3 =  (-1*z1_2) + (-3*z2_2) + (2*u1_2) + (-1*u2_2) + (-1.1751*r1[2]) + (-0.1412*r2[2]) ;
		z2_3 =  (3*z1_2) + (-5*z2_2) + (1*u1_2) + (0*u2_2) + (-2.6599*r1[2]) + (2.2549*r2[2]) ;
		x1_3 =  (-1*x1_2) + (-3*x2_2) + (2*u1_attacked_2) + (-1*u2_attacked_2) ;
		x2_3 =  (3*x1_2) + (-5*x2_2) + (1*u1_attacked_2) + (0*u2_attacked_2) ;
		x1_abs[2] = absolute(x1_3);
		x2_abs[2] = absolute(x2_3);
		//pattern=1.0;
		u_attack[0][3] = 0;
		u_attack[1][3] = 0;
		y_attack[0][3] = AttackFormat2(syn);
		y_attack[1][3] = AttackFormat2(syn);
		u1_3 =  - (2.9846*z1_3) - (-4.9827*z2_3);
		u2_3 =  - (6.9635*z1_3) - (-6.9599*z2_3);
		u1_attacked_3 = u1_3 + u_attack[0][3];
		u2_attacked_3 = u2_3 + u_attack[1][3];
		y1_3 = y_attack[0][3] + (0.8*x1_3) + (2.4*x2_3) + (0*u1_3) + (0*u2_3);
		y2_3 = y_attack[1][3] + (1.6*x1_3) + (0.8*x2_3) + (0*u1_3) + (0*u2_3);
		r1[3] = y1_3 - (0.8*z1_3) - (2.4*z2_3) - (0*u1_attacked_3) - (0*u2_attacked_3);
		r2[3] = y2_3 - (1.6*z1_3) - (0.8*z2_3) - (0*u1_attacked_3) - (0*u2_attacked_3);
		r[3] = max(absolute(r1[3]),absolute(r2[3]));
		z1_4 =  (-1*z1_3) + (-3*z2_3) + (2*u1_3) + (-1*u2_3) + (-1.1751*r1[3]) + (-0.1412*r2[3]) ;
		z2_4 =  (3*z1_3) + (-5*z2_3) + (1*u1_3) + (0*u2_3) + (-2.6599*r1[3]) + (2.2549*r2[3]) ;
		x1_4 =  (-1*x1_3) + (-3*x2_3) + (2*u1_attacked_3) + (-1*u2_attacked_3) ;
		x2_4 =  (3*x1_3) + (-5*x2_3) + (1*u1_attacked_3) + (0*u2_attacked_3) ;
		x1_abs[3] = absolute(x1_4);
		x2_abs[3] = absolute(x2_4);
		//pattern=1.0;
		u_attack[0][4] = 0;
		u_attack[1][4] = 0;
		y_attack[0][4] = AttackFormat2(syn);
		y_attack[1][4] = AttackFormat2(syn);
		u1_4 =  - (2.9846*z1_4) - (-4.9827*z2_4);
		u2_4 =  - (6.9635*z1_4) - (-6.9599*z2_4);
		u1_attacked_4 = u1_4 + u_attack[0][4];
		u2_attacked_4 = u2_4 + u_attack[1][4];
		y1_4 = y_attack[0][4] + (0.8*x1_4) + (2.4*x2_4) + (0*u1_4) + (0*u2_4);
		y2_4 = y_attack[1][4] + (1.6*x1_4) + (0.8*x2_4) + (0*u1_4) + (0*u2_4);
		r1[4] = y1_4 - (0.8*z1_4) - (2.4*z2_4) - (0*u1_attacked_4) - (0*u2_attacked_4);
		r2[4] = y2_4 - (1.6*z1_4) - (0.8*z2_4) - (0*u1_attacked_4) - (0*u2_attacked_4);
		r[4] = max(absolute(r1[4]),absolute(r2[4]));
		z1_5 =  (-1*z1_4) + (-3*z2_4) + (2*u1_4) + (-1*u2_4) + (-1.1751*r1[4]) + (-0.1412*r2[4]) ;
		z2_5 =  (3*z1_4) + (-5*z2_4) + (1*u1_4) + (0*u2_4) + (-2.6599*r1[4]) + (2.2549*r2[4]) ;
		x1_5 =  (-1*x1_4) + (-3*x2_4) + (2*u1_attacked_4) + (-1*u2_attacked_4) ;
		x2_5 =  (3*x1_4) + (-5*x2_4) + (1*u1_attacked_4) + (0*u2_attacked_4) ;
		x1_abs[4] = absolute(x1_5);
		x2_abs[4] = absolute(x2_5);
		//pattern=1.0;
		u_attack[0][5] = 0;
		u_attack[1][5] = 0;
		y_attack[0][5] = AttackFormat2(syn);
		y_attack[1][5] = AttackFormat2(syn);
		u1_5 =  - (2.9846*z1_5) - (-4.9827*z2_5);
		u2_5 =  - (6.9635*z1_5) - (-6.9599*z2_5);
		u1_attacked_5 = u1_5 + u_attack[0][5];
		u2_attacked_5 = u2_5 + u_attack[1][5];
		y1_5 = y_attack[0][5] + (0.8*x1_5) + (2.4*x2_5) + (0*u1_5) + (0*u2_5);
		y2_5 = y_attack[1][5] + (1.6*x1_5) + (0.8*x2_5) + (0*u1_5) + (0*u2_5);
		r1[5] = y1_5 - (0.8*z1_5) - (2.4*z2_5) - (0*u1_attacked_5) - (0*u2_attacked_5);
		r2[5] = y2_5 - (1.6*z1_5) - (0.8*z2_5) - (0*u1_attacked_5) - (0*u2_attacked_5);
		r[5] = max(absolute(r1[5]),absolute(r2[5]));
		z1_6 =  (-1*z1_5) + (-3*z2_5) + (2*u1_5) + (-1*u2_5) + (-1.1751*r1[5]) + (-0.1412*r2[5]) ;
		z2_6 =  (3*z1_5) + (-5*z2_5) + (1*u1_5) + (0*u2_5) + (-2.6599*r1[5]) + (2.2549*r2[5]) ;
		x1_6 =  (-1*x1_5) + (-3*x2_5) + (2*u1_attacked_5) + (-1*u2_attacked_5) ;
		x2_6 =  (3*x1_5) + (-5*x2_5) + (1*u1_attacked_5) + (0*u2_attacked_5) ;
		x1_abs[5] = absolute(x1_6);
		x2_abs[5] = absolute(x2_6);
		//pattern=1.0;
		u_attack[0][6] = 0;
		u_attack[1][6] = 0;
		y_attack[0][6] = AttackFormat2(syn);
		y_attack[1][6] = AttackFormat2(syn);
		u1_6 =  - (2.9846*z1_6) - (-4.9827*z2_6);
		u2_6 =  - (6.9635*z1_6) - (-6.9599*z2_6);
		u1_attacked_6 = u1_6 + u_attack[0][6];
		u2_attacked_6 = u2_6 + u_attack[1][6];
		y1_6 = y_attack[0][6] + (0.8*x1_6) + (2.4*x2_6) + (0*u1_6) + (0*u2_6);
		y2_6 = y_attack[1][6] + (1.6*x1_6) + (0.8*x2_6) + (0*u1_6) + (0*u2_6);
		r1[6] = y1_6 - (0.8*z1_6) - (2.4*z2_6) - (0*u1_attacked_6) - (0*u2_attacked_6);
		r2[6] = y2_6 - (1.6*z1_6) - (0.8*z2_6) - (0*u1_attacked_6) - (0*u2_attacked_6);
		r[6] = max(absolute(r1[6]),absolute(r2[6]));
		z1_7 =  (-1*z1_6) + (-3*z2_6) + (2*u1_6) + (-1*u2_6) + (-1.1751*r1[6]) + (-0.1412*r2[6]) ;
		z2_7 =  (3*z1_6) + (-5*z2_6) + (1*u1_6) + (0*u2_6) + (-2.6599*r1[6]) + (2.2549*r2[6]) ;
		x1_7 =  (-1*x1_6) + (-3*x2_6) + (2*u1_attacked_6) + (-1*u2_attacked_6) ;
		x2_7 =  (3*x1_6) + (-5*x2_6) + (1*u1_attacked_6) + (0*u2_attacked_6) ;
		x1_abs[6] = absolute(x1_7);
		x2_abs[6] = absolute(x2_7);
		//pattern=1.0;
		u_attack[0][7] = 0;
		u_attack[1][7] = 0;
		y_attack[0][7] = 0;
		y_attack[1][7] = 0;
		u1_7 =  - (2.9846*z1_7) - (-4.9827*z2_7);
		u2_7 =  - (6.9635*z1_7) - (-6.9599*z2_7);
		u1_attacked_7 = u1_7 + u_attack[0][7];
		u2_attacked_7 = u2_7 + u_attack[1][7];
		y1_7 = y_attack[0][7] + (0.8*x1_7) + (2.4*x2_7) + (0*u1_7) + (0*u2_7);
		y2_7 = y_attack[1][7] + (1.6*x1_7) + (0.8*x2_7) + (0*u1_7) + (0*u2_7);
		r1[7] = y1_7 - (0.8*z1_7) - (2.4*z2_7) - (0*u1_attacked_7) - (0*u2_attacked_7);
		r2[7] = y2_7 - (1.6*z1_7) - (0.8*z2_7) - (0*u1_attacked_7) - (0*u2_attacked_7);
		r[7] = max(absolute(r1[7]),absolute(r2[7]));
		z1_8 =  (-1*z1_7) + (-3*z2_7) + (2*u1_7) + (-1*u2_7) + (-1.1751*r1[7]) + (-0.1412*r2[7]) ;
		z2_8 =  (3*z1_7) + (-5*z2_7) + (1*u1_7) + (0*u2_7) + (-2.6599*r1[7]) + (2.2549*r2[7]) ;
		x1_8 =  (-1*x1_7) + (-3*x2_7) + (2*u1_attacked_7) + (-1*u2_attacked_7) ;
		x2_8 =  (3*x1_7) + (-5*x2_7) + (1*u1_attacked_7) + (0*u2_attacked_7) ;
		x1_abs[7] = absolute(x1_8);
		x2_abs[7] = absolute(x2_8);
		//pattern=1.0;
		u_attack[0][8] = 0;
		u_attack[1][8] = 0;
		y_attack[0][8] = 0;
		y_attack[1][8] = 0;
		u1_8 =  - (2.9846*z1_8) - (-4.9827*z2_8);
		u2_8 =  - (6.9635*z1_8) - (-6.9599*z2_8);
		u1_attacked_8 = u1_8 + u_attack[0][8];
		u2_attacked_8 = u2_8 + u_attack[1][8];
		y1_8 = y_attack[0][8] + (0.8*x1_8) + (2.4*x2_8) + (0*u1_8) + (0*u2_8);
		y2_8 = y_attack[1][8] + (1.6*x1_8) + (0.8*x2_8) + (0*u1_8) + (0*u2_8);
		r1[8] = y1_8 - (0.8*z1_8) - (2.4*z2_8) - (0*u1_attacked_8) - (0*u2_attacked_8);
		r2[8] = y2_8 - (1.6*z1_8) - (0.8*z2_8) - (0*u1_attacked_8) - (0*u2_attacked_8);
		r[8] = max(absolute(r1[8]),absolute(r2[8]));
		z1_9 =  (-1*z1_8) + (-3*z2_8) + (2*u1_8) + (-1*u2_8) + (-1.1751*r1[8]) + (-0.1412*r2[8]) ;
		z2_9 =  (3*z1_8) + (-5*z2_8) + (1*u1_8) + (0*u2_8) + (-2.6599*r1[8]) + (2.2549*r2[8]) ;
		x1_9 =  (-1*x1_8) + (-3*x2_8) + (2*u1_attacked_8) + (-1*u2_attacked_8) ;
		x2_9 =  (3*x1_8) + (-5*x2_8) + (1*u1_attacked_8) + (0*u2_attacked_8) ;
		x1_abs[8] = absolute(x1_9);
		x2_abs[8] = absolute(x2_9);
		//pattern=1.0;
		u_attack[0][9] = 0;
		u_attack[1][9] = 0;
		y_attack[0][9] = 0;
		y_attack[1][9] = 0;
		u1_9 =  - (2.9846*z1_9) - (-4.9827*z2_9);
		u2_9 =  - (6.9635*z1_9) - (-6.9599*z2_9);
		u1_attacked_9 = u1_9 + u_attack[0][9];
		u2_attacked_9 = u2_9 + u_attack[1][9];
		y1_9 = y_attack[0][9] + (0.8*x1_9) + (2.4*x2_9) + (0*u1_9) + (0*u2_9);
		y2_9 = y_attack[1][9] + (1.6*x1_9) + (0.8*x2_9) + (0*u1_9) + (0*u2_9);
		r1[9] = y1_9 - (0.8*z1_9) - (2.4*z2_9) - (0*u1_attacked_9) - (0*u2_attacked_9);
		r2[9] = y2_9 - (1.6*z1_9) - (0.8*z2_9) - (0*u1_attacked_9) - (0*u2_attacked_9);
		r[9] = max(absolute(r1[9]),absolute(r2[9]));
		z1_10 =  (-1*z1_9) + (-3*z2_9) + (2*u1_9) + (-1*u2_9) + (-1.1751*r1[9]) + (-0.1412*r2[9]) ;
		z2_10 =  (3*z1_9) + (-5*z2_9) + (1*u1_9) + (0*u2_9) + (-2.6599*r1[9]) + (2.2549*r2[9]) ;
		x1_10 =  (-1*x1_9) + (-3*x2_9) + (2*u1_attacked_9) + (-1*u2_attacked_9) ;
		x2_10 =  (3*x1_9) + (-5*x2_9) + (1*u1_attacked_9) + (0*u2_attacked_9) ;
		x1_abs[9] = absolute(x1_10);
		x2_abs[9] = absolute(x2_10);
		//pattern=1.0;
		u_attack[0][10] = 0;
		u_attack[1][10] = 0;
		y_attack[0][10] = 0;
		y_attack[1][10] = 0;
		u1_10 =  - (2.9846*z1_10) - (-4.9827*z2_10);
		u2_10 =  - (6.9635*z1_10) - (-6.9599*z2_10);
		u1_attacked_10 = u1_10 + u_attack[0][10];
		u2_attacked_10 = u2_10 + u_attack[1][10];
		y1_10 = y_attack[0][10] + (0.8*x1_10) + (2.4*x2_10) + (0*u1_10) + (0*u2_10);
		y2_10 = y_attack[1][10] + (1.6*x1_10) + (0.8*x2_10) + (0*u1_10) + (0*u2_10);
		r1[10] = y1_10 - (0.8*z1_10) - (2.4*z2_10) - (0*u1_attacked_10) - (0*u2_attacked_10);
		r2[10] = y2_10 - (1.6*z1_10) - (0.8*z2_10) - (0*u1_attacked_10) - (0*u2_attacked_10);
		r[10] = max(absolute(r1[10]),absolute(r2[10]));
		z1_11 =  (-1*z1_10) + (-3*z2_10) + (2*u1_10) + (-1*u2_10) + (-1.1751*r1[10]) + (-0.1412*r2[10]) ;
		z2_11 =  (3*z1_10) + (-5*z2_10) + (1*u1_10) + (0*u2_10) + (-2.6599*r1[10]) + (2.2549*r2[10]) ;
		x1_11 =  (-1*x1_10) + (-3*x2_10) + (2*u1_attacked_10) + (-1*u2_attacked_10) ;
		x2_11 =  (3*x1_10) + (-5*x2_10) + (1*u1_attacked_10) + (0*u2_attacked_10) ;
		x1_abs[10] = absolute(x1_11);
		x2_abs[10] = absolute(x2_11);
		//pattern=1.0;
		u_attack[0][11] = 0;
		u_attack[1][11] = 0;
		y_attack[0][11] = 0;
		y_attack[1][11] = 0;
		u1_11 =  - (2.9846*z1_11) - (-4.9827*z2_11);
		u2_11 =  - (6.9635*z1_11) - (-6.9599*z2_11);
		u1_attacked_11 = u1_11 + u_attack[0][11];
		u2_attacked_11 = u2_11 + u_attack[1][11];
		y1_11 = y_attack[0][11] + (0.8*x1_11) + (2.4*x2_11) + (0*u1_11) + (0*u2_11);
		y2_11 = y_attack[1][11] + (1.6*x1_11) + (0.8*x2_11) + (0*u1_11) + (0*u2_11);
		r1[11] = y1_11 - (0.8*z1_11) - (2.4*z2_11) - (0*u1_attacked_11) - (0*u2_attacked_11);
		r2[11] = y2_11 - (1.6*z1_11) - (0.8*z2_11) - (0*u1_attacked_11) - (0*u2_attacked_11);
		r[11] = max(absolute(r1[11]),absolute(r2[11]));
		z1_12 =  (-1*z1_11) + (-3*z2_11) + (2*u1_11) + (-1*u2_11) + (-1.1751*r1[11]) + (-0.1412*r2[11]) ;
		z2_12 =  (3*z1_11) + (-5*z2_11) + (1*u1_11) + (0*u2_11) + (-2.6599*r1[11]) + (2.2549*r2[11]) ;
		x1_12 =  (-1*x1_11) + (-3*x2_11) + (2*u1_attacked_11) + (-1*u2_attacked_11) ;
		x2_12 =  (3*x1_11) + (-5*x2_11) + (1*u1_attacked_11) + (0*u2_attacked_11) ;
		x1_abs[11] = absolute(x1_12);
		x2_abs[11] = absolute(x2_12);
		//pattern=1.0;
		u_attack[0][12] = 0;
		u_attack[1][12] = 0;
		y_attack[0][12] = 0;
		y_attack[1][12] = 0;
		u1_12 =  - (2.9846*z1_12) - (-4.9827*z2_12);
		u2_12 =  - (6.9635*z1_12) - (-6.9599*z2_12);
		u1_attacked_12 = u1_12 + u_attack[0][12];
		u2_attacked_12 = u2_12 + u_attack[1][12];
		y1_12 = y_attack[0][12] + (0.8*x1_12) + (2.4*x2_12) + (0*u1_12) + (0*u2_12);
		y2_12 = y_attack[1][12] + (1.6*x1_12) + (0.8*x2_12) + (0*u1_12) + (0*u2_12);
		r1[12] = y1_12 - (0.8*z1_12) - (2.4*z2_12) - (0*u1_attacked_12) - (0*u2_attacked_12);
		r2[12] = y2_12 - (1.6*z1_12) - (0.8*z2_12) - (0*u1_attacked_12) - (0*u2_attacked_12);
		r[12] = max(absolute(r1[12]),absolute(r2[12]));
		z1_13 =  (-1*z1_12) + (-3*z2_12) + (2*u1_12) + (-1*u2_12) + (-1.1751*r1[12]) + (-0.1412*r2[12]) ;
		z2_13 =  (3*z1_12) + (-5*z2_12) + (1*u1_12) + (0*u2_12) + (-2.6599*r1[12]) + (2.2549*r2[12]) ;
		x1_13 =  (-1*x1_12) + (-3*x2_12) + (2*u1_attacked_12) + (-1*u2_attacked_12) ;
		x2_13 =  (3*x1_12) + (-5*x2_12) + (1*u1_attacked_12) + (0*u2_attacked_12) ;
		x1_abs[12] = absolute(x1_13);
		x2_abs[12] = absolute(x2_13);
		//pattern=1.0;
		u_attack[0][13] = 0;
		u_attack[1][13] = 0;
		y_attack[0][13] = 0;
		y_attack[1][13] = 0;
		u1_13 =  - (2.9846*z1_13) - (-4.9827*z2_13);
		u2_13 =  - (6.9635*z1_13) - (-6.9599*z2_13);
		u1_attacked_13 = u1_13 + u_attack[0][13];
		u2_attacked_13 = u2_13 + u_attack[1][13];
		y1_13 = y_attack[0][13] + (0.8*x1_13) + (2.4*x2_13) + (0*u1_13) + (0*u2_13);
		y2_13 = y_attack[1][13] + (1.6*x1_13) + (0.8*x2_13) + (0*u1_13) + (0*u2_13);
		r1[13] = y1_13 - (0.8*z1_13) - (2.4*z2_13) - (0*u1_attacked_13) - (0*u2_attacked_13);
		r2[13] = y2_13 - (1.6*z1_13) - (0.8*z2_13) - (0*u1_attacked_13) - (0*u2_attacked_13);
		r[13] = max(absolute(r1[13]),absolute(r2[13]));
		z1_14 =  (-1*z1_13) + (-3*z2_13) + (2*u1_13) + (-1*u2_13) + (-1.1751*r1[13]) + (-0.1412*r2[13]) ;
		z2_14 =  (3*z1_13) + (-5*z2_13) + (1*u1_13) + (0*u2_13) + (-2.6599*r1[13]) + (2.2549*r2[13]) ;
		x1_14 =  (-1*x1_13) + (-3*x2_13) + (2*u1_attacked_13) + (-1*u2_attacked_13) ;
		x2_14 =  (3*x1_13) + (-5*x2_13) + (1*u1_attacked_13) + (0*u2_attacked_13) ;
		x1_abs[13] = absolute(x1_14);
		x2_abs[13] = absolute(x2_14);
		//pattern=1.0;
		u_attack[0][14] = 0;
		u_attack[1][14] = 0;
		y_attack[0][14] = 0;
		y_attack[1][14] = 0;
		u1_14 =  - (2.9846*z1_14) - (-4.9827*z2_14);
		u2_14 =  - (6.9635*z1_14) - (-6.9599*z2_14);
		u1_attacked_14 = u1_14 + u_attack[0][14];
		u2_attacked_14 = u2_14 + u_attack[1][14];
		y1_14 = y_attack[0][14] + (0.8*x1_14) + (2.4*x2_14) + (0*u1_14) + (0*u2_14);
		y2_14 = y_attack[1][14] + (1.6*x1_14) + (0.8*x2_14) + (0*u1_14) + (0*u2_14);
		r1[14] = y1_14 - (0.8*z1_14) - (2.4*z2_14) - (0*u1_attacked_14) - (0*u2_attacked_14);
		r2[14] = y2_14 - (1.6*z1_14) - (0.8*z2_14) - (0*u1_attacked_14) - (0*u2_attacked_14);
		r[14] = max(absolute(r1[14]),absolute(r2[14]));
		z1_15 =  (-1*z1_14) + (-3*z2_14) + (2*u1_14) + (-1*u2_14) + (-1.1751*r1[14]) + (-0.1412*r2[14]) ;
		z2_15 =  (3*z1_14) + (-5*z2_14) + (1*u1_14) + (0*u2_14) + (-2.6599*r1[14]) + (2.2549*r2[14]) ;
		x1_15 =  (-1*x1_14) + (-3*x2_14) + (2*u1_attacked_14) + (-1*u2_attacked_14) ;
		x2_15 =  (3*x1_14) + (-5*x2_14) + (1*u1_attacked_14) + (0*u2_attacked_14) ;
		x1_abs[14] = absolute(x1_15);
		x2_abs[14] = absolute(x2_15);

		assert(((r[0]>0.03) || (r[1]>0.03) || (r[2]>0.03) || (r[3]>0.03) || (r[4]>0.03) || (r[5]>0.03) || (r[6]>0.03) || (r[7]>0.03) || (r[8]>0.03) || (r[9]>0.03) || (r[10]>0.03) || (r[11]>0.03) || (r[12]>0.03) || (r[13]>0.03) || (r[14]>0.03))||((x1_abs[0]<=0.05) && (x2_abs[0]<=0.15) && (x1_abs[1]<=0.05) && (x2_abs[1]<=0.15) && (x1_abs[2]<=0.05) && (x2_abs[2]<=0.15) && (x1_abs[3]<=0.05) && (x2_abs[3]<=0.15) && (x1_abs[4]<=0.05) && (x2_abs[4]<=0.15) && (x1_abs[5]<=0.05) && (x2_abs[5]<=0.15) && (x1_abs[6]<=0.05) && (x2_abs[6]<=0.15) && (x1_abs[7]<=0.05) && (x2_abs[7]<=0.15) && (x1_abs[8]<=0.05) && (x2_abs[8]<=0.15) && (x1_abs[9]<=0.05) && (x2_abs[9]<=0.15) && (x1_abs[10]<=0.05) && (x2_abs[10]<=0.15) && (x1_abs[11]<=0.05) && (x2_abs[11]<=0.15) && (x1_abs[12]<=0.05) && (x2_abs[12]<=0.15) && (x1_abs[13]<=0.05) && (x2_abs[13]<=0.15) && (x1_abs[14]<=0.05) && (x2_abs[14]<=0.15)));
		return 0;
	}