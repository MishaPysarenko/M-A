
#include <iostream>

long long climbRecursive(int n, long long memo[])
{
    if (n <= 1)
        return 1;

    if (memo[n] != 0)
        return memo[n];

    memo[n] = climbRecursive(n - 1, memo)
            + climbRecursive(n - 2, memo);

    return memo[n];
}

long long climbStairs(int n)
{
    long long memo[46] = {};
    return climbRecursive(n, memo);
}

int main()
{
    std::cout << climbStairs(2) << '\n'; // 2
    std::cout << climbStairs(3) << '\n'; // 3
    std::cout << climbStairs(5) << '\n'; // 8

    return 0;
}
