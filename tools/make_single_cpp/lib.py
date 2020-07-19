import os
import re
from typing import Iterator, Optional, List, Set, NoReturn


INCLUDE_PATTERN = re.compile('#include <(.*)>')
INCLUDE_TEMPLATE = '#include <{path}>'


def iter_single_cpp_lines(in_lines: Iterator[str], include_dirs: List[str]) -> Iterator[str]:
    seen_external_paths = set()
    out_lines = list()

    parse_lines(in_lines, include_dirs, set(), seen_external_paths, out_lines)

    yield from [INCLUDE_TEMPLATE.format(path=path) for path in sorted(seen_external_paths)]
    yield from out_lines


def get_include_path(line: str) -> Optional[str]:
    match = INCLUDE_PATTERN.match(line)

    return match and match.group(1)


def to_local_path(path: str, include_dirs: List[str]) -> Optional[str]:
    paths = [p for p in (os.path.join(dir_, path) for dir_ in include_dirs) if os.path.isfile(p)]

    return paths[0] if paths else None


def parse_lines(in_lines: Iterator[str], include_dirs: List[str], seen_local_paths: Set[str], 
                seen_external_paths: Set[str], out_lines: List[str]) -> NoReturn:
    for in_line in in_lines:
        path = get_include_path(in_line)

        if not path:
            out_lines.append(in_line.rstrip('\n'))
            continue

        local_path = to_local_path(path, include_dirs)

        if local_path:
            if local_path not in seen_local_paths:
                seen_local_paths.add(local_path)

                with open(local_path, 'r') as in_:
                    parse_lines(in_, include_dirs, seen_local_paths, seen_external_paths, out_lines)

        else:
            seen_external_paths.add(path)
