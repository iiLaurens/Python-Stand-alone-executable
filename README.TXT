I have often wanted a stand-alone version of python that would be a single
Windows executable.  This is my attempt to make a generally useful executable.

It consists of Python 3.5.2 and should include all standard libraries.

It was built with pyinstaller.

If conda is installed, the python environment can be recreated using the following command:
	conda env create -f environment.yml -p .\env

To build, make sure you have the following files:
  py.py          # the main source file
  setup.py       # the file needed for py2exe
type:
  pyinstaller py.py --onefile

You'll end up with a file called dist\py.exe.

Go ahead and use the executable or source as you see fit.  Credit is
appreciated, but not necessary.  I accept no liability.

If you found this useful, let me know.  If there is an issue, also let me know.
Obviously, one could include more or less libraries to either add features or
reduce the size of the executable.  I don't intend to make alternate versions
with different libraries.

This project is ultimately based on the Python 2.7 stand-alone version created by David Manthey.
Please visit http://www.orbitals.com/programs/pyexe.html

2017/2/12 - Laurens Janssen - github@laurens.xyz

