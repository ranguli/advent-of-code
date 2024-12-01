#include <algorithm>
#include <cmath> 
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::ifstream file("input.txt");

    std::vector<int> leftNumbers;
    std::vector<int> rightNumbers;

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream lineParser(line);
        int left, right;

        lineParser >> left >> right;
        leftNumbers.push_back(left);
        rightNumbers.push_back(right);
    }

    std::sort(leftNumbers.begin(), leftNumbers.end());
    std::sort(rightNumbers.begin(), rightNumbers.end());
    
    int part1 = 0;

    for (size_t i = 0; i < leftNumbers.size(); ++i) {
        part1 += std::abs(leftNumbers[i] - rightNumbers[i]);
    }

    std::cout << "Part 1 result: " << part1 << "\n";

    int part2 = 0;

    for (size_t i = 0; i < leftNumbers.size(); ++i) {
        int count = std::count(rightNumbers.begin(), rightNumbers.end(), leftNumbers[i]);
        part2 += leftNumbers[i] * count;

    }
    
    std::cout << "Part 2 result: " << part2 << "\n";

    return 0;
}