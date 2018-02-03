#include <stdlib.h>
#include <stdio.h>
#include"heap.c"
int main(){
HeapType *theHeap;
int *out;
int size;
	
theHeap = (HeapType *)malloc(sizeof(HeapType));

	initHeap(theHeap,7);
	theHeap->store[0]=10;
	theHeap->store[1]=5;
	theHeap->store[2]=20;
	theHeap->store[3]=4;
	theHeap->store[4]=6;
	theHeap->store[5]=15;
	theHeap->store[6]=30;
	theHeap->end = 7;
	inorder(theHeap,&out,&size);
								
}
