module part1(SW,HEX0,HEX1);
	output[6:0] HEX0,HEX1;
	input[0:7]SW;
	
	dec_7_seg U1(SW[4:7],HEX1);
	dec_7_seg U0(SW[0:3],HEX0);
endmodule


module dec_7_seg(In,Disp);
	
	input[3:0]In;
	output[6:0]Disp;
	
	wire [3:0]x;
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