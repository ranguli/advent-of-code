#include <fstream>
#include <iostream>
#include <sstream>
#include <regex>
#include <string>

int main() {
    std::ifstream file("input.txt");

    // Read the entire file into a string
    std::ostringstream buffer;
    buffer << file.rdbuf();
    std::string fileContent = buffer.str();

    std::regex pattern(R"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))");

    auto begin = std::sregex_iterator(fileContent.begin(), fileContent.end(), pattern);
    auto end = std::sregex_iterator();

    int part2 = 0;

    bool doing = true;

    for (auto it = begin; it != end; ++it) {
        std::smatch match = *it;

        if (match.str(0) == "do()") {
            doing = true;
            continue;
        } 
        if(match.str(0) == "don't()") {
            doing = false;
            continue;
        } 
        
        if (doing) {
            int num1 = std::stoi(match.str(1));
            int num2 = std::stoi(match.str(2));
            
            part2 += num1 * num2;
        }
    }

    std::cout << "Part 2 result: " << part2 << "\n";

    return 0;
}



