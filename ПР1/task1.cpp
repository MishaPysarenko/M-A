
#include <iostream>
#include <string>

void reversePrint(const std::string& str, size_t index = 0)
{
    if (index == str.size())
        return;

    reversePrint(str, index + 1);
    std::cout << str[index];
}

int main()
{
    reversePrint("tiger"); // regit
    std::cout << '\n';
    return 0;
}
