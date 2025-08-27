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

```

```

2. CMD:
``` bash
# create the directory (including parent directory)
sudo mkdir -pv /mnt/lfs

# check if directory is empty or not
ls /mnt/lfs

# mount the storage partition to that directory
sudo mount /dev/nvme0n1p7 /mnt/lfs

# OPTIONAL: if swap not on already (usually its on), turn it on
sudo /sbin/swapon -v /dev/nvme0n1p5

# check if mounted successfully using list block devices command
lsblk -f

# set the LFS variable in terminal and reload current terminal
echo "export LFS=/mnt/lfs" >> ~/.bashrc
source ~/.bashrc

# check LFS variable
echo $LFS

# set file mode creation mask
umask 022

# check file mode creation mask
umask

# set owner and permission mode of $LFS dir
sudo chown root:root $LFS
sudo chmod 755 $LFS

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

# move the package list and its md5sum file to sources dir
sudo cp /home/cyberkid05/Downloads/Files/wget-list-sysv $LFS/sources/
sudo cp /home/cyberkid05/Downloads/Files/md5sums $LFS/sources/
```

- **Sticky Bit (`t`)** → when applied to a directory, it ensures that **only the owner of a file** within the directory can delete or modify that file. Other users can still create and modify files within the directory, but they can't delete or rename files owned by others.

``` bash
#!/bin/bash

# Navigate to the LFS sources directory and save current location
pushd $LFS/sources

# Verify MD5 checksums against the md5sums file
md5sum -c md5sums

# Return to the previous directory
popd
```

``` bash
# move downloaded missing files from Downloads to the required path
mv ~/Downloads/expat-2.6.4.tar.xz $LFS/sources/

# verify if files moved
ls $LFS/sources/

# download all required packages
wget -nc --continue --input-file=/home/cyberkid05/Downloads/Files/wget-list-sysv --directory-prefix=$LFS/sources

# check if any downloaded files corrupt


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

# verify if new user and group made
cat /etc/passwd | grep lfs # This indicates that the user `lfs` exists and has `/bin/bash` as the shell.

cat /etc/group | grep lfs

# set password for lfs user
passwd lfs

# grant lfs user full access to all directories under $LFS by making lfs the owner
chown -v lfs $LFS/{usr{,/*},lib,var,etc,bin,sbin,tools}

sudo chown -R lfs:root $LFS/{usr,var,etc,tools}
```

- `{etc,var}` → **brace expansion** that expands to both `etc` and `var`, so `mkdir` will create both directories `$LFS/etc` and `$LFS/var`.

FILE: mini_scripts.sh (paste and run the snippets one by one)
``` bash
# create symlinks
for i in bin lib sbin; do
  ln -sv usr/$i $LFS/$i
done

# verify system architecture (32 or 64 bit)
uname -m

# DO NOT RUN (NOT WORKING, INSTEAD RUN BELOW CMD)
case $(uname -m) in
  x86_64) sudo mkdir -pv $LFS/lib64 ;;
esac

# run this, if system is 64 bit
sudo mkdir -pv $LFS/lib64

# DO NOT RUN (NOT WORKING, INSTEAD RUN BELOW CMD)
case $(uname -m) in
  x86_64) sudo chown -v lfs $LFS/lib64 ;;
esac

# run this, if system is 64 bit
sudo chown -v lfs $LFS/lib64

```

``` bash
# verify if symlinks already exists
ls -l /bin
ls -l /lib
ls -l /sbin

# a more script friendly way to verify symlinks
test -L /bin && echo "/bin is a symbolic link" || echo "/bin is not a symbolic link"
test -L /lib && echo "/lib is a symbolic link" || echo "/lib is not a symbolic link"
test -L /sbin && echo "/sbin is a symbolic link" || echo "/sbin is not a symbolic link"
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
export MAKEFLAGS=-j8
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
  
  8. 
 Installing binutils
``` bash
# switch to lfs user
su - lfs

# check if LFS variable set for lfs user
echo $LFS

# switch to sources dir
cd $LFS/sources/

# extract the package
tar -xvf binutils-2.44.tar.xz

# go inside extracted package folder
cd binutils-2.44

# binutils require building in a separate dir
mkdir -v build
cd build
     
# prepare binutils for compilation
../configure \
  --prefix=$LFS/tools \
  --with-sysroot=$LFS \
  --target=$LFS_TGT \
  --disable-nls \
  --enable-gprofng=no \
  --disable-werror \
  --enable-default-hash-style=gnu

# continue compilation (if "make" fails with parallel jobs, rerun with "make -j1")
make

# install the package
make install

# go back to sources dir
cd $LFS/sources/

# remove the extracted folder (if not mentioned to keep by LFS book)
rm -rf binutils-2.44

# verify if ld and as binaries from binutils are present or not
$LFS/tools/bin/$LFS_TGT-ld --version
$LFS/tools/bin/$LFS_TGT-as --version

```

Installing gcc
``` bash
su - lfs
cd $LFS/sources/

# Extract and rename MPFR
tar -xvf ../mpfr-4.2.1.tar.xz
mv -v mpfr-4.2.1 mpfr

# Extract and rename GMP
tar -xvf ../gmp-6.3.0.tar.xz
mv -v gmp-6.3.0 gmp

# Extract and rename MPC
tar -xvf ../mpc-1.3.1.tar.gz
mv -v mpc-1.3.1 mpc

# set the default dir name for 64bit libraries to lib
case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' -i.orig gcc/config/i386/t-linux64
  ;;
esac

mkdir -v build
cd build

# prepare gcc for compilation
../configure \
  --target=$LFS_TGT \
  --prefix=$LFS/tools \
  --with-glibc-version=2.39 \
  --with-sysroot=$LFS \
  --with-newlib \
  --without-headers \
  --enable-default-pie \
  --enable-default-ssp \
  --disable-nls \
  --disable-shared \
  --disable-multilib \
  --disable-threads \
  --disable-libatomic \
  --disable-libgomp \
  --disable-libquadmath \
  --disable-libssp \
  --disable-libvtv \
  --disable-libstdcxx \
  --enable-languages=c,c++

make
make install

# create a full version of the internal header
cd ..
cat gcc/limitx.h gcc/glimits.h gcc/limity.h > `dirname $($LFS_TGT-gcc -print-libgcc-file-name)`/include/limits.h

# verify if limits.h file was created 
ls -l `dirname $($LFS_TGT-gcc -print-libgcc-file-name)`/include/limits.h

```
