PREREQ:
- Ch 1-4:
	- run on host
	- root user
	- LFS variable set for root user
- Ch 5-6:
	- /mnt/lfs/ must be mounted
	- lfs user
- Ch 7-10:
	- /mnt/lfs/ must be mounted
	- root user
	- LFS variable set for root user

1.  GUI:
	Use Minitool Partition to resize C:// and create an unallocated space of roughly 50 GB

2. CMD:
``` bash
# create the directory (including parent directory)
sudo mkdir -pv /mnt/lfs

# check if directory is empty or not
ls /mnt/lfs

# mount the storage partition to that directory
sudo mount /dev/nvme0n1p7 /mnt/lfs

# check if mounted successfully using list block devices command
lsblk -f

# set the LFS variable in terminal and reload current terminal
echo "export LFS=/mnt/lfs" >> ~/.bashrc
	source ~/.bashrc
```   

3. FILE: version-check.sh
``` bash
#!/bin/bash
# A script to list version numbers of critical development tools
# If you have tools installed in other directories, adjust PATH here AND
# in ~lfs/.bashrc (section 4.4) as well.

LC_ALL=C
PATH=/usr/bin:/bin

bail() { echo "FATAL: $1"; exit 1; }

grep --version > /dev/null 2> /dev/null || bail "grep does not work"
sed '' /dev/null || bail "sed does not work"
sort /dev/null || bail "sort does not work"

ver_check()
{
   if ! type -p $2 &>/dev/null
   then
      echo "ERROR: Cannot find $2 ($1)"; return 1;
   fi
   v=$($2 --version 2>&1 | grep -E -o '[0-9]+\.[0-9\.]+[a-z]*' | head -n1)
   if printf '%s\n' $3 $v | sort --version-sort --check &>/dev/null
   then
      printf "OK: %-9s %-6s >= $3\n" "$1" "$v"; return 0;
   else
      printf "ERROR: %-9s is TOO OLD ($3 or later required)\n" "$1";
      return 1;
   fi
}

ver_kernel()
{
   kver=$(uname -r | grep -E -o '^[0-9\.]+')
   if printf '%s\n' $1 $kver | sort --version-sort --check &>/dev/null
   then
      printf "OK: Linux Kernel $kver >= $1\n"; return 0;
   else
      printf "ERROR: Linux Kernel ($kver) is TOO OLD ($1 or later required)\n" "$kver";
      return 1;
   fi
}

# Coreutils first because --version-sort needs Coreutils >= 7.0
ver_check Coreutils sort 8.1 || bail "Coreutils too old, stop"
ver_check Bash bash 3.2
ver_check Binutils ld 2.13.1
ver_check Bison bison 2.7
ver_check Diffutils diff 2.8.1
ver_check Findutils find 4.2.31
ver_check Gawk gawk 4.0.1
ver_check GCC gcc 5.2
ver_check "GCC (C++)" g++ 5.2
ver_check Grep grep 2.5.1a
ver_check Gzip gzip 1.3.12
ver_check M4 m4 1.4.10
ver_check Make make 4.0
ver_check Patch patch 2.5.4
ver_check Perl perl 5.8.8
ver_check Python python3 3.4
ver_check Sed sed 4.1.5
ver_check Tar tar 1.22
ver_check Texinfo texi2any 5.0
ver_check Xz xz 5.0.0
ver_kernel 4.19

if mount | grep -q 'devpts on /dev/pts' && [ -e /dev/ptmx ]
then echo "OK: Linux Kernel supports UNIX 98 PTY";
else echo "ERROR: Linux Kernel does NOT support UNIX 98 PTY"; fi

alias_check() {
   if $1 --version 2>&1 | grep -qi $2
   then printf "OK: %-4s is $2\n" "$1";
   else printf "ERROR: %-4s is NOT $2\n" "$1"; fi
}
echo "Aliases:"
alias_check awk GNU
alias_check yacc Bison
alias_check sh Bash

echo "Compiler check:"
if printf "int main(){}" | g++ -x c++ -
then echo "OK: g++ works";
else echo "ERROR: g++ does NOT work"; fi
rm -f a.out

if [ "$(nproc)" = "" ]; then
   echo "ERROR: nproc is not available or it produces empty output"
else
   echo "OK: nproc reports $(nproc) logical cores are available"
fi
```

CMD:
``` bash
# check for all required packages
./version-check.sh

# install missing packages
sudo apt install bison gawk m4 texinfo
```

4.  CMD: create sources folder in the mounted directory
``` bash
# create sources folder in the mounted directory
mkdir -v $LFS/sources

# grant write permission, sticky bit to directory for all users
chmod -v a+wt $LFS/sources
```

- **Sticky Bit (`t`)** → when applied to a directory, it ensures that **only the owner of a file** within the directory can delete or modify that file. Other users can still create and modify files within the directory, but they can't delete or rename files owned by others.

``` bash
# move downloaded missing files from Downloads to the required path
mv ~/Downloads/expat-2.6.4.tar.xz $LFS/sources/

# verify if files moved
ls $LFS/sources/

# download all required packages
wget -nc --continue --input-file=/home/cyberkid05/Downloads/Files/wget-list-sysv --directory-prefix=$LFS/sources

# change owner of these files
chown root:root $LFS/sources/*
```

- **`-nc` (or `--no-clobber`)** → tells `wget` **not to overwrite existing files** in the target directory. If a file already exists, it will **skip the download**.
    
- **`--continue`** → allows `wget` to **resume an interrupted download** from where it left off, instead of starting the download over again.
    
- **`--input-file=/home/cyberkid05/Downloads/Files/wget-list-sysv`** → specifies a file containing a list of URLs that `wget` will download. The file should contain one URL per line.
    
    - `/home/cyberkid05/Downloads/Files/wget-list-sysv` → the file containing the list of URLs to be downloaded.
        
- **`--directory-prefix=$LFS/sources`** → tells `wget` where to **save the downloaded files**. The `$LFS/sources` directory is where the files will be stored.

- **`chown`** → The command to **change file ownership**.
    
- **`root:root`** → Specifies the new **owner** and **group** for the files. In this case:
    
    - `root` → The user who will **own** the files (in this case, `root`).
        
    - `root` → The **group** that will own the files (also set to `root`).
        
- **`$LFS/sources/*`** → The **path** of the files whose ownership will be changed:
        
    - `*` → A wildcard that **selects all files** in the `sources` directory.

6. 
``` bash
mkdir -pv $LFS/{etc,var} $LFS/usr/{bin,lib,sbin}
mkdir -pv $LFS/tools

# add new user lfs and add it to a group lfs
groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs

# set password for lfs user
passwd lfs

# grant lfs user full access to all directories under $LFS by making lfs the owner
chown -v lfs $LFS/{usr{,/*},lib,var,etc,bin,sbin,tools}

sudo chown -R lfs:root $LFS/{usr,var,etc,tools}
```

- `{etc,var}` → **brace expansion** that expands to both `etc` and `var`, so `mkdir` will create both directories `$LFS/etc` and `$LFS/var`.

FILE: mini_scripts.sh
``` bash
for i in bin lib sbin; do
  ln -sv usr/$i $LFS/$i
done

case $(uname -m) in
  x86_64) sudo mkdir -pv $LFS/lib64 ;;
esac

case $(uname -m) in
  x86_64) sudo chown -v lfs $LFS/lib64 ;;
esac
```

CMD:
``` bash
./mini_scripts.sh
```

7. 
``` bash
# switch to lfs user
su - lfs

# add this line to .bash_profile
cat > /.bash_profile << "EOF"
exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash
EOF

cat > ~/.bashrc << "EOF"
set +h
umask 022
LFS=/mnt/lfs
LC_ALL=POSIX
LFS_TGT=$(uname -m)-lfs-linux-gnu
PATH=/usr/bin
if [ ! -L /bin ]; then PATH=/bin:$PATH; fi
PATH=$LFS/tools/bin:$PATH
CONFIG_SITE=$LFS/usr/share/config.site
export LFS LC_ALL LFS_TGT PATH CONFIG_SITE
EOF
```
- **`cat`**: This command is used to concatenate and display the content of files, but in this case, you're redirecting input into the file.
    
- **`>`**: The redirection operator is used here to send the input from `cat` into a file (`~/.bash_profile`), meaning whatever you type after this command will be written to that file.
    
- **`~/.bash_profile`**: This is a hidden file in your home directory (`~` represents your home directory) that is executed by Bash when a user logs in. It's often used for setting up environment variables, functions, and running scripts.
    
- **`<< "EOF"`**: This indicates that the input ends when the string `EOF`  (delimiter) is encountered. It's called a "here document" in Bash, and the content between `<< "EOF"` and the `EOF` delimiter will be inserted into the file.

Several commercial distributions add an undocumented instantiation of /etc/bash.bashrc to the initialization of bash. This file has the potential to modify the lfs user's environment in ways that can affect the building of critical LFS packages. To make sure the lfs user's environment is clean, check for the presence of /etc/bash.bashrc and, if present, move it out of the way

  ``` bash (root)
  # in a new terminal, run this as root
  sudo sh -c '[ ! -e /etc/bash.bashrc ] || mv -v /etc/bash.bashrc /etc/bash.bashrc.NOUSE'
  
  # # to restore the file back after building LFS
  mv -v /etc/bash.bashrc.NOUSE /etc/bash.bashrc
  ```
  
  ``` bash (lfs)
  # set the number of cores to use for compilation
  # my Acer Aspire 7 has 4 perf cores (2 threads each) and 2 effi cores(1 thread each) so total logical cores would be 8 + 4  = 12, thereby my cpu can handle 12 tasks(threads) at the same time
  make -j8
  export MAKEFLAGS=-j8
  ```
