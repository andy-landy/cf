
#include <lib/cpp/utils_logo.h>

#include <lib/cpp/debug_print.h>
#include <lib/cpp/include_stl.h>
#include <lib/cpp/read.h>

using namespace std;

void SolveOne();

int main() {
    SpeedUpIo();

    for (size_t case_ = 0, numCases = Read<size_t>(); case_ < numCases; ++case_) {
        SolveOne();
        cout << endl;
    }

    return 0;
}

#include <lib/cpp/solve_logo.h>
