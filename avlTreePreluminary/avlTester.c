#include <stdio.h>
#include <stdlib.h>
#include "avl.h"
int main(){	
	int c;
	int w;
	int out;
	avlNode *root;
	avlNode *doot;
	avlNode *shoot;
	avlNode *woot;	
	avlNode *LR;
	avlNode *RL;
	
	c = 0;
	w =0;
	doot =NULL;
	root = NULL;
	shoot =NULL;
	woot = NULL;
	LR = NULL; 
	RL = NULL;
	out = 0;

	add_bst(&root,5); 
	add_bst(&root,3); 
	add_bst(&root,1); 
	add_bst(&root,4); 
	add_bst(&root,7);
 	add_bst(&root,6);
	add_bst(&root,8); 
	printAvlInOrder(root);
	printAvlLevelOrder(root);
	printf ("testing depth\n\n");
	depthCalc(root,c,&w);
	
	printf("Depth is %d\n",w);
	printf("testing Comparision\n");
	printf("Difference in Depth is  %d\n",compare(root));
	
	printf("Testing isAVL \n");
	out = isAVL(&root);
	printf("isAvl Test:\n\nThis should return 0 for true %d\n\n",out);
	printf("New Tree Heavy imbalance on Right `doot`\n\n");
	add_bst(&doot,1); 
	add_bst(&doot,2); 
	add_bst(&doot,3); 
	add_bst(&doot,4); 
	add_bst(&doot,5);
 	add_bst(&doot,6);
	add_bst(&doot,7); 
	printAvlInOrder(doot);
	printAvlLevelOrder(doot);
	

	out = isAVL(&doot);
	printf("isAvl doot Test:\n\nthis should return -1 for false %d\n",out);
	printf("This is Shoot\n\n");
	add_bst(&shoot,5); 
	add_bst(&shoot,3); 
	add_bst(&shoot,100); 
	add_bst(&shoot,50); 
	add_bst(&shoot,150);
 	add_bst(&shoot,160);
	add_bst(&shoot,140); 
	
	out = 0;
	printAvlInOrder(shoot);
	printAvlLevelOrder(shoot);
	
	printf("Testing Rotation with shoot\n\n");
	out = isAVL(&shoot);
	printf("isAvl shoot Test:\n\n this should return -1 for false %d\n",out);

	rotate(&shoot,0);
	
	out = isAVL(&shoot);
	printf("isAvl Test:\n\nthis should return 0 for True %d\n",out);

	printAvlInOrder(shoot);
	printAvlLevelOrder(shoot);
	
	printf("Testing Right Rotation woot Begin\n");
	
	add_bst(&woot,100); 
	add_bst(&woot,50); 
	add_bst(&woot,40); 
	add_bst(&woot,50); 
	add_bst(&woot,30);
 	add_bst(&woot,175);
	add_bst(&woot,60); 
	printAvlInOrder(woot);

	out = 0;

	out = isAVL(&woot);
	printf("tisAvl Test:\n\nhis should return -1 for false %d\n",out);

	rotate(&woot,1);
	
	out = isAVL(&woot);
	printf("isAvl Test:\n\nthis should return 0 for True %d\n",out);

	printAvlInOrder(woot);



	add_bst(&LR,10); 
	add_bst(&LR,20); 
	add_bst(&LR,30); 
	add_bst(&LR,25); 

	out = 0;

	printf("Testing LR rotation Begin\n");
	printAvlInOrder(LR);
	printAvlLevelOrder(LR);

	out = isAVL(&LR);
	printf("isAVL Test:\n\n this should return -1 for false %d\n",out);

	dblrotate(&LR,0);
	
	out = isAVL(&LR);
	printf("this should return 0 for True %d\n\n",out);

	printAvlInOrder(LR);
	printAvlLevelOrder(LR);
	printf("Testing RL rotation with RL\n\n");
	
	add_bst(&RL,20); 
	add_bst(&RL,25); 
	add_bst(&RL,15); 
	add_bst(&RL,10); 
	add_bst(&RL,12);  
	out = 0;

	printAvlInOrder(RL);
	printAvlLevelOrder(RL);

	out = isAVL(&RL);
	printf("isAvl Test: \n\nthis should return -1 for false %d\n",out);

	dblrotate(&RL,1);
	
	out = isAVL(&RL);
	printf("isAVL Test:\n\nthis should return 0 for True %d\n",out);

	printAvlInOrder(RL);
	printAvlLevelOrder(RL);
	
	return 0; 


}

