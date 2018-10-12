module part2(SW,HEX0,HEX1);
	wire [3:0]v,a,out;
	wire z; 
	
	output[6:0] HEX0,HEX1;
	input[3:0]SW;
	
	assign v = SW; //Conversion to v for clarity
	
	
	assign z =((v[3])&(v[2]))|((v[3])&(v[1])) ; //z tells us when there is a decimal carry (>9)
	
	
	inter_a A0(v,a); // Generate output in the case of v >9
	mux2to1_4(v,a,z,out);//Pick the proper output based on z

	dec_7_car U1(z,HEX1);  //display decimal carry 
	dec_7_seg U0(out,HEX0);//display place zero
	
	
endmodule



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
	
	assign Out[0]= 0;
 	assign Out[1]= (V[3])&(V[2])&(V[1]);
	assign Out[2]= (~V[1]);
	assign Out[3]= V[0]&V[3];

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

module dec_7_seg(In,Disp);//circuit A
	
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