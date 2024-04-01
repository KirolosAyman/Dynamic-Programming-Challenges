#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<long long, long long> memo;

long long grid_traveler(int m, int n) {
    long long key = m * 1000000LL + n;
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }
    if (m == 1 && n == 1) {
        return 1;
    }
    if (m == 0 || n == 0) {
        return 0;
    }
    memo[key] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1);
    return memo[key];
}

int main() {
    cout << grid_traveler(18, 18) << std::endl;
    return 0;
}
