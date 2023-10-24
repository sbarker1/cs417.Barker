//Samuel Barker
//sbarker1@my.athens.edu
//Assignment 6, Problem 2

//References:
// https://www.geeksforgeeks.org/factory-method-for-designing-pattern/#
// https://www.modernescpp.com/index.php/factory-method/
// https://sourcemaking.com/design_patterns/factory_method/cpp/1

#include <iostream>
#include <string>

struct Office 
{
     std::string m_street;
     std::string m_city;
     int m_cubicle;
};

class Employee {
     friend class EmployeeFactory;  //I give permission to create Employee instances. 

private:
     std::string m_name;
     Office* m_office;

     Employee(const std::string& n, Office* o) : m_name(n), m_office(o) {}

public:
     Employee(const Employee& rhs) : m_name(rhs.m_name), m_office(new Office{ *rhs.m_office }) {}
     Employee& operator=(const Employee& rhs) {
          if (this == &rhs) return *this;
          m_name = rhs.m_name;
          m_office = new Office{ *rhs.m_office };

          //Copy name then create deep copy of office. 
          return *this;
     }

     friend std::ostream& operator<<(std::ostream& os, const Employee& o) {
          return os << o.m_name << " works at "
               << o.m_office->m_street << " " << o.m_office->m_city
               << " seats @" << o.m_office->m_cubicle;
     }
};

//Factory pattern is applied here:
class EmployeeFactory {
public:
     static Employee createEmployee(const std::string& name, const std::string& street, const std::string& city, int cubicle) {
          Office* office = new Office{ street, city, cubicle };
          return Employee(name, office);
     }
};

int main() 
{
     
     //Let's establish employee information 
     Employee employee1 = EmployeeFactory::createEmployee("Carol Perkins", "9000 Greenbrier Pkwy", "Madison", 253);
     Employee employee2 = EmployeeFactory::createEmployee("Tom Smith", "7817 Fanning Rd", "Huntsville", 164);

     
     std::cout << employee1 << std::endl;
     std::cout << employee2 << std::endl;

     return 0;
}
