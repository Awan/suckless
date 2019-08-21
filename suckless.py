#!/usr/bin/env python3

import subprocess as sp

# lets compile dwm first
sp.os.chdir('dwm')
sp.call(['sh', 'depends'])
sp.call(['make'])
sp.call(['sudo', 'make', 'install'])

# demenu
sp.os.chdir('../dmenu')
sp.call(['make'])
sp.call(['sudo', 'make', 'install'])

# slstatus
sp.os.chdir('../slstatus')
sp.call(['make'])
sp.call(['sudo', 'make', 'install'])

# slock
sp.os.chdir('../slock')
sp.call(['make'])
sp.call(['sudo', 'make', 'install'])
