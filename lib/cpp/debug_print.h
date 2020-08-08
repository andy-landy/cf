#include <iostream>
#include <list>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <vector>


// - concepts - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

template<typename TIterable>
concept CIsIterable = requires(TIterable iterable) {
    { *(++iterable.begin() != iterable.end() ? iterable.begin() : iterable.end()) }
        -> typename TIterable::value_type;
};

template<typename TMapping>
concept CIsMapping = requires(TMapping mapping) {
    { *(++mapping.begin() != mapping.end() ? mapping.begin() : mapping.end()) } 
        -> std::pair<typename TMapping::key_type, typename TMapping::mapped_type>;
};

// - print functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

template<CIsIterable TIterable>
void PrintIterable(std::ostream &out, const TIterable &values, char openChar = '(',
        char closeChar = ')', char delimChar = ',') {
    out << openChar;
    for (const auto &value: values) {
        out << value << delimChar << ' ';
    }
    out << closeChar;
}

template<CIsMapping TMapping>
void PrintMapping(std::ostream &out, const TMapping &mapping) {
    out << '{';
    for (const auto &[key, value]: mapping) {
        out << key << ": " << value << ", ";
    }
    out << '}';
}

// - operator overrides - - - - - - - - - - - - - - - - - - - - - - - - - - -  -

template<typename TValue>
std::ostream &operator<<(std::ostream &out, const std::vector<TValue> &values) {
    PrintIterable<std::vector<TValue>>(out, values, '[', ']', ',');
    return out;
}

template<typename TValue>
std::ostream &operator<<(std::ostream &out, const std::list<TValue> &values) {
    PrintIterable<std::list<TValue>>(out, values, '[', ']', '>');
    return out;
}

template<typename TValue>
std::ostream &operator<<(std::ostream &out, const std::set<TValue> &values) {
    PrintIterable<std::set<TValue>>(out, values, '{', '}', ',');
    return out;
}

template<typename TValue>
std::ostream &operator<<(std::ostream &out, const std::unordered_set<TValue> &values) {
    PrintIterable<std::unordered_set<TValue>>(out, values, '{', '}', ',');
    return out;
}

template<typename TIterable>
    requires CIsIterable<TIterable> 
        && !CIsMapping<TIterable> 
        && !std::is_base_of<std::string, TIterable>::value
std::ostream &operator<<(std::ostream &out, const TIterable &values) {
    PrintIterable<TIterable>(out, values, '(', ')', ',');
    return out;
}

template<CIsMapping TMapping>
std::ostream &operator<<(std::ostream &out, const TMapping mapping) {
    PrintMapping<TMapping>(out, mapping);
    return out;
}
