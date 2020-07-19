#include <iostream>
#include <vector>

template<typename TBasicType>
TBasicType Read() {
    TBasicType result;

    std::cin >> result;

    return result;
}

template<typename TBasicType>
auto ReadArray(size_t size) {
    std::vector<TBasicType> result(size);

    for (size_t i = 0; i < size; ++i) {
        std::cin >> result[i];
    }

    return result;
}

void SpeedUpIo() {
    std::cin.sync_with_stdio(false);
    std::cin.tie(nullptr);
}
