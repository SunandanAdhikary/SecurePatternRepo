#include<stdio.h>
#include<math.h>
#include<inttypes.h>
#include "library.h"
float nondet_float();
int8_t nondet_int8();
int const K = 15,attackLen = 7, startpoint = 0;
int main()
	{
		float r1[K], r2[K], r[K], theta[K], omega[K], a1[K], a2[K], x1_0 = 0, x2_0 = 0, u_0 = 0, u_attacked_0 = 0, y1_0 = 0, y2_0 = 0, z1_0 = 0, z2_0 = 0,x1next_0 = 0, x2next_0 = 0, z1next_0 = 0, z2next_0 = 0,x1_1 = 0, x2_1 = 0, u_1 = 0, u_attacked_1 = 0, y1_1 = 0, y2_1 = 0, z1_1 = 0, z2_1 = 0,x1next_1 = 0, x2next_1 = 0, z1next_1 = 0, z2next_1 = 0,x1_2 = 0, x2_2 = 0, u_2 = 0, u_attacked_2 = 0, y1_2 = 0, y2_2 = 0, z1_2 = 0, z2_2 = 0,x1next_2 = 0, x2next_2 = 0, z1next_2 = 0, z2next_2 = 0,x1_3 = 0, x2_3 = 0, u_3 = 0, u_attacked_3 = 0, y1_3 = 0, y2_3 = 0, z1_3 = 0, z2_3 = 0,x1next_3 = 0, x2next_3 = 0, z1next_3 = 0, z2next_3 = 0,x1_4 = 0, x2_4 = 0, u_4 = 0, u_attacked_4 = 0, y1_4 = 0, y2_4 = 0, z1_4 = 0, z2_4 = 0,x1next_4 = 0, x2next_4 = 0, z1next_4 = 0, z2next_4 = 0,x1_5 = 0, x2_5 = 0, u_5 = 0, u_attacked_5 = 0, y1_5 = 0, y2_5 = 0, z1_5 = 0, z2_5 = 0,x1next_5 = 0, x2next_5 = 0, z1next_5 = 0, z2next_5 = 0,x1_6 = 0, x2_6 = 0, u_6 = 0, u_attacked_6 = 0, y1_6 = 0, y2_6 = 0, z1_6 = 0, z2_6 = 0,x1next_6 = 0, x2next_6 = 0, z1next_6 = 0, z2next_6 = 0,x1_7 = 0, x2_7 = 0, u_7 = 0, u_attacked_7 = 0, y1_7 = 0, y2_7 = 0, z1_7 = 0, z2_7 = 0,x1next_7 = 0, x2next_7 = 0, z1next_7 = 0, z2next_7 = 0,x1_8 = 0, x2_8 = 0, u_8 = 0, u_attacked_8 = 0, y1_8 = 0, y2_8 = 0, z1_8 = 0, z2_8 = 0,x1next_8 = 0, x2next_8 = 0, z1next_8 = 0, z2next_8 = 0,x1_9 = 0, x2_9 = 0, u_9 = 0, u_attacked_9 = 0, y1_9 = 0, y2_9 = 0, z1_9 = 0, z2_9 = 0,x1next_9 = 0, x2next_9 = 0, z1next_9 = 0, z2next_9 = 0,x1_10 = 0, x2_10 = 0, u_10 = 0, u_attacked_10 = 0, y1_10 = 0, y2_10 = 0, z1_10 = 0, z2_10 = 0,x1next_10 = 0, x2next_10 = 0, z1next_10 = 0, z2next_10 = 0,x1_11 = 0, x2_11 = 0, u_11 = 0, u_attacked_11 = 0, y1_11 = 0, y2_11 = 0, z1_11 = 0, z2_11 = 0,x1next_11 = 0, x2next_11 = 0, z1next_11 = 0, z2next_11 = 0,x1_12 = 0, x2_12 = 0, u_12 = 0, u_attacked_12 = 0, y1_12 = 0, y2_12 = 0, z1_12 = 0, z2_12 = 0,x1next_12 = 0, x2next_12 = 0, z1next_12 = 0, z2next_12 = 0,x1_13 = 0, x2_13 = 0, u_13 = 0, u_attacked_13 = 0, y1_13 = 0, y2_13 = 0, z1_13 = 0, z2_13 = 0,x1next_13 = 0, x2next_13 = 0, z1next_13 = 0, z2next_13 = 0,x1_14 = 0, x2_14 = 0, u_14 = 0, u_attacked_14 = 0, y1_14 = 0, y2_14 = 0, z1_14 = 0, z2_14 = 0,x1next_14 = 0, x2next_14 = 0, z1next_14 = 0, z2next_14 = 0,x1_15 = 0, x2_15 = 0, u_15 = 0, u_attacked_15 = 0, y1_15 = 0, y2_15 = 0, z1_15 = 0, z2_15 = 0,x1next_15 = 0, x2next_15 = 0, z1next_15 = 0, z2next_15 = 0;
		int8_t syn = 0;

		//pattern=1;
		syn = nondet_int8();
		a1[0] = AttackFormat2(syn);
		syn = nondet_int8();
		a2[0] = AttackFormat2(syn);
		u_0 = -(0.0556*z1_0) - (0.3306*z2_0);
		u_attacked_0 = u_0 + a1[0];
		y1_0 = x1_0 + a2[0];
		y2_0 = x2_0;
		r1[0] = y1_0 - z1_0;
		r2[0] = y2_0 - z2_0;
		r[0] = max(absolute(r1[0]),absolute(r2[0]));
		z1_1 = (0.66*z1_0) + (0.53*z2_0) + (0.34*u_0) + (0.36*r1[0]) + (0.27*r2[0]);
		z2_1 = -(0.53*z1_0) + (0.13*z2_0) + (0.53*u_0) - (0.31*r1[0]) + (0.08*r2[0]);
		x1_1 = (0.66*x1_0) + (0.53*x2_0) + (0.34*u_attacked_0);
		x2_1 = - (0.53*x1_0) + (0.13*x2_0) + (0.53*u_attacked_0);
		theta[0] = absolute(x1_1);
		omega[0] = absolute(x2_1);

		//pattern=1;
		syn = nondet_int8();
		a1[1] = AttackFormat2(syn);
		syn = nondet_int8();
		a2[1] = AttackFormat2(syn);
		u_1 = -(0.0556*z1_1) - (0.3306*z2_1);
		u_attacked_1 = u_1 + a1[1];
		y1_1 = x1_1 + a2[1];
		y2_1 = x2_1;
		r1[1] = y1_1 - z1_1;
		r2[1] = y2_1 - z2_1;
		r[1] = max(absolute(r1[1]),absolute(r2[1]));
		z1_2 = (0.66*z1_1) + (0.53*z2_1) + (0.34*u_1) + (0.36*r1[1]) + (0.27*r2[1]);
		z2_2 = -(0.53*z1_1) + (0.13*z2_1) + (0.53*u_1) - (0.31*r1[1]) + (0.08*r2[1]);
		x1_2 = (0.66*x1_1) + (0.53*x2_1) + (0.34*u_attacked_1);
		x2_2 = - (0.53*x1_1) + (0.13*x2_1) + (0.53*u_attacked_1);
		theta[1] = absolute(x1_2);
		omega[1] = absolute(x2_2);

		//pattern=1;
		syn = nondet_int8();
		a1[2] = AttackFormat2(syn);
		syn = nondet_int8();
		a2[2] = AttackFormat2(syn);
		u_2 = -(0.0556*z1_2) - (0.3306*z2_2);
		u_attacked_2 = u_2 + a1[2];
		y1_2 = x1_2 + a2[2];
		y2_2 = x2_2;
		r1[2] = y1_2 - z1_2;
		r2[2] = y2_2 - z2_2;
		r[2] = max(absolute(r1[2]),absolute(r2[2]));
		z1_3 = (0.66*z1_2) + (0.53*z2_2) + (0.34*u_2) + (0.36*r1[2]) + (0.27*r2[2]);
		z2_3 = -(0.53*z1_2) + (0.13*z2_2) + (0.53*u_2) - (0.31*r1[2]) + (0.08*r2[2]);
		x1_3 = (0.66*x1_2) + (0.53*x2_2) + (0.34*u_attacked_2);
		x2_3 = - (0.53*x1_2) + (0.13*x2_2) + (0.53*u_attacked_2);
		theta[2] = absolute(x1_3);
		omega[2] = absolute(x2_3);

		//pattern=1;
		syn = nondet_int8();
		a1[3] = AttackFormat2(syn);
		syn = nondet_int8();
		a2[3] = AttackFormat2(syn);
		u_3 = -(0.0556*z1_3) - (0.3306*z2_3);
		u_attacked_3 = u_3 + a1[3];
		y1_3 = x1_3 + a2[3];
		y2_3 = x2_3;
		r1[3] = y1_3 - z1_3;
		r2[3] = y2_3 - z2_3;
		r[3] = max(absolute(r1[3]),absolute(r2[3]));
		z1_4 = (0.66*z1_3) + (0.53*z2_3) + (0.34*u_3) + (0.36*r1[3]) + (0.27*r2[3]);
		z2_4 = -(0.53*z1_3) + (0.13*z2_3) + (0.53*u_3) - (0.31*r1[3]) + (0.08*r2[3]);
		x1_4 = (0.66*x1_3) + (0.53*x2_3) + (0.34*u_attacked_3);
		x2_4 = - (0.53*x1_3) + (0.13*x2_3) + (0.53*u_attacked_3);
		theta[3] = absolute(x1_4);
		omega[3] = absolute(x2_4);

		//pattern=1;
		syn = nondet_int8();
		a1[4] = AttackFormat2(syn);
		syn = nondet_int8();
		a2[4] = AttackFormat2(syn);
		u_4 = -(0.0556*z1_4) - (0.3306*z2_4);
		u_attacked_4 = u_4 + a1[4];
		y1_4 = x1_4 + a2[4];
		y2_4 = x2_4;
		r1[4] = y1_4 - z1_4;
		r2[4] = y2_4 - z2_4;
		r[4] = max(absolute(r1[4]),absolute(r2[4]));
		z1_5 = (0.66*z1_4) + (0.53*z2_4) + (0.34*u_4) + (0.36*r1[4]) + (0.27*r2[4]);
		z2_5 = -(0.53*z1_4) + (0.13*z2_4) + (0.53*u_4) - (0.31*r1[4]) + (0.08*r2[4]);
		x1_5 = (0.66*x1_4) + (0.53*x2_4) + (0.34*u_attacked_4);
		x2_5 = - (0.53*x1_4) + (0.13*x2_4) + (0.53*u_attacked_4);
		theta[4] = absolute(x1_5);
		omega[4] = absolute(x2_5);

		//pattern=1;
		syn = nondet_int8();
		a1[5] = AttackFormat2(syn);
		syn = nondet_int8();
		a2[5] = AttackFormat2(syn);
		u_5 = -(0.0556*z1_5) - (0.3306*z2_5);
		u_attacked_5 = u_5 + a1[5];
		y1_5 = x1_5 + a2[5];
		y2_5 = x2_5;
		r1[5] = y1_5 - z1_5;
		r2[5] = y2_5 - z2_5;
		r[5] = max(absolute(r1[5]),absolute(r2[5]));
		z1_6 = (0.66*z1_5) + (0.53*z2_5) + (0.34*u_5) + (0.36*r1[5]) + (0.27*r2[5]);
		z2_6 = -(0.53*z1_5) + (0.13*z2_5) + (0.53*u_5) - (0.31*r1[5]) + (0.08*r2[5]);
		x1_6 = (0.66*x1_5) + (0.53*x2_5) + (0.34*u_attacked_5);
		x2_6 = - (0.53*x1_5) + (0.13*x2_5) + (0.53*u_attacked_5);
		theta[5] = absolute(x1_6);
		omega[5] = absolute(x2_6);

		//pattern=1;
		syn = nondet_int8();
		a1[6] = AttackFormat2(syn);
		syn = nondet_int8();
		a2[6] = AttackFormat2(syn);
		u_6 = -(0.0556*z1_6) - (0.3306*z2_6);
		u_attacked_6 = u_6 + a1[6];
		y1_6 = x1_6 + a2[6];
		y2_6 = x2_6;
		r1[6] = y1_6 - z1_6;
		r2[6] = y2_6 - z2_6;
		r[6] = max(absolute(r1[6]),absolute(r2[6]));
		z1_7 = (0.66*z1_6) + (0.53*z2_6) + (0.34*u_6) + (0.36*r1[6]) + (0.27*r2[6]);
		z2_7 = -(0.53*z1_6) + (0.13*z2_6) + (0.53*u_6) - (0.31*r1[6]) + (0.08*r2[6]);
		x1_7 = (0.66*x1_6) + (0.53*x2_6) + (0.34*u_attacked_6);
		x2_7 = - (0.53*x1_6) + (0.13*x2_6) + (0.53*u_attacked_6);
		theta[6] = absolute(x1_7);
		omega[6] = absolute(x2_7);

		//pattern=1;
		a1[7] = 0;
		a2[7] = 0;
		u_7 = -(0.0556*z1_7) - (0.3306*z2_7);
		u_attacked_7 = u_7 + a1[7];
		y1_7 = x1_7 + a2[7];
		y2_7 = x2_7;
		r1[7] = y1_7 - z1_7;
		r2[7] = y2_7 - z2_7;
		r[7] = max(absolute(r1[7]),absolute(r2[7]));
		z1_8 = (0.66*z1_7) + (0.53*z2_7) + (0.34*u_7) + (0.36*r1[7]) + (0.27*r2[7]);
		z2_8 = -(0.53*z1_7) + (0.13*z2_7) + (0.53*u_7) - (0.31*r1[7]) + (0.08*r2[7]);
		x1_8 = (0.66*x1_7) + (0.53*x2_7) + (0.34*u_attacked_7);
		x2_8 = - (0.53*x1_7) + (0.13*x2_7) + (0.53*u_attacked_7);
		theta[7] = absolute(x1_8);
		omega[7] = absolute(x2_8);

		//pattern=1;
		a1[8] = 0;
		a2[8] = 0;
		u_8 = -(0.0556*z1_8) - (0.3306*z2_8);
		u_attacked_8 = u_8 + a1[8];
		y1_8 = x1_8 + a2[8];
		y2_8 = x2_8;
		r1[8] = y1_8 - z1_8;
		r2[8] = y2_8 - z2_8;
		r[8] = max(absolute(r1[8]),absolute(r2[8]));
		z1_9 = (0.66*z1_8) + (0.53*z2_8) + (0.34*u_8) + (0.36*r1[8]) + (0.27*r2[8]);
		z2_9 = -(0.53*z1_8) + (0.13*z2_8) + (0.53*u_8) - (0.31*r1[8]) + (0.08*r2[8]);
		x1_9 = (0.66*x1_8) + (0.53*x2_8) + (0.34*u_attacked_8);
		x2_9 = - (0.53*x1_8) + (0.13*x2_8) + (0.53*u_attacked_8);
		theta[8] = absolute(x1_9);
		omega[8] = absolute(x2_9);

		//pattern=1;
		a1[9] = 0;
		a2[9] = 0;
		u_9 = -(0.0556*z1_9) - (0.3306*z2_9);
		u_attacked_9 = u_9 + a1[9];
		y1_9 = x1_9 + a2[9];
		y2_9 = x2_9;
		r1[9] = y1_9 - z1_9;
		r2[9] = y2_9 - z2_9;
		r[9] = max(absolute(r1[9]),absolute(r2[9]));
		z1_10 = (0.66*z1_9) + (0.53*z2_9) + (0.34*u_9) + (0.36*r1[9]) + (0.27*r2[9]);
		z2_10 = -(0.53*z1_9) + (0.13*z2_9) + (0.53*u_9) - (0.31*r1[9]) + (0.08*r2[9]);
		x1_10 = (0.66*x1_9) + (0.53*x2_9) + (0.34*u_attacked_9);
		x2_10 = - (0.53*x1_9) + (0.13*x2_9) + (0.53*u_attacked_9);
		theta[9] = absolute(x1_10);
		omega[9] = absolute(x2_10);

		//pattern=1;
		a1[10] = 0;
		a2[10] = 0;
		u_10 = -(0.0556*z1_10) - (0.3306*z2_10);
		u_attacked_10 = u_10 + a1[10];
		y1_10 = x1_10 + a2[10];
		y2_10 = x2_10;
		r1[10] = y1_10 - z1_10;
		r2[10] = y2_10 - z2_10;
		r[10] = max(absolute(r1[10]),absolute(r2[10]));
		z1_11 = (0.66*z1_10) + (0.53*z2_10) + (0.34*u_10) + (0.36*r1[10]) + (0.27*r2[10]);
		z2_11 = -(0.53*z1_10) + (0.13*z2_10) + (0.53*u_10) - (0.31*r1[10]) + (0.08*r2[10]);
		x1_11 = (0.66*x1_10) + (0.53*x2_10) + (0.34*u_attacked_10);
		x2_11 = - (0.53*x1_10) + (0.13*x2_10) + (0.53*u_attacked_10);
		theta[10] = absolute(x1_11);
		omega[10] = absolute(x2_11);

		//pattern=1;
		a1[11] = 0;
		a2[11] = 0;
		u_11 = -(0.0556*z1_11) - (0.3306*z2_11);
		u_attacked_11 = u_11 + a1[11];
		y1_11 = x1_11 + a2[11];
		y2_11 = x2_11;
		r1[11] = y1_11 - z1_11;
		r2[11] = y2_11 - z2_11;
		r[11] = max(absolute(r1[11]),absolute(r2[11]));
		z1_12 = (0.66*z1_11) + (0.53*z2_11) + (0.34*u_11) + (0.36*r1[11]) + (0.27*r2[11]);
		z2_12 = -(0.53*z1_11) + (0.13*z2_11) + (0.53*u_11) - (0.31*r1[11]) + (0.08*r2[11]);
		x1_12 = (0.66*x1_11) + (0.53*x2_11) + (0.34*u_attacked_11);
		x2_12 = - (0.53*x1_11) + (0.13*x2_11) + (0.53*u_attacked_11);
		theta[11] = absolute(x1_12);
		omega[11] = absolute(x2_12);

		//pattern=1;
		a1[12] = 0;
		a2[12] = 0;
		u_12 = -(0.0556*z1_12) - (0.3306*z2_12);
		u_attacked_12 = u_12 + a1[12];
		y1_12 = x1_12 + a2[12];
		y2_12 = x2_12;
		r1[12] = y1_12 - z1_12;
		r2[12] = y2_12 - z2_12;
		r[12] = max(absolute(r1[12]),absolute(r2[12]));
		z1_13 = (0.66*z1_12) + (0.53*z2_12) + (0.34*u_12) + (0.36*r1[12]) + (0.27*r2[12]);
		z2_13 = -(0.53*z1_12) + (0.13*z2_12) + (0.53*u_12) - (0.31*r1[12]) + (0.08*r2[12]);
		x1_13 = (0.66*x1_12) + (0.53*x2_12) + (0.34*u_attacked_12);
		x2_13 = - (0.53*x1_12) + (0.13*x2_12) + (0.53*u_attacked_12);
		theta[12] = absolute(x1_13);
		omega[12] = absolute(x2_13);

		//pattern=1;
		a1[13] = 0;
		a2[13] = 0;
		u_13 = -(0.0556*z1_13) - (0.3306*z2_13);
		u_attacked_13 = u_13 + a1[13];
		y1_13 = x1_13 + a2[13];
		y2_13 = x2_13;
		r1[13] = y1_13 - z1_13;
		r2[13] = y2_13 - z2_13;
		r[13] = max(absolute(r1[13]),absolute(r2[13]));
		z1_14 = (0.66*z1_13) + (0.53*z2_13) + (0.34*u_13) + (0.36*r1[13]) + (0.27*r2[13]);
		z2_14 = -(0.53*z1_13) + (0.13*z2_13) + (0.53*u_13) - (0.31*r1[13]) + (0.08*r2[13]);
		x1_14 = (0.66*x1_13) + (0.53*x2_13) + (0.34*u_attacked_13);
		x2_14 = - (0.53*x1_13) + (0.13*x2_13) + (0.53*u_attacked_13);
		theta[13] = absolute(x1_14);
		omega[13] = absolute(x2_14);

		//pattern=1;
		a1[14] = 0;
		a2[14] = 0;
		u_14 = -(0.0556*z1_14) - (0.3306*z2_14);
		u_attacked_14 = u_14 + a1[14];
		y1_14 = x1_14 + a2[14];
		y2_14 = x2_14;
		r1[14] = y1_14 - z1_14;
		r2[14] = y2_14 - z2_14;
		r[14] = max(absolute(r1[14]),absolute(r2[14]));
		z1_15 = (0.66*z1_14) + (0.53*z2_14) + (0.34*u_14) + (0.36*r1[14]) + (0.27*r2[14]);
		z2_15 = -(0.53*z1_14) + (0.13*z2_14) + (0.53*u_14) - (0.31*r1[14]) + (0.08*r2[14]);
		x1_15 = (0.66*x1_14) + (0.53*x2_14) + (0.34*u_attacked_14);
		x2_15 = - (0.53*x1_14) + (0.13*x2_14) + (0.53*u_attacked_14);
		theta[14] = absolute(x1_15);
		omega[14] = absolute(x2_15);


		assert(((r[0]>0.030000) || (r[1]>0.030000) || (r[2]>0.030000) || (r[3]>0.030000) || (r[4]>0.030000) || (r[5]>0.030000) || (r[6]>0.030000) || (r[7]>0.030000) || (r[8]>0.030000) || (r[9]>0.030000) || (r[10]>0.030000) || (r[11]>0.030000) || (r[12]>0.030000) || (r[13]>0.030000) || (r[14]>0.030000))||((theta[0]<=0.1 && omega[0]<=0.05) && (theta[1]<=0.1 && omega[1]<=0.05) && (theta[2]<=0.1 && omega[2]<=0.05) && (theta[3]<=0.1 && omega[3]<=0.05) && (theta[4]<=0.1 && omega[4]<=0.05) && (theta[5]<=0.1 && omega[5]<=0.05) && (theta[6]<=0.1 && omega[6]<=0.05) && (theta[7]<=0.1 && omega[7]<=0.05) && (theta[8]<=0.1 && omega[8]<=0.05) && (theta[9]<=0.1 && omega[9]<=0.05) && (theta[10]<=0.1 && omega[10]<=0.05) && (theta[11]<=0.1 && omega[11]<=0.05) && (theta[12]<=0.1 && omega[12]<=0.05) && (theta[13]<=0.1 && omega[13]<=0.05) && (theta[14]<=0.1 && omega[14]<=0.05)));
		return 0;
	}