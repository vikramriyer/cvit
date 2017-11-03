#include <stdio.h>
#include <stdlib.h>


struct node {
    int data;
    struct node *next;
};

struct node* head;


void insert(int data){
    struct node *t = head;
    if ( head == NULL ){
        head = (struct node*)(malloc(sizeof(struct node)));
        head->data = data;
        head->next = NULL;
        return;
    }

    while ( t -> next != NULL){
        t = t->next;
    }


    t->next = (struct node*)(malloc(sizeof(struct node)));
    t->next->next = NULL;
    t->next->data = data;
}

void debug(){
    struct node *t = head;
    while(t!=NULL){
        printf("%d ", t->data);;;
        t = t->next;
    }
    printf("\n");

}

void reverse(){
    /*
        p1 - pointer to the previous node
        p2 - pointer to the current node
        p3 - pointer to the next node

        Algo:
        interate through the linked list and keep reversing the link of the current
        node to the previous one until the end.

        For ex: if the nodes are 1->2->3->NULL, p2 is at '1'
        iteration 1: NULL<-1 2->3->NULL, p2 is at '2'
        iteration 2: NULL<-1<-2 3->NULL, p2 is at '3'
        iteration 2: NULL<-1<-2<-3
    */
    struct node *p1, *p2, *p3;
    p1 = NULL;
    p2 = head;
    while(p2){
        p3 = p2->next;
        p2->next = p1;
        p1 = p2;
        p2 = p3;
    }
    head = p1;
}

int main(int argc, char *argv[]){
    head = NULL;
    int i;
    for(i=1; i<=10; i++){
        insert(i);
    }
    debug();
    reverse();
    debug();
    return 0;
}
