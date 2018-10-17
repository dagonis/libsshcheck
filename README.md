# libsshcheck
Throw away libssh checker.

Quick and dirty, living off the land Python script that works for Python 3 (and accidentally python 2.7! 2.6 and older will fail).

This will only work for a few weeks, when the clean libssh versions start to increment the checks in this tool will no longer work. If this is after November 1st 2018, find a better tool or edit this one for your own purposes.

# Install
Don't have to install anything. Clone and run!

`git clone https://github.com/dagonis/libsshcheck.git`

# Example output

```
python libcheck.py 8.8.8.8 166.164.47.80 176.37.126.71
8.8.8.8 unable to connect
166.164.47.80 looks vulnerable
176.37.126.71 may not be vulnerable
```
