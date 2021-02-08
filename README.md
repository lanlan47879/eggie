# eggie
Egg generator used for buffer overflows in cs3433 

## Background
This small program was written for a buffer overflow assignment in cs3433. The program generates an egg that was used to exploit the
finger daemon on the instructor provided machines. Defaults to 32 bit Intel shell code but supports 32 bit ARM shell code. If I ever get around to it,
I will add support for bot 64 bit Intel shell code and 64 bit ARM shell code.

## Usage
The program can run with default settings with `python3 eggie.py`. This will generate a file called eggie containing the produced egg.

### Changing Default Settings
  
There are multiple arguments that can be used to change the default settings

* -a, --architecture can be used to specify the target machine's architecture. options include `intel` (default) and `arm`
* -o, --offset can be used to specify the offset from the stack pointer. later used to calculate the address that will populate the egg
* -s, --size can be used to specify the total size of the egg
* -c, --command can be used to specify the command that will be used in the shell code. options include `sh` and `ls`. not that the `arm` shell code will not function with the `ls` option
* -l, --alignment can be used to specify the word alignment of the shell code on the victim machine's stack
