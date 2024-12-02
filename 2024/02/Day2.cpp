#include <algorithm>
#include <cmath> 
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

bool isStrictlySorted(const std::vector<int>& vec) {
    // Check for ascending order
    bool ascending = std::is_sorted(vec.begin(), vec.end()) &&
                     std::adjacent_find(vec.begin(), vec.end(), std::equal_to<>()) == vec.end();

    // Check for descending order
    bool descending = std::is_sorted(vec.rbegin(), vec.rend()) &&
                      std::adjacent_find(vec.rbegin(), vec.rend(), std::equal_to<>()) == vec.rend();

    return ascending || descending;
}

int main() {
    std::ifstream file("input.txt");

    std::string line;

    int safe_levels = 0;

    while (std::getline(file, line)) {
        std::istringstream lineParser(line);
        std::vector<int> report;
        int num;

        while (lineParser >> num) { // Extract each number from the line
            report.push_back(num);
        }

        auto isSorted = isStrictlySorted(report); 

        if (!isSorted) {
            continue;
        }
            
        bool variance = false;

        for (size_t i = 0; i < report.size() - 1; ++i) {
            if (std::abs(report[i] - report[i + 1]) > 3) {
                variance = true;
                break;
            }
        }

        if (!variance) {
            safe_levels++;
        }

        // Safety dampener
        /*
        for (size_t i = 0; i < report.size() - 1; ++i) {
            if (std::abs(report[i] - report[i + 1]) > 3) {
                variance = true;
                break;
            }
        }
        */
    }


    std::cout << "Part 1 result: " << safe_levels << "\n";
    return 0;
}