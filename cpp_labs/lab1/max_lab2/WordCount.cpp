#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>
#include <iomanip>
#include <filesystem>

struct Counts {
    std::size_t lines = 0;
    std::size_t words = 0;
    std::size_t bytes = 0;
    std::size_t chars = 0;
};

Counts countFile(const std::string& filename) {
    Counts counts;
    std::ifstream file(filename, std::ios::binary);
    if (!file) {
        std::cerr << "Cannot open file: " << filename << std::endl;
        return counts;
    }

    std::string line;
    while (std::getline(file, line)) {
        ++counts.lines;
        counts.bytes += line.size() + 1; // +1 for newline

        bool inWord = false;
        for (char ch : line) {
            ++counts.chars;
            if (std::isspace(static_cast<unsigned char>(ch))) {
                if (inWord) inWord = false;
            } else {
                if (!inWord) {
                    inWord = true;
                    ++counts.words;
                }
            }
        }
    }

    if (!file.eof()) {
        file.clear();
        file.seekg(0, std::ios::end);
        counts.bytes = file.tellg();
    }

    return counts;
}

int main(int argc, char* argv[]) {
    std::unordered_set<std::string> options;
    std::vector<std::string> files;

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg.rfind("-", 0) == 0) {
            if (arg.rfind("--", 0) == 0) {
                options.insert(arg.substr(2));
            } else {
                for (std::size_t j = 1; j < arg.size(); ++j) {
                    switch (arg[j]) {
                        case 'l': options.insert("lines"); break;
                        case 'w': options.insert("words"); break;
                        case 'c': options.insert("bytes"); break;
                        case 'm': options.insert("chars"); break;
                        default:
                            std::cerr << "Unknown option: -" << arg[j] << std::endl;
                    }
                }
            }
        } else {
            files.push_back(arg);
        }
    }

    if (files.empty()) {
        std::cerr << "No input files specified." << std::endl;
        return 1;
    }

    for (const auto& filename : files) {
        Counts counts = countFile(filename);

        if (options.empty()) {
            std::cout << std::setw(7) << counts.lines
                      << std::setw(8) << counts.words
                      << std::setw(8) << counts.bytes
                      << " " << filename << std::endl;
        } else {
            if (options.count("lines")) std::cout << "lines: " << counts.lines << std::endl;
            if (options.count("words")) std::cout << "words: " << counts.words << std::endl;
            if (options.count("bytes")) std::cout << "bytes: " << counts.bytes << std::endl;
            if (options.count("chars")) std::cout << "chars: " << counts.chars << std::endl;
            std::cout << "file name: " << filename << std::endl;
        }
    }

    return 0;
}
