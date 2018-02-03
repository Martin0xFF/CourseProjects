#include <stdlib.h>
#include <stdio.h>
#include "avl.h"
/*~~~~`Avl~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
int qEnqueue(qNode **root,avlNode *val){
	if (root ==NULL){return -1;}
	if (*root== NULL){
		*root = (qNode *)malloc(sizeof(qNode)); 
		(*root)->pval = val;
		(*root)->nxt = NULL;
		return 0;
	}else{
		return qEnqueue(&((*root)->nxt),val);
	}

return 0;
}


int qDequeue(qNode **node,int *out){ /*Dequeue for the bst WIPPPPPP */
	avlNode *temp = NULL; 
	qNode *p = *node;
	
	if (node ==NULL){return -1;}
	if(*node == NULL){return -1;}
	if ((*node)->nxt == NULL){
		temp = (*node)->pval;
		free(*node);
		*node = NULL;
		*out =(temp)->val;
	}else{
		temp = (*node)->pval;	 
		*node = (*node)->nxt;
		free(p);
		*out =(temp)->val; 
	}
	
	
return 0;
}

int add_bst(avlNode **root,int val){
	if (root == NULL){return -1;}
	if (*root == NULL){
		*root = (avlNode *)malloc(sizeof(avlNode));;
		(*root)->val = val;
		(*root)->l = NULL;
		(*root)->r = NULL;
		return 0;	
	}else{
		if (val<(*root)->val){
			return add_bst(&((*root)->l),val);
	
		}else{
			return add_bst(&((*root)->r),val);
		}
	}
}

int ProcessAvlLevel(qNode **que){
	avlNode *temp = (*que)->pval;
	if (temp->l != NULL){
		qEnqueue(que,temp->l);
	}
	if (temp->r != NULL){
		qEnqueue(que,temp->r);
	}
	
return 0;			
}




int printAvlInOrder(avlNode *root){
	if (root == NULL){return 0;}
	printAvlInOrder(root->l);
	printf("%d\n",root->val);
	printAvlInOrder(root->r);
	return 0;
}

int printAvlLevelOrder(avlNode *root){
	qNode *fillMe = NULL;
	int *out ;
	fillMe = (qNode *)malloc(sizeof(qNode));
	fillMe->pval = root;
	fillMe->nxt = NULL;

	while (fillMe != NULL){
		ProcessAvlLevel(&fillMe);
		qDequeue(&fillMe,out);
		printf("%d ",*out);
	}		
	printf("\n");
	
return 0; 	
}


/*~~~~`Avl~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

int isAVL(avlNode **root){
	int out;
	out = 0;	

	if (root==NULL){return -1;}
	if (*root==NULL){return -1;}

	ProccessInOrder(*root,&out);
	/*printf("outVal is %d\n",out);*/
	return out;
}
int ProccessInOrder(avlNode *root,int *outVal){
	if (root == NULL){return -1;}
	

	ProccessInOrder(root->l,outVal);
 	ProccessInOrder(root->r,outVal);
        if (compare(root) != 0 ){
		*outVal = -1; 
	}
	
	return 0;
}

int compare(avlNode *root){
	int maxl;
	int maxr;
	int counter;
	maxl = 0;
	maxr = 0;
	counter = 1;
	/*Calc Left then right*/
	/*printf("NewNode\n\n");*/
	depthCalc(root->l,counter,&maxl);
	depthCalc(root->r,counter,&maxr);
	/*printf("maxl,%d, maxr %d\n",maxl,maxr);
	printf("difference, %d\n",(maxr-maxl));*/
	if ( ((maxr-maxl) > 1)||((maxr-maxl)< -1) ){
	return -1;
	} 
	return 0;		
}

int compareDepth(avlNode *root){
	int maxl;
	int maxr;
	int counter;
	maxl = 0;
	maxr = 0;
	counter = 1;
	/*Calc Left then right*/
	/*printf("NewNode\n\n");*/
	depthCalc(root->l,counter,&maxl);
	depthCalc(root->r,counter,&maxr);
	/*printf("maxl,%d, maxr %d\n",maxl,maxr);
	printf("difference, %d\n",(maxr-maxl));*/
	return (maxr-maxl);		
}


int depthCalc(avlNode *root,int currentDepth,int *maxDepth){
	if (root == NULL){return 0;}
	if (*maxDepth < currentDepth){*maxDepth = currentDepth;}
	
/*	printf("madDepth is %d, Current Depth is %d,pointer is %d\n",*maxDepth,currentDepth,root);*/
	depthCalc(root->l,currentDepth+1,maxDepth);
	depthCalc(root->r,currentDepth+1,maxDepth);
	return 0;
}




int rotate(avlNode **root,unsigned int Left0_Right1){
	avlNode *inter;
	inter = NULL;

	if (root==NULL){return -1;}
	if (*root==NULL){return -1;}
	
	if (Left0_Right1 == 0){
		inter = *root; /*Call inter A*/
		
		*root = (*root)->r; /*root is now B */
		inter->r = (*root)->l;
		(*root)->l = inter;	
	}else{
		inter = *root; /*Call inter A*/
		
		*root = (*root)->l; /*root is now B */
		inter->l = (*root)->r;
		(*root)->r = inter;	

	}

	return 0;

}
int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1){
	avlNode *temp;
	int flag;
	
	flag = 0;	
	temp = *root;

	if (root==NULL){return -1;}
	if (*root==NULL){return -1;}
	if (MajLMinR0_MajRMinL1 == 0){
		while(temp !=NULL){
			
			
			temp = temp->r;/* Keep going down right branch until problematic node is found*/
			if ((temp) !=NULL){
				if (compareDepth(temp->r)<0){ /*if the difference is less than zero we have an imbalance on the left side, need a right rotatio*/
				/*	printf("value of node %d\n\n",(temp)->val);*/
					rotate(&(temp)->r,1);
					/*printf("New Node value%d\n\n",(temp)->val);*/
					break;
				}
			}

		}
		rotate(root,0);
	}else{
		while(temp !=NULL){
					
			temp = (temp)->l;/* Keep going down Left branch until problematic node is found*/
		
			if (temp !=NULL){
				if (compareDepth(temp->l)>0 ){ /*if the difference is greater than zero we have an imbalance on the right side, need a left rotatio*/		
					rotate(&(temp->l),0);
					break;
				}
			}
		}
		rotate(root,1);


	}

	return 0;

	
	
	


}

