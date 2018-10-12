module part3(SW,LEDR);
		input [8:0]SW;
		output[8:0]LEDR;
		
		wire [3:0]s;
		wire [4:0]c;
		
		assign c[0] = SW[8];
		FA U0(SW[0],SW[4],c[0],c[1],s[0]);
		FA U1(SW[1],SW[5],c[1],c[2],s[1]);
		FA U2(SW[2],SW[6],c[2],c[3],s[2]);
		FA U3(SW[3],SW[7],c[3],c[4],s[3]);
		
		assign LEDR[0] = s[0];
		assign LEDR[1] = s[1];	
		assign LEDR[2] = s[2];
		assign LEDR[3] = s[3];
		
		assign LEDR[4] = c[4];
		
endmodule

module FA(a,b,cin,cout,s); 

	input a,b,cin;
	output cout,s;
	
	assign cout = (a&cin)|(b&a)|(b&cin);
	assign s = ((~b)&(~a)&(cin))|((~b)&(a)&(~cin))|(b&a&cin)|(b&(~a)&(~cin));

endmodule

