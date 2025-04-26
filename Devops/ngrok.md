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
on running ngrok tunneling, a process starts with following output, use the port given in the 'Forwarding' field to connect to remote machine
``` bash
ngrok                                                                                                                                                 (Ctrl+C to quit)
                                                                                                                                                                      
🛡️ Protect endpoints w/ IP Intelligence: https://ngrok.com/r/ipintel                                                                                                   
                                                                                                                                                                      
Session Status                online                                                                                                                                  
Account                       Adithya E S (Plan: Free)                                                                                                                
Version                       3.22.1                                                                                                                                  
Region                        India (in)                                                                                                                              
Latency                       76ms                                                                                                                                    
Web Interface                 http://127.0.0.1:4040                                                                                                                   
Forwarding                    tcp://0.tcp.in.ngrok.io:16205 -> localhost:22                                                                                           
                                                                                                                                                                      
Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                             
                              0       0       0.00    0.00    0.00    0.00
```

# commands to be run on my machine
``` bash
choco install ngrok

ssh user@0.tcp.in.ngrok.io -p 16205
```

# To download files from your remote Ubuntu machine to your Windows 11 PC, use SCP:
``` bash
scp -P 16205 user@0.tcp.in.ngrok.io:/path/to/remote/file C:\local\destination\folder

# example:
scp -P 16205 user@0.tcp.in.ngrok.io:/home/user/adithyaes/AdiCode/Mtech_ResearchWork/Augs/isles_aug_seg_HIMRA_5_midsem_UNet.py "C:\Cyberkid\MyMTech\Labwork\SecondYear\SEM4\temp"
```
# For downloading multiple files or directories, use:
``` bash
scp -P 16205 -r user@0.tcp.in.ngrok.io:/path/to/remote/directory C:\local\destination\folder
```
