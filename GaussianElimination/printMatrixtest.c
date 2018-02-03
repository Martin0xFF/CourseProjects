#include <stdio.h>
#include <stdlib.h> 
int printMatrix (float (*arrin), int dimx,int dimy);
int r = 5 ;
int c = 10;

int main(void){
	int size;
	float arr[r][c];
	int i;
	int y;

		for (i = 0; i < r; i++){
			for ( y = 0 ; y < c ; y++){
				arr[i][y] = (i+1)*(y+1);
				printf("%f ",arr[i][y]);
	 		//	printf("%d ",arr);
			//	printf("%d ",&arr[i][y]);


		
		}
	printf("\n");
	
	}
printf("end of reference list\n");
	
printMatrix(&arr[0][0],5,10);

/*scanf("%d", &size);
*c[0] = 'd';
x = (int *)(malloc(size*sizeof(int)));
c = (char *)(malloc(size*sizeof(int)));

x[0] = -15000;
c[0] = 'd';

printf( "value of in x is %d\n",x[0]);
printf(" value of ch x is %c\n",c[0]);

 */	

//free(x);
//free(c);
	return 0;
}

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
