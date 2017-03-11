# sample


## Overview
This is sample of fablib.


## Run sample by test-repo
Follow these steps.
```
$ fab test:l=sample,p='bootstrap|setup'
```


## Testing Guidelines
This library can be tested with tox.
Follow these steps.
```
$ tox
...
...
Done.
Disconnecting from 192.168.122.101... done.
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
__init__.py       7      0   100%
__________ summary ________________________
  py27: commands succeeded
  congratulations :)
```


## License
This is licensed under the MIT. See the [LICENSE](./LICENSE) file for details.
