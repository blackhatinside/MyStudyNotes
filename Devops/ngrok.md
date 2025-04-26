# To connect to a remote machine (eg. NITR Lab Ubuntu System [private network]) using Reverse SSH Tunneling from Windows 11 (our machine)

the following installation didn't work for ngrok in Ubuntu
``` bash
cd ~
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar xvzf ngrok-v3-stable-linux-amd64.tgz
```

SO TRY THE BELOW COMMANDS INSTEAD 

# commands to be run on remote college system
``` bash
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh

# install ngrok
sudo snap install ngrok

# sign up, sign in and create an auth token (eg. 1YAQYcZLeP555FNSKWN245NNwefr324rcsB4syhl_87Z4JB8GhKdCE1F) in "https://dashboard.ngrok.com/get-started/your-authtoken" and use it
./ngrok authtoken 1YAQYcZLeP555FNSKWN245NNwefr324rcsB4syhl_87Z4JB8GhKdCE1F

# start the tunnel
./ngrok tcp 22
```

# commands to be run on my machine
``` bash
choco install ngrok

ssh user@0.tcp.in.ngrok.io -p 19370
```
