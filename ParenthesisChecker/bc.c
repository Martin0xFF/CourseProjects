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

int llnode_add_to_head( llnode **x, char value){
	if (x == NULL){return -1;}
	if (*x ==NULL){
		*x = (llnode *) malloc(sizeof(llnode));
		(*x)->value = value;
		(*x)->next = NULL;
		return 0;
	}else{
		llnode *temp = NULL;
		temp = (llnode *)malloc(sizeof(llnode));
		temp->value = value;
		temp->next = *x;
		*x = temp;
		return 0 ;
			
	}

}


/*
int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail((&((*x)->next)),value);
   }
}
*/
int push (llnode **x, char value){
	return llnode_add_to_head(x,value);  	
}


 
int pop(llnode **x, char *return_value){
	if (x == NULL) {return -1;}
	if(*x== NULL){return -1;}
	
	if ((*x)->next == NULL){
		*return_value = (*x)->value; 
		free(*x);
		*x = NULL;	
		return 0;
	}else{
		llnode *temp;
		*return_value =((*x)->value);
		temp = *x;
		*x = ((*x)->next);
		free(temp);
		temp = NULL;
		return 0; 
	}
	
}
/*
int peak(llnode *x,char *out){
    	if(x== NULL){
		*out = 'w';	
		return -1;
	}
	
	if ((x)->next == NULL){
		*out = (x)->value; 		
		return 0;
	}else{
		return peak((x->next), out);	
	}

}
*/

int peak(llnode **x,char *out){
    int rval = 0;
    rval = pop(x,out);

    if (rval == 0){
	push(x,*out);
	return 0;
    }
    else{
  	*out = 'w';
	return -1; 
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
      
      if((value =='(') || (value == '{') || (value == '[') ){
      push(&input_list,value);
      }

      top = ' ';
         
      if ((value ==')') || (value == '}') || (value == ']') ){  	
	 peak(&input_list, &top);
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
	n = n + 1 ;
       
   }
   
  if((rvalue == 0) && (input_list == NULL)) { 
     printf("PASS\n");  
    
  }else{ 
    printf("Fail,%d\n",n);

}

  i = 0;
  while(i != (-1)){
	i = pop(&input_list,&out); 
  }  
  
  return 0;
}
