#include<stdio.h>
#include<math.h>
#include<inttypes.h>
#include "library.h"
float nondet_float();
int8_t nondet_int8();
int const K =15,attackLen = 7, startpoint = 0;
int main()
	{
		float r[K], a1[K], a2[K], x1_abs[K],x2_abs[K],r1[K],r2[K],x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,y1_7 = 0, y2_7 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,y1_7 = 0, y2_7 = 0, x1_8 = 0, z1_8 = 0,x1next_8 = 0, z1next_8 = 0,x2_8 = 0, z2_8 = 0,x2next_8 = 0, z2next_8 = 0,u1_8 = 0, u1_attacked_8 = 0,y1_8 = 0, y2_8 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,y1_7 = 0, y2_7 = 0, x1_8 = 0, z1_8 = 0,x1next_8 = 0, z1next_8 = 0,x2_8 = 0, z2_8 = 0,x2next_8 = 0, z2next_8 = 0,u1_8 = 0, u1_attacked_8 = 0,y1_8 = 0, y2_8 = 0, x1_9 = 0, z1_9 = 0,x1next_9 = 0, z1next_9 = 0,x2_9 = 0, z2_9 = 0,x2next_9 = 0, z2next_9 = 0,u1_9 = 0, u1_attacked_9 = 0,y1_9 = 0, y2_9 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,y1_7 = 0, y2_7 = 0, x1_8 = 0, z1_8 = 0,x1next_8 = 0, z1next_8 = 0,x2_8 = 0, z2_8 = 0,x2next_8 = 0, z2next_8 = 0,u1_8 = 0, u1_attacked_8 = 0,y1_8 = 0, y2_8 = 0, x1_9 = 0, z1_9 = 0,x1next_9 = 0, z1next_9 = 0,x2_9 = 0, z2_9 = 0,x2next_9 = 0, z2next_9 = 0,u1_9 = 0, u1_attacked_9 = 0,y1_9 = 0, y2_9 = 0, x1_10 = 0, z1_10 = 0,x1next_10 = 0, z1next_10 = 0,x2_10 = 0, z2_10 = 0,x2next_10 = 0, z2next_10 = 0,u1_10 = 0, u1_attacked_10 = 0,y1_10 = 0, y2_10 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,y1_7 = 0, y2_7 = 0, x1_8 = 0, z1_8 = 0,x1next_8 = 0, z1next_8 = 0,x2_8 = 0, z2_8 = 0,x2next_8 = 0, z2next_8 = 0,u1_8 = 0, u1_attacked_8 = 0,y1_8 = 0, y2_8 = 0, x1_9 = 0, z1_9 = 0,x1next_9 = 0, z1next_9 = 0,x2_9 = 0, z2_9 = 0,x2next_9 = 0, z2next_9 = 0,u1_9 = 0, u1_attacked_9 = 0,y1_9 = 0, y2_9 = 0, x1_10 = 0, z1_10 = 0,x1next_10 = 0, z1next_10 = 0,x2_10 = 0, z2_10 = 0,x2next_10 = 0, z2next_10 = 0,u1_10 = 0, u1_attacked_10 = 0,y1_10 = 0, y2_10 = 0, x1_11 = 0, z1_11 = 0,x1next_11 = 0, z1next_11 = 0,x2_11 = 0, z2_11 = 0,x2next_11 = 0, z2next_11 = 0,u1_11 = 0, u1_attacked_11 = 0,y1_11 = 0, y2_11 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,y1_7 = 0, y2_7 = 0, x1_8 = 0, z1_8 = 0,x1next_8 = 0, z1next_8 = 0,x2_8 = 0, z2_8 = 0,x2next_8 = 0, z2next_8 = 0,u1_8 = 0, u1_attacked_8 = 0,y1_8 = 0, y2_8 = 0, x1_9 = 0, z1_9 = 0,x1next_9 = 0, z1next_9 = 0,x2_9 = 0, z2_9 = 0,x2next_9 = 0, z2next_9 = 0,u1_9 = 0, u1_attacked_9 = 0,y1_9 = 0, y2_9 = 0, x1_10 = 0, z1_10 = 0,x1next_10 = 0, z1next_10 = 0,x2_10 = 0, z2_10 = 0,x2next_10 = 0, z2next_10 = 0,u1_10 = 0, u1_attacked_10 = 0,y1_10 = 0, y2_10 = 0, x1_11 = 0, z1_11 = 0,x1next_11 = 0, z1next_11 = 0,x2_11 = 0, z2_11 = 0,x2next_11 = 0, z2next_11 = 0,u1_11 = 0, u1_attacked_11 = 0,y1_11 = 0, y2_11 = 0, x1_12 = 0, z1_12 = 0,x1next_12 = 0, z1next_12 = 0,x2_12 = 0, z2_12 = 0,x2next_12 = 0, z2next_12 = 0,u1_12 = 0, u1_attacked_12 = 0,y1_12 = 0, y2_12 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,y1_7 = 0, y2_7 = 0, x1_8 = 0, z1_8 = 0,x1next_8 = 0, z1next_8 = 0,x2_8 = 0, z2_8 = 0,x2next_8 = 0, z2next_8 = 0,u1_8 = 0, u1_attacked_8 = 0,y1_8 = 0, y2_8 = 0, x1_9 = 0, z1_9 = 0,x1next_9 = 0, z1next_9 = 0,x2_9 = 0, z2_9 = 0,x2next_9 = 0, z2next_9 = 0,u1_9 = 0, u1_attacked_9 = 0,y1_9 = 0, y2_9 = 0, x1_10 = 0, z1_10 = 0,x1next_10 = 0, z1next_10 = 0,x2_10 = 0, z2_10 = 0,x2next_10 = 0, z2next_10 = 0,u1_10 = 0, u1_attacked_10 = 0,y1_10 = 0, y2_10 = 0, x1_11 = 0, z1_11 = 0,x1next_11 = 0, z1next_11 = 0,x2_11 = 0, z2_11 = 0,x2next_11 = 0, z2next_11 = 0,u1_11 = 0, u1_attacked_11 = 0,y1_11 = 0, y2_11 = 0, x1_12 = 0, z1_12 = 0,x1next_12 = 0, z1next_12 = 0,x2_12 = 0, z2_12 = 0,x2next_12 = 0, z2next_12 = 0,u1_12 = 0, u1_attacked_12 = 0,y1_12 = 0, y2_12 = 0, x1_13 = 0, z1_13 = 0,x1next_13 = 0, z1next_13 = 0,x2_13 = 0, z2_13 = 0,x2next_13 = 0, z2next_13 = 0,u1_13 = 0, u1_attacked_13 = 0,y1_13 = 0, y2_13 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,y1_7 = 0, y2_7 = 0, x1_8 = 0, z1_8 = 0,x1next_8 = 0, z1next_8 = 0,x2_8 = 0, z2_8 = 0,x2next_8 = 0, z2next_8 = 0,u1_8 = 0, u1_attacked_8 = 0,y1_8 = 0, y2_8 = 0, x1_9 = 0, z1_9 = 0,x1next_9 = 0, z1next_9 = 0,x2_9 = 0, z2_9 = 0,x2next_9 = 0, z2next_9 = 0,u1_9 = 0, u1_attacked_9 = 0,y1_9 = 0, y2_9 = 0, x1_10 = 0, z1_10 = 0,x1next_10 = 0, z1next_10 = 0,x2_10 = 0, z2_10 = 0,x2next_10 = 0, z2next_10 = 0,u1_10 = 0, u1_attacked_10 = 0,y1_10 = 0, y2_10 = 0, x1_11 = 0, z1_11 = 0,x1next_11 = 0, z1next_11 = 0,x2_11 = 0, z2_11 = 0,x2next_11 = 0, z2next_11 = 0,u1_11 = 0, u1_attacked_11 = 0,y1_11 = 0, y2_11 = 0, x1_12 = 0, z1_12 = 0,x1next_12 = 0, z1next_12 = 0,x2_12 = 0, z2_12 = 0,x2next_12 = 0, z2next_12 = 0,u1_12 = 0, u1_attacked_12 = 0,y1_12 = 0, y2_12 = 0, x1_13 = 0, z1_13 = 0,x1next_13 = 0, z1next_13 = 0,x2_13 = 0, z2_13 = 0,x2next_13 = 0, z2next_13 = 0,u1_13 = 0, u1_attacked_13 = 0,y1_13 = 0, y2_13 = 0, x1_14 = 0, z1_14 = 0,x1next_14 = 0, z1next_14 = 0,x2_14 = 0, z2_14 = 0,x2next_14 = 0, z2next_14 = 0,u1_14 = 0, u1_attacked_14 = 0,y1_14 = 0, y2_14 = 0, ,x1_0 = 0, z1_0 = 0,x1next_0 = 0, z1next_0 = 0,x2_0 = 0, z2_0 = 0,x2next_0 = 0, z2next_0 = 0,u1_0 = 0, u1_attacked_0 = 0,y1_0 = 0, y2_0 = 0, x1_1 = 0, z1_1 = 0,x1next_1 = 0, z1next_1 = 0,x2_1 = 0, z2_1 = 0,x2next_1 = 0, z2next_1 = 0,u1_1 = 0, u1_attacked_1 = 0,y1_1 = 0, y2_1 = 0, x1_2 = 0, z1_2 = 0,x1next_2 = 0, z1next_2 = 0,x2_2 = 0, z2_2 = 0,x2next_2 = 0, z2next_2 = 0,u1_2 = 0, u1_attacked_2 = 0,y1_2 = 0, y2_2 = 0, x1_3 = 0, z1_3 = 0,x1next_3 = 0, z1next_3 = 0,x2_3 = 0, z2_3 = 0,x2next_3 = 0, z2next_3 = 0,u1_3 = 0, u1_attacked_3 = 0,y1_3 = 0, y2_3 = 0, x1_4 = 0, z1_4 = 0,x1next_4 = 0, z1next_4 = 0,x2_4 = 0, z2_4 = 0,x2next_4 = 0, z2next_4 = 0,u1_4 = 0, u1_attacked_4 = 0,y1_4 = 0, y2_4 = 0, x1_5 = 0, z1_5 = 0,x1next_5 = 0, z1next_5 = 0,x2_5 = 0, z2_5 = 0,x2next_5 = 0, z2next_5 = 0,u1_5 = 0, u1_attacked_5 = 0,y1_5 = 0, y2_5 = 0, x1_6 = 0, z1_6 = 0,x1next_6 = 0, z1next_6 = 0,x2_6 = 0, z2_6 = 0,x2next_6 = 0, z2next_6 = 0,u1_6 = 0, u1_attacked_6 = 0,y1_6 = 0, y2_6 = 0, x1_7 = 0, z1_7 = 0,x1next_7 = 0, z1next_7 = 0,x2_7 = 0, z2_7 = 0,x2next_7 = 0, z2next_7 = 0,u1_7 = 0, u1_attacked_7 = 0,y1_7 = 0, y2_7 = 0, x1_8 = 0, z1_8 = 0,x1next_8 = 0, z1next_8 = 0,x2_8 = 0, z2_8 = 0,x2next_8 = 0, z2next_8 = 0,u1_8 = 0, u1_attacked_8 = 0,y1_8 = 0, y2_8 = 0, x1_9 = 0, z1_9 = 0,x1next_9 = 0, z1next_9 = 0,x2_9 = 0, z2_9 = 0,x2next_9 = 0, z2next_9 = 0,u1_9 = 0, u1_attacked_9 = 0,y1_9 = 0, y2_9 = 0, x1_10 = 0, z1_10 = 0,x1next_10 = 0, z1next_10 = 0,x2_10 = 0, z2_10 = 0,x2next_10 = 0, z2next_10 = 0,u1_10 = 0, u1_attacked_10 = 0,y1_10 = 0, y2_10 = 0, x1_11 = 0, z1_11 = 0,x1next_11 = 0, z1next_11 = 0,x2_11 = 0, z2_11 = 0,x2next_11 = 0, z2next_11 = 0,u1_11 = 0, u1_attacked_11 = 0,y1_11 = 0, y2_11 = 0, x1_12 = 0, z1_12 = 0,x1next_12 = 0, z1next_12 = 0,x2_12 = 0, z2_12 = 0,x2next_12 = 0, z2next_12 = 0,u1_12 = 0, u1_attacked_12 = 0,y1_12 = 0, y2_12 = 0, x1_13 = 0, z1_13 = 0,x1next_13 = 0, z1next_13 = 0,x2_13 = 0, z2_13 = 0,x2next_13 = 0, z2next_13 = 0,u1_13 = 0, u1_attacked_13 = 0,y1_13 = 0, y2_13 = 0, x1_14 = 0, z1_14 = 0,x1next_14 = 0, z1next_14 = 0,x2_14 = 0, z2_14 = 0,x2next_14 = 0, z2next_14 = 0,u1_14 = 0, u1_attacked_14 = 0,y1_14 = 0, y2_14 = 0, x1_15 = 0, z1_15 = 0,x1next_15 = 0, z1next_15 = 0,x2_15 = 0, z2_15 = 0,x2next_15 = 0, z2next_15 = 0,u1_15 = 0, u1_attacked_15 = 0,y1_15 = 0, y2_15 = 0;
		int8_t syn = 0;

		//pattern=1;
		syn = nondet_int8();
		a1[0] = AttackFormat2(syn);
		syn = nondet_int8();
		a2[0] = AttackFormat2(syn);