//Samuel Barker
//00100768
//sbarker1@my.athens.edu
//CS 417, Assign 1 - Tree.cpp

#include "Tree.h"

Tree::Tree() : root(nullptr) {}

Tree::~Tree() {
     destroyTree(root);
}

void Tree::destroyTree(Node* node) {
     if (node) {
          destroyTree(node->left);
          destroyTree(node->right);
          delete node;
     }
}

void Tree::insert(const IndexCard& indexCard) {
     insertNode(root, indexCard);
}

void Tree::insertNode(Node*& node, const IndexCard& indexCard) {
     if (!node) {
          node = new Node(indexCard);
     }
     else if (indexCard.getKeyword() < node->indexCard.getKeyword()) {
          insertNode(node->left, indexCard);
     }
     else {
          insertNode(node->right, indexCard);
     }
}

IndexCard* Tree::search(const std::string& keyword) {
     return searchNode(root, keyword);
}

IndexCard* Tree::searchNode(Node* node, const std::string& keyword) {
     if (!node) {
          return nullptr;
     }

     if (keyword == node->indexCard.getKeyword()) {
          return &(node->indexCard);
     }
     else if (keyword < node->indexCard.getKeyword()) {
          return searchNode(node->left, keyword);
     }
     else {
          return searchNode(node->right, keyword);
     }
}

std::vector<IndexCard> Tree::traverse() {
     std::vector<IndexCard> result;
     inOrderTraversal(root, result);
     return result;
}

void Tree::inOrderTraversal(Node* node, std::vector<IndexCard>& result) {
     if (node) {
          inOrderTraversal(node->left, result);
          result.push_back(node->indexCard);
          inOrderTraversal(node->right, result);
     }
}
