# cf
codeforces competitions automation

### example

```sh
$ ln -s /path/to/cf ~/cf

$ mkdir todays_competition
$ cd todays_competition
$ ~/cf/prepare_problem_dirs --contest 1379 --names A B C D E F1 F2

$ cd A
$ vim solve.cpp
$ ~/cf/test_cpp
# submit code via website

$ cd B
$ vim p.py
$ ~/cf/test_py
# submit code via website

$ cd C
...
```

### features

* makes a dir tree with code stubs
* downloads sample inputs and outputs
* allows local cpp includes, making a pretty single main.cpp
* tests the code against downloaded inputs and outputs


### conventions

* cpp code resides at solve.cpp
* cpp code is packed in main.cpp, binary name is a.out
* py code resides at p.py
* input names are "in$i", output names are "out$i" with i in 0..<some n>


