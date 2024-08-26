# Dirtycow, assumes SSH access to one of the users.

Using `uname -a` we can get the kernel version.
This version is vulnerable to dirty-cow exploit, a race-condition allowing for privilege-escalated write in the linux kernel.
A write-up of it can be found [here](https://chao-tic.github.io/blog/2017/05/24/dirty-cow)

Here we will just exploit this race-condition using [PoC source code](https://raw.githubusercontent.com/FireFart/dirtycow/master/dirty.c).

We can just download it in /tmp then run it easily, upon waiting, we get a shell, it's root.
