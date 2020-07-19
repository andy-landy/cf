from lib import iter_single_cpp_lines


def test_no_includes():
    in_lines = [
        '#include <iostream>',
        '',
        'int main() {}'
    ]

    assert list(iter_single_cpp_lines(in_lines, ['.', 'nonexistent'])) == in_lines


def test_simple_includes():
    assert list(iter_single_cpp_lines(
        [
            '#include <io>',
            '#include <f1.h>',
            '#include <dir1/f1.h>',
            '#include <dir1/f1.h>',
            '#include <f0.h>',
            '#include <io>',
            '#include <dir2/f2.h>',
            '',
            'int fAll(int x) {return x + x + x}',
            '#include <dir2/f2.h>',
            'int main() {}',
        ], 
        ['test_dir', 'test_dir/dir1'], 
    )) == [
        '#include <io>',
        '#include <iostream>',
        '#include <vector>',
        'int f1(int x) {',
        '    return x + 1;',
        '}',
        '',
        'int f1(int x) {',
        '    return x + 0;',
        '}',
        '',
        '',
        'int f2(int x) {',
        '    return f1(x) + f0(x) + 1 - x;',
        '}',
        '',
        '',
        '',
        'int fAll(int x) {return x + x + x}',
        'int main() {}',
    ]
