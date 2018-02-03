 /*
 * mic container to store data that is input with an
 * unknown number of items.
 *
 * Note how we get the data:
 * -while loop (because the number of iterations is unknown)
 * -scanf returns EOF, or End-Of-File, when "nothing" has been input
 * -for each iteration, we stuff the input data into a linked list
 *
 * Usage:
 * gcc getData.c
 * echo "1 2 3 4 5 6 7 8     9      10" | ./a.out
 * should report 10 items read and dump it out
 * -> white space is ignored (space, tab, return)
 *
 * Assignment:
 * -modify this code so that it handles input "char" data
 * rather than ints (trivial modification)
 * echo "abcdef" | ./a.out
 * should report 7 items read
 * (white space is representable by the char hence the
 * final return you enter is stored as a char)
 */

#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int push (llnode **x, char value){
	return llnode_add_to_tail(x,value);  	
}
 
int pop(llnode **x, char *return_value){
	if (x == NULL) { return -1;}
	if(*x== NULL){return -1;}
	if ((*x)->next == NULL){
		*return_value = (*x)->value; 
		free(*x);
		*x = NULL;		
		return 0 ; 
	}else{
		return pop(&((*x)->next), return_value);	
	}
	
}

int peak(llnode *x,char *out){
    int rval = 0;
    rval = pop(&x,out);

    if (!(rval == 0)){
	
    }
    else{
   	push(&x,*out);
    } 
}


int main(void) {
   int n=0;
   int i; 
   char value=' ';
   char top = ' ';
   char out = ' ';
   int rvalue=0;
   llnode *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      n=n+1;
      if((value =='(') || (value == '{') || (value == '[') ){
      push(&input_list,value);
      }
      top = ' ';

      peak(input_list, &top);
     
      if ( (value ==')') || (value == '}') || (value == ']') ){  	
	if((value ==')') && (top == '(')){
		rvalue = pop(&input_list,&out);
	}
	else if ((value == '}') && (top == '{')) {
		rvalue = pop(&input_list,&out);
	}
	else if ((value == ']') && (top == '[')) {
		rvalue = pop(&input_list,&out);
	}else{
	rvalue = -1;
	break;}	
     }
       
   }
   
  if((rvalue == 0) && (input_list == NULL)) { 
     printf("PASS\n");  
    
  }else{ 
    printf("Fail,%d\n",n);

}
  /* for (i=0; i<n;i = i++){ 
   rvalue = pop(&input_list,&out);
   printf("%c\n",out);
   out = ' ';
   } 
*/
   return 0;
}
