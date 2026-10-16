
#include <iostream>

int fibonacci(int n)
{
    if (n <= 1)
        return n;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main()
{
    std::cout << fibonacci(2) << '\n'; // 1
    std::cout << fibonacci(3) << '\n'; // 2
    std::cout << fibonacci(4) << '\n'; // 3

    return 0;
}
