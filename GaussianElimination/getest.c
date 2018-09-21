	
#include <stdio.h>
#include <stdlib.h>


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

int ge_fw(float *matrix , int row, int col){
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
	
	if (matrix == NULL){
		return -1; 
	}	
	
	if(sizeof(matrix[0]) != sizeof(float)){
		return -1; 	
	} 
	
	for (w=0; w < row;w++){
		for (i = 0; i<col; i++){
			matrix[w*col + i] = (float)matrix[w*col + i];  
		}	
	}  
	
	while (0==0) {
		for (w = cycle;w < row;w++){
			if (matrix[w*col + cycle] != 0){
			 	for (i=0; i< col;i++){
					temp[w*col + i] = matrix[cycle*col + i];
				}	
				
				for (i= 0; i < col; i++){
					matrix[cycle*col + i] = matrix[w*col + i];  
				}

				for (i=0;i<col; i++){
					matrix[w*col +i] = temp[w*col + i];
				}
				
			}  
			
		} 
		
		for (w = cycle+1; w < row;w++){
			if (matrix[w*col + cycle]!=0){
				scale = matrix[w*col + cycle]/matrix[cycle*col + cycle];
				for (i=0;i<col;i++){
					matrix[w*col + i] = matrix[w*col +i] -(scale*matrix[cycle*col + i]); 
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


int ge_bw(float *matrix , int row, int col){
	int w = 0;
	int i = 0;	
	int rank = 0;
	int cycle = 0;
	int check = 0;
	int small = 0; 
	float scale = 1; 
	float *temp;

	temp = (float*)malloc(sizeof(float)*row*col);

	if (row>col){
		small = col;
	}
	
	else {
		small = row;
	}
	
	for (w=0; w < row ;w++){
		for (i = 0; i<col; i++){
			if (matrix[w*col + i]>0){
				if (matrix[w*col + i]<0.001){
					matrix[w*col + i] = 0;
				}
			}
			else{
				if (matrix[w*col + i]>-0.001){
					matrix[w*col + i] = 0;
				}
			}
			matrix[w*col + i] = (float)matrix[w*col + i];  
		 

			
		}
	}	

		
	for (i=0;i<small;i++){
		if (matrix[i*col +i] != 0){
			rank = rank + 1;
		 
		}
	}

	
	if (rank==0){
	return -1; 
	}
	
	if (matrix == NULL){
		return -1; 
	}	
	
	if(sizeof(matrix[0]) != sizeof(float)){
		return -1; 	
	} 
	

	  
	
	while (0==0) {
	
			if (matrix[(rank-1)*col + (rank-1)] != 1){
				scale = matrix[(rank-1)*col + (rank-1)];
				for (i=0; i<col;i++){
					matrix[(rank-1)*col +i] = matrix[(rank-1)*col +i]/scale	; 
				}
				
			}  
			
	 
		
		for (w = rank-1; 0 < w;w = w-1){
			if (matrix[(w-1)*col + (rank-1)]!=0){
				scale = matrix[(w-1)*col + rank -1];
				for (i=0;i<col;i++){
					
					matrix[(w-1)*col + i] = matrix[(w-1)*col +i] -(scale*(matrix[(rank-1)*col + i])); 
					
				}
			}
		} 	
		rank = rank - 1;  
		if (rank == 0){
			free(temp);
			return 1;
		}	 	
		 
		
	} 
	 	
}




int main(void){
	
	float test[4][3]; 
	int r = 4;
	int co = 3;	
	int c = 0;
	int i = 0;

	 
		for (i=0;i<r;i++){
			for (c=0; c<co;c++){
				test[i][c] =i+c-2;
				

			}
		}

	printf("\n input matrix \n");
	printMatrix(*test,r,co);
	
	ge_fw(*test,r,co);

	ge_bw(*test,r,co);
	
	printf("\n output matrix \n");
	printMatrix(*test,r,co);

}

		
