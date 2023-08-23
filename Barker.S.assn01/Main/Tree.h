//Samuel Barker
//00100768
//sbarker1@my.athens.edu
//CS 417, Assign 1 - Tree.h

#ifndef TREE_H
#define TREE_H

#include "Node.h"
#include <vector>

class Tree {
private:
     Node* root;
     void destroyTree(Node* node);
     void insertNode(Node*& node, const IndexCard& indexCard);
     IndexCard* searchNode(Node* node, const std::string& keyword);
     void inOrderTraversal(Node* node, std::vector<IndexCard>& result);

public:
     Tree();
     ~Tree();
     void insert(const IndexCard& indexCard);
     IndexCard* search(const std::string& keyword);
     std::vector<IndexCard> traverse();
};

#endif 
