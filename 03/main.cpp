#include <algorithm>
#include <iostream>
#include <vector>
#include <ranges>
#include <fstream>
#include <expected>

auto from_file(std::string &&filename) -> std::expected<std::vector<std::string>, std::string> {
    std::ifstream file(filename);
    if (!file.is_open()) {
        return std::unexpected("failed to open file");
    }
    auto ret = std::vector<std::string>{};
    while (!file.eof()) {
        std::string line;
        std::getline(file, line);
        ret.emplace_back(line);
    }
    return ret;

}

auto max_two_jigs(const std::string &jigs) -> std::pair<int, int> {
    auto greatest_pair = std::make_pair(0, 0);
    for (int i = 0; jigs.size() > i; i++) {
        const char c = jigs[i];
        if (const int char_to_int = c - '0'; char_to_int > greatest_pair.first && i != jigs.size() - 1) {
            greatest_pair.first = char_to_int;
            greatest_pair.second = -1;
        } else if (char_to_int > greatest_pair.second) {
            greatest_pair.second = char_to_int;
        }
    }
    return greatest_pair;
}

auto max_twelve_jigs(const std::string &jigs) -> size_t {
    size_t ret = 0;
    int start_idx = 0;
    for (int rem = 12; rem > 0; rem--) {
        size_t greatest = 0;
        for (int i = start_idx; jigs.size() > i; i++) {
            const char c = jigs[i];
            if (const size_t char_to_int = c - '0'; char_to_int > greatest && (jigs.size() - i) >= rem) {
                greatest = char_to_int;
                start_idx = i + 1;
            }
        }
        ret = ret * 10 + greatest;
    }
    return ret;
}

auto main() -> int {
    using std::ranges::fold_left;
    auto jigs = from_file("input.txt");
    if (!jigs.has_value()) {
        std::cerr << jigs.error() << std::endl;
        return 1;
    }
    // part 1
    std::cout << fold_left(jigs.value(),0,[](int a,const auto &v) {
        auto greatest_pair = max_two_jigs(v);
        return a + greatest_pair.first * 10 + greatest_pair.second;
    }) << '\n';
    // part 2
    constexpr size_t init = 0;
    std::cout <<  fold_left(jigs.value(),init,[](size_t a,auto &v) -> size_t {return a + max_twelve_jigs(v);}) << '\n';
    return 0;
}