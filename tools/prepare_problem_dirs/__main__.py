import argparse
import os
import shutil
from typing import List, NoReturn, Tuple, Iterator

import bs4
import requests



def iter_in_out_texts(contest: str, name: str) -> Iterator[Tuple[str, str]]:
    response = requests.get(f'https://codeforces.com/contest/{contest}/problem/{name}')
    response.raise_for_status()

    for sample_div in bs4.BeautifulSoup(response.text, features='html.parser')\
            .findAll('div', attrs={'class': 'sample-test'}):
        yield (
            sample_div.find('div', attrs={'class': 'input'}).find('pre').text.strip(),
            sample_div.find('div', attrs={'class': 'output'}).find('pre').text.strip(),
        )


def prepare_problem_dirs(at: str, ref_dir: str, names: List[str], contest: str) -> NoReturn:
    for name in names:
        dir_ = os.path.join(at, name)
        
        try:
            shutil.copytree(ref_dir, dir_, dirs_exist_ok=True)
        except shutil.Error:
            pass

        for i, (in_text, out_text) in enumerate(iter_in_out_texts(contest, name)):
            with open(os.path.join(dir_, f'in{i}'), 'w') as out:
                out.write(in_text)

            with open(os.path.join(dir_, f'out{i}'), 'w') as out:
                out.write(out_text)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ref-dir', required=True)
    parser.add_argument('--names', nargs='+', required=True)
    parser.add_argument('--contest', required=True)

    return parser.parse_args()


def main():
    args = parse_args()

    prepare_problem_dirs(at='.', ref_dir=args.ref_dir, names=args.names, contest=args.contest)


if __name__ == '__main__':
    main()
