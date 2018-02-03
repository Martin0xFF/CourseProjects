
int printMatrix (float (*arrin), int dimx,int dimy){
	int n = 0; 
	int m = 0;
 
	for (n = 0; n < dimx ; n++){
		for (m = 0 ; m < dimy ; m++){


			printf("%8.3f ",arrin[dimy*n+m]);
			}
		printf("\n");

	
	} return 0;

}

int ge_fw(float *matrix , int row, int col,float *matrix_out){
	int w = 0;
	int i = 0;	
	int small;
	int cycle = 0;
	float scale = 1; 
	int check = 0;
	float *temp;

	temp = (float*)malloc(sizeof(float)*row*col);

	if (row>col){
		small = col;
	}

	else {
		small = row;
	}
		
	if (matrix_out == NULL){
		return -1; 
	}
	if (matrix == NULL){
		return -1; 
	}	
	
	if(sizeof(matrix[0]) != sizeof(float)){
		return -1; 	
	} 
	
	for (w=0; w < row;w++){
		for (i = 0; i<col; i++){
			matrix_out[w*col + i] = (float)matrix[w*col + i];  
		}	
	}  
	
	while (0==0) {
		for (w = cycle;w < row;w++){
			if (matrix_out[w*col + cycle] != 0){
			 	for (i=0; i< col;i++){
					temp[w*col + i] = matrix_out[cycle*col + i];
				}	
				
				for (i= 0; i < col; i++){
					matrix_out[cycle*col + i] = matrix_out[w*col + i];  
				}

				for (i=0;i<col; i++){
					matrix_out[w*col +i] = temp[w*col + i];
				}
				
			}  
			
		} 
		
		for (w = cycle+1; w < row;w++){
			if (matrix_out[w*col + cycle]!=0){
				scale = matrix_out[w*col + cycle]/matrix_out[cycle*col + cycle];
				for (i=0;i<col;i++){
					matrix_out[w*col + i] = matrix_out[w*col +i] -(scale*matrix_out[cycle*col + i]); 
				}
			}
		} 	
		cycle = cycle + 1;  
		if (cycle >= small){
			free(temp);
			return 1;
	} 	
		 
		
	} 
	 	
}


int ge_bw(float *matrix , int row, int col,float *matrix_out){
	int w = 0;
	int i = 0;	
	int rank = 0;
	int cycle = 0;
	int check = 0;
	int small = 0; 
	float scale = 1; 
	float *temp;
		
	if (matrix_out == NULL){
		return -1; 
	}	
	if (matrix == NULL){
		return -1; 
	}
	
	if(sizeof(matrix_out[0]) != sizeof(float)){
		return -1; 	
	} 	
	temp = (float*)malloc(sizeof(float)*row*col);
	
	
	if (row>col){
		small = col;
	}
	
	else {
		small = row;
	}
	for (w=0; w < row ;w++){
		for (i = 0; i<col; i++){
		matrix_out[w*col +i] = matrix[w*col +i]; 
		}
	}
	for (w=0; w < row ;w++){
		for (i = 0; i<col; i++){
			if (matrix_out[w*col + i]>0){
				if (matrix_out[w*col + i]<0.001){
					matrix_out[w*col + i] = 0;
				}
			}
			else{
				if (matrix_out[w*col + i]>-0.001){
					matrix_out[w*col + i] = 0;
				}
			}
			matrix_out[w*col + i] = (float)matrix_out[w*col + i];  
		 

			
		}
	}	

		
	for (i=0;i<small;i++){
		if (matrix_out[i*col +i] != 0){
			rank = rank + 1;
		 
		}
	}

	
	if (rank==0){
	return -1; 
	}

	

	

	  
	
	while (0==0) {
	
			if (matrix_out[(rank-1)*col + (rank-1)] != 1){
				scale = matrix_out[(rank-1)*col + (rank-1)];
				for (i=0; i<col;i++){
					matrix_out[(rank-1)*col +i] = matrix_out[(rank-1)*col +i]/scale	; 
				}
				
			}  
			
	 
		
		for (w = rank-1; 0 < w;w = w-1){
			if (matrix_out[(w-1)*col + (rank-1)]!=0){
				scale = matrix_out[(w-1)*col + rank -1];
				for (i=0;i<col;i++){
					
					matrix_out[(w-1)*col + i] = matrix_out[(w-1)*col +i] -(scale*(matrix_out[(rank-1)*col + i])); 
					
				}
			}
		} 	
		rank = rank - 1;  
		if (rank == 0){
			free(temp);
			return 0;
		}	 	
		 
		
	} 
	 	
}


		
