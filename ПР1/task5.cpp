
#include <iostream>
#include <iomanip>

double powerPositive(double x, long long n)
{
    if (n == 0)
        return 1.0;

    double half = powerPositive(x, n / 2);

    if (n % 2 == 0)
        return half * half;

    return half * half * x;
}

double myPow(double x, int n)
{
    long long exponent = n;

    if (exponent < 0)
        return 1.0 / powerPositive(x, -exponent);

    return powerPositive(x, exponent);
}

int main()
{
    std::cout << std::fixed << std::setprecision(5);

    std::cout << myPow(2.0, 10) << '\n'; // 1024.00000
    std::cout << myPow(2.1, 3) << '\n';  // 9.26100
    std::cout << myPow(2.0, -2) << '\n'; // 0.25000

    return 0;
}
