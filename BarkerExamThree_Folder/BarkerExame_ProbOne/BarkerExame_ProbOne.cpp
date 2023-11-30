//Samuel Barker
//00100768
//sbarker1@my.athens.edu
//Exam 3, Problem One

//References:
// [1] https://www.geeksforgeeks.org/implementation-of-singleton-class-in-cpp/ 
// [2] https://refactoring.guru/design-patterns/singleton/cpp/example
// [3] https://refactoring.guru/design-patterns/facade/cpp/example
// [4] https://sourcemaking.com/design_patterns/facade/cpp/1

#include <iostream>
#include <string>

enum class ErrorLevel { SEVERE, ERROR, WARNING, INFO };
//Using provided code from instructions
struct ErrorContext {
     ErrorLevel errlevel;
     const char* logmsg;
};

// To test out when running program. 
void SDAOSlogger(struct ErrorContext& logcontext) 
{
     std::cout << "Logging - Level: ";
     switch (logcontext.errlevel) {
     case ErrorLevel::SEVERE:
          std::cout << "SEVERE";
          break;
     case ErrorLevel::ERROR:
          std::cout << "ERROR";
          break;
     case ErrorLevel::WARNING:
          std::cout << "WARNING";
          break;
     case ErrorLevel::INFO:
          std::cout << "INFO";
          break;
          //"enum defines four values"
     }

     std::cout << ", Message: " << logcontext.logmsg << std::endl;
}

class Logger  // C++ class using Singleton and Facade patterns
{ 
private:
// Singleton pattern: single instance of Logger [1]
     static Logger* instance;

// Private constructor for Singleton pattern
     Logger() {
     }


public:
           // Singleton pattern: Get instance of Logger [2]
     static Logger* getInstance() {
          if (!instance) {
               instance = new Logger();
          }
          return instance;
     }

     // Facade pattern: Log message based on error level [4]
     void logMessage(ErrorLevel errlevel, const std::string& message) {

          const char* cstr = message.c_str();

          ErrorContext logContext{ errlevel, cstr };
          SDAOSlogger(logContext);
     }

  // Facade pattern: use log messages for each error level [3]
     void logSevere(const std::string& message) {
          logMessage(ErrorLevel::SEVERE, message);
     }

     void logError(const std::string& message) {
          logMessage(ErrorLevel::ERROR, message);
     }

     void logWarning(const std::string& message) {
          logMessage(ErrorLevel::WARNING, message);
     }

     void logInfo(const std::string& message) {
          logMessage(ErrorLevel::INFO, message);
     }
};

// Singleton pattern: Initialize the static instance [1]
Logger* Logger::instance = nullptr;

// Test the Logger class
int main() {
     Logger* logger = Logger::getInstance(); // Facade pattern: Get the Logger instance

     // Facade pattern: Log messages using the Facade. Also, let's test this out by running this. Messages below print. 
     logger->logSevere("This is a SEVERE message...");
     logger->logError("This is an ERROR message...");
     logger->logWarning("This is a WARNING message...");
     logger->logInfo("This is a INFOrmational message...");

     return 0;
}
