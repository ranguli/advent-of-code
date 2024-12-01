#include <algorithm>
#include <cmath> 
#include <fstream>
#include <iostream>
#include <numeric>
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
    
    int result;

    // I could have replaced this with unreadable functional
    // slop for style points, but I didn't.
    for (size_t i = 0; i < leftNumbers.size(); ++i) {
        result += std::abs(leftNumbers[i] - rightNumbers[i]);
    }

    std::cout << "Result: " << result << "\n";
    return 0;
}