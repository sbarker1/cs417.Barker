//Samuel Barker
//00100768
//sbarker1@my.athens.edu
//CS 417, Assign 1 - IndexCard.h

#ifndef INDEXCARD_H
#define INDEXCARD_H

#include <string>

class IndexCard {
private:
     std::string keyword;
     int indexNumber;
     std::string content;

public:
     IndexCard(const std::string& keyword, int indexNumber, const std::string& content);
     std::string getKeyword() const;
     int getIndexNumber() const;
     std::string getContent() const;
};

#endif 
