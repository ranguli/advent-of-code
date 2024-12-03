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

    std::regex pattern(R"(mul\((\d{1,3}),(\d{1,3})\))");

    auto begin = std::sregex_iterator(fileContent.begin(), fileContent.end(), pattern);
    auto end = std::sregex_iterator();

    int part1 = 0;

    for (auto it = begin; it != end; ++it) {
        std::smatch match = *it;

        int num1 = std::stoi(match.str(1));
        int num2 = std::stoi(match.str(2));

        part1 += num1 * num2;
    }

    std::cout << "Part 1 result: " << part1 << "\n";

    return 0;
}