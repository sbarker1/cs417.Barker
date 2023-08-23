//Samuel Barker
//00100768
//sbarker1@my.athens.edu
//CS 417, Assign 1 - Main.cpp

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include "Tree.h"

int main() {
     Tree cardTree;

     std::ifstream inputFile("index_cards.txt");
     std::string line;
     while (std::getline(inputFile, line)) {
          std::istringstream iss(line);
          std::string keyword;
          int indexNumber;
          std::string content;

          if (iss >> keyword >> indexNumber) {
               std::getline(iss, content);
               cardTree.insert(IndexCard(keyword, indexNumber, content));
          }
     }

     while (true) {
          std::cout << "Enter a keyword to search (or 'exit' to quit): ";
          std::string keyword;
          std::cin >> keyword;

          if (keyword == "exit") {
               break;
          }

          IndexCard* result = cardTree.search(keyword);
          if (result) {
               std::cout << "Index Number: " << result->getIndexNumber() << std::endl;
               std::cout << "Content: " << result->getContent() << std::endl;
          }
          else {
               std::cout << "Keyword not found." << std::endl;
          }
     }

     return 0;
}
