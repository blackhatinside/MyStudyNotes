'''     // -- Template by A_*_A -- //       '''

# ''' # FASTIO  BEGINS 0.34 sec
# FASTIO  ENDS '''
import sys;k=int(sys.stdin.readline().split()[1]);sys.stdout.write('%d'%sum(1 for x in map(int,sys.stdin.buffer) if not x%k))

# ----------------------------------------------------------------

# ''' # FASTIO  BEGINS 0.37 sec
import sys
# FASTIO  ENDS '''
_, k = map(int, sys.stdin.readline().split())
count = sum(1 for x in map(int, sys.stdin.buffer) if not x % k)
sys.stdout.write(str(count))

# ----------------------------------------------------------------

# ''' # FASTIO  BEGINS 0.64 sec
import sys
input=sys.stdin.readline
# FASTIO  ENDS '''

y0, y1 = [int(x) for x in input().split()]
c = sum(not int(input()) % y1 for i in range(y0))
print(c)

# ----------------------------------------------------------------

# ''' # FASTIO  BEGINS 0.65 sec
import atexit, io, os
inputt = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = lambda: inputt()   # int
# input = lambda: inputt().decode().strip()   # str
ss = io.BytesIO()
_write = ss.write
ss.write = lambda s: _write(s.encode())
atexit.register(lambda: os.write(1, ss.getvalue()))
# FASTIO  ENDS '''

y0, y1 = [int(x) for x in input().split()]
c = sum(not int(input()) % y1 for i in range(y0))
print(c)

# ----------------------------------------------------------------

# ''' # FASTIO  BEGINS 0.87 sec
import sys
input=lambda:sys.stdin.readline()
# FASTIO  ENDS '''

y0, y1 = [int(x) for x in input().split()]
c = sum(not int(input()) % y1 for i in range(y0))
print(c)

# ----------------------------------------------------------------

# ''' # FASTIO  BEGINS 0.94 sec
import atexit,io,os,sys
ss=io.BytesIO()
_write=ss.write
ss.write=lambda sett:_write(sett.encode())
atexit.register(lambda:os.write(1,ss.getvalue()))
y_in=open(0).read().split("\n")
def y_inf():
    for y_id in range(len(y_in)):
        yield y_id
y_ino=y_inf()
input=lambda:y_in[next(y_ino)]
# FASTIO  ENDS '''

y0, y1 = [int(x) for x in input().split()]
c = sum(not int(input()) % y1 for i in range(y0))
print(c)

# ----------------------------------------------------------------

# ''' # FASTIO  BEGINS 1.08 sec
import sys
input=lambda:sys.stdin.readline().rstrip("\r\n")
# FASTIO  ENDS '''

y0, y1 = [int(x) for x in input().split()]
c = sum(not int(input()) % y1 for i in range(y0))
print(c)

# ----------------------------------------------------------------

# ''' # FASTIO  BEGINS 1.8 sec
import os,sys
from io import BytesIO,IOBase
BUFSIZ=8192
class FastIO(IOBase):
    newlines=0
    def __init__(self,file):
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="n"in file.mode or "r" not in file.mode
        self.write=self.buffer.write if self.writable else None
    def read(self):
        while True:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZ))
            if not b:
                break
            ptr=self.buffer.tell()
            self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines=0
        return self.buffer.read()
    def readline(self):
        while self.newlines==0:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size, BUFSIZ))
            self.newlines=b.count(b"\n")+(not b)
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines-=1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd,self.buffer.getvalue())
            self.buffer.truncate(0),self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda sett:self.buffer.write(sett.encode("ascii"))
        self.read=lambda:self.buffer.read().decode("ascii")
        self.readline=lambda:self.buffer.readline().decode("ascii")
if sys.version_info[0]<3:
    sys.stdin,sys.stdout=FastIO(sys.stdin),FastIO(sys.stdout)
else:
    sys.stdin,sys.stdout=IOWrapper(sys.stdin),IOWrapper(sys.stdout)
input=lambda:sys.stdin.readline().rstrip("\r\n")
# FASTIO  ENDS '''

y0, y1 = [int(x) for x in input().split()]
c = sum(not int(input()) % y1 for i in range(y0))
print(c)

# ----------------------------------------------------------------

# ''' # FASTIO  BEGINS 2.1 sec
# FASTIO  ENDS '''

y0, y1 = [int(x) for x in input().split()]
c = sum(not int(input()) % y1 for i in range(y0))
print(c)

'''     // -- Template by A_*_A -- //       '''
