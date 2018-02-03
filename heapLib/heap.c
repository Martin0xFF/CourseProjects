#include<stdlib.h>
#include<stdio.h>

typedef struct{
   int *store;
   unsigned int end;
   unsigned int size; 		
}HeapType;
/* Maping heap tree Rep to Array, left root = index*2+1
	to goback to partent (fromleft) parent = leftchild (index-1)/2 
 * */

int initHeap(HeapType *pHeap,int size);
int inorder(HeapType *pHeap,int **output,int *o_size );
int preorder(HeapType *pHeap,int **output,int *o_size) ;
int postorder(HeapType *pHeap,int **output,int *o_size);



int initHeap(HeapType *pHeap,int size){
	if (pHeap==NULL){return -1;}
	(pHeap->store) = (int *) malloc(sizeof(int)*size);
	pHeap->size = size;
	pHeap->end = 0; /* Begin at Index 0, it is the first invalid location*/ 
	return 0; 
}
int preorder(HeapType *pHeap,int **output,int *o_size) {
	int indexNode = 0;
	if (pHeap == NULL){return -1;}
	if (output == NULL){return -1;}
	*output = (int *)malloc(sizeof(int)*pHeap->end);
	Traverse(pHeap,output,0,1);
	return 0;
}

int inorder(HeapType *pHeap,int **output,int *o_size ){
	int indexNode = 0;
	if (pHeap == NULL){return -1;}
	if (output == NULL){return -1;}
	*output = (int *)malloc(sizeof(int)*pHeap->end);
	Traverse(pHeap,output,0,2);
	return 0;		
}

int postorder(HeapType *pHeap,int **output,int *o_size){
	int indexNode = 0;
	if (pHeap == NULL){return -1;}
	if (output == NULL){return -1;}
	*output = (int *)malloc(sizeof(int)*pHeap->end);
	Traverse(pHeap,output,0,3);
	return 0;	
}

/*Traverse is a genearl Helper, the flag put in determines the type of processing 1-preorder 2- inorder 3-postorder*/
int Traverse(HeapType *pHeap,int **output, int location,unsigned int flag ){
	if (location >= (pHeap->end)){return -1;}

	if (flag == 1){	printf("%d ",pHeap->store[location]);}
	
	Traverse(pHeap,output,location*2+1, flag);

	if (flag == 2){	printf("%d ",pHeap->store[location]);}

	Traverse(pHeap,output,location*2+2,flag);
	
	if (flag == 3){	printf("%d ",pHeap->store[location]);}
	
	return 0;

		
}


