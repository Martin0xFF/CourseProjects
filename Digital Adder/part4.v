module part4(SW,LEDR,HEX0,HEX1,HEX3,HEX5);
	input [8:0]SW;
	output[9:0]LEDR;
	output[6:0] HEX0,HEX1,HEX3,HEX5;
		
	wire [3:0]v,a,out;
	wire z,push,cout; 
	
	BCD_summer sum0(SW,v,cout); //Conversion to v for clarity


	// Indication of sums LEDR[0] = s0
	assign LEDR[0]= v[0] ;
	assign LEDR[1]= v[1] ;
	assign LEDR[2]= v[2] ;
	assign LEDR[3]= v[3] ;
	
	// Indication of carryout
	assign LEDR[4]= cout;

	assign z =((v[3])&(v[2]))|((v[3])&(v[1])) ; //z tells us when there is a decimal carry (>9)
	
	assign LEDR[9] =((SW[3])&(SW[2]))|((SW[3])&(SW[1]))|((SW[7])&(SW[6]))|((SW[7])&(SW[5]));//Check for Error, X>9,Y>9	
	
	assign push= z|cout; //If there is a carry out or the sum is greater than 9, push to circuit a
	
	inter_a A0(v,a); // Generate output in the case of v >9
	mux2to1_4(v,a,push,out);//Pick the proper output based on push

	dec_7_car U1(push,HEX1);  //display decimal carry 
	dec_7_seg U0(out,HEX0);//display place zero
	
	dec_7_seg U3(SW[3:0],HEX3);
	dec_7_seg U5(SW[7:4],HEX5);
	
		
endmodule

//~~~~~~~~~~
module BCD_summer(In,Out,cout);
		input [8:0]In;
		output[3:0]Out;
		output cout;
		
		wire [3:0]s;
		wire [4:0]c;
		
		assign c[0] = In[8];
		FA U0(In[0],In[4],c[0],c[1],s[0]);
		FA U1(In[1],In[5],c[1],c[2],s[1]);
		FA U2(In[2],In[6],c[2],c[3],s[2]);
		FA U3(In[3],In[7],c[3],c[4],s[3]);
		
		assign Out[0] = s[0];
		assign Out[1] = s[1];	
		assign Out[2] = s[2];
		assign Out[3] = s[3];
		
		assign cout = c[4];
		
endmodule

module FA(a,b,cin,cout,s); 

	input a,b,cin;
	output cout,s;
	
	assign cout = (a&cin)|(b&a)|(b&cin);
	assign s = ((~b)&(~a)&(cin))|((~b)&(a)&(~cin))|(b&a&cin)|(b&(~a)&(~cin));

endmodule




//~~~~



module mux2to1_4(X,Y,s,Out);
    input[3:0]X,Y;
	 input s;
	 output[3:0] Out;
     
    assign Out[0] = (~s & X[0])|(s & Y[0]); // defining the values of the multiplexer
    assign Out[1] = (~s & X[1])|(s & Y[1]);
    assign Out[2] = (~s & X[2])|(s & Y[2]);
    assign Out[3] = (~s & X[3])|(s & Y[3]);
    
endmodule


module inter_a(V,Out);
	input [3:0]V;
	output [0:3]Out;
	
	assign Out[0]= (~V[3])&(~V[2])&(V[1]);
 	assign Out[1]= (~V[3])&(~V[2])&(~V[1])|((V[3])&(V[2])&(V[1]));
	assign Out[2]= ((V[3])&(V[2])&(~V[1]))|((~V[3])&(~V[2])&(~V[1]));
	assign Out[3]= ((~V[3])&(~V[2])&(V[0]))|((V[3])&(V[2])&(V[0]))|((V[3])&(V[1])&(V[0]));

endmodule

module dec_7_car(In,Disp);

	input In;
	output [6:0]Disp;

	assign Disp[0] =1 ;
	assign Disp[1] =~In ;
	assign Disp[2] =~In ;
	assign Disp[3] = 1;
	assign Disp[4] = 1;
	assign Disp[5] = 1;
	assign Disp[6] = 1;
	
endmodule

module dec_7_seg(In,Disp);
	
	input[3:0]In;
	output[6:0]Disp;
	
	wire [0:3]x;
	assign x = In; 
	
	//Logic was done with x[3] being the least significant bit and x[0] is the most
	assign Disp[0] = ((~x[0])&(~x[1])&(~x[2])&(x[3]))|((x[1])&(~x[2])&(~x[3]));
	
	assign Disp[1] = ((x[1])&(~x[2])&(x[3]))|((x[1])&(x[2])&(~x[3]));
	
	assign Disp[2] = (~x[1])&(x[2])&(~x[3]);
	
	assign Disp[3] = ((x[1])&(~x[2])&(~x[3]))|((~x[1])&(~x[2])&(x[3]))|((x[1])&(x[2])&(x[3]));
	
	assign Disp[4] = ((x[1])&(~x[2])&(~x[3]))|(x[3]);
	
	assign Disp[5] = ((~x[0])&(~x[1])&(x[3]))|((~x[1])&(x[2]))|((x[2])&(x[3]));
	
	assign Disp[6] = ((~x[0])&(~x[1])&(~x[2]))|((x[1])&(x[2])&(x[3]));


endmodule 