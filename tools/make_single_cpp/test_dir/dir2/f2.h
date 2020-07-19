#include <f0.h>
#include <dir1/f1.h>

#include <iostream>

int f2(int x) {
    return f1(x) + f0(x) + 1 - x;
}


