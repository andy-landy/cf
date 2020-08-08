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
# now submit main.cpp via website

$ cd ../B
$ vim main.py
$ ~/cf/test_py
# now submit main.py via website

$ cd ../C
...
```

### features

* makes a dir tree with code stubs
* downloads sample inputs and outputs
* allows local cpp includes, making a pretty single main.cpp
* tests the code against downloaded inputs and outputs


### conventions

* cpp code to edit is solve.cpp
* cpp code to submit is main.cpp
* py code to edit and submit is main.py
* input names are "in$i", output names are "out$i" with i in 0..N, you can add some manually


