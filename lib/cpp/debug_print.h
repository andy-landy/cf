#include <iostream>
#include <map>
#include <vector>

template<typename TOstream, typename TValue>
TOstream &operator<<(TOstream &out, const std::vector<TValue> &values) {
    out << '[';

    for (const auto &value: values) {
        out << value << ", ";
    }

    return out << ']';
}

template<typename TOstream, typename TKey, typename TValue, typename TCmp>
TOstream &operator<<(TOstream &out, const std::map<TKey, TValue, TCmp> &keyToValue) {
    out << '{';

    for (const auto &[key, value]: keyToValue) {
        out << key << ": " << value << ", ";
    }

    return out << '}';
}
