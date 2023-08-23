//Samuel Barker
//00100768
//sbarker1@my.athens.edu
//CS 417, Assign 1 - Node.h

#ifndef NODE_H
#define NODE_H

#include "IndexCard.h"

class Node {
private:
     IndexCard indexCard;
     Node* left;
     Node* right;

public:
     Node(const IndexCard& indexCard);
     friend class Tree;
};

#endif 
