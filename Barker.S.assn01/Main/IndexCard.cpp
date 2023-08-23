//Samuel Barker
//00100768
//sbarker1@my.athens.edu
//CS 417, Assign 1 - IndexCard.cpp

#include "IndexCard.h"

IndexCard::IndexCard(const std::string& keyword, int indexNumber, const std::string& content)
     : keyword(keyword), indexNumber(indexNumber), content(content) {}

std::string IndexCard::getKeyword() const {
     return keyword;
}

int IndexCard::getIndexNumber() const {
     return indexNumber;
}

std::string IndexCard::getContent() const {
     return content;
}
