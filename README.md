# mooneshine
Proxy redteam SSH connections going to the blue team and assign a random IP address on the way out.

## Usage
To install on a server, run the install script
```
bash install.sh
```

Then from a client machine, connect to moonshine by running the following
```
ssh -A shine@moonshine remotebox ls -al
```

Specify a user and password to use on the remote host
```
ssh -A shine@moonshine root:toor@remotebox
```

To create an alias for moonshine
```
alias moonshine='sshpass -p password ssh -A shine@moonshine'
```
