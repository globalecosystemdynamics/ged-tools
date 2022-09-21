# buildDataTable

This is a helper tool to consolidate output data from ALchemer surveys per
ecosystem. The desired output defined by the directory structure requirements 
in "mapeo procesos" file. 

# Project structure
buildtable/\
├── etc\
│   ├── mutualismo\
│   │   └── buildDataTable\_v2.py\
│   └── tmp\
│       ├── csv2json.py\
│       ├── parse2json.py\
│       └── regex-substitution.py\
├── README.md\
└── src\
    └── buildDataTable.py
    
* `./buildtable/src`: buildDataTable.py source.
* `./etc/mutualismo`: Contains alternate version of `buildDataTable.py` for
    "mutualismo" tasks.
* `./etc/tmp`: Contains helper examples of methods used in `buildDataTable.py`.

# Example

At `./buildtable/examples` a test CSV file named `test.csv` is found to test
the tool. 

Type: `user@system~$ ./buildDataTable.py`
      `Enter raw *.csv file to parse: ../examples/test.csv`

After entering the test CSV file a new file `consolidated_data.csv` would be
created. 

## TODO
* Generate in depth description on the algorithm used.
* Improve methods and get rid of possible redudant/unecessary steps.
* Test in Windows & iOS environments.
* Document user usage guidelines.
* Remove helper files after excetion of script is done. Currentley they are
  left as debug aid for new contributors to understand the program workflow.
* Document `buildDataTable\_v2.py` source.
* Call labelSubstitution.py from buildDataTable.py.

Copyright (C) 2021 Global Ecosystem Dynamics Initiave.
