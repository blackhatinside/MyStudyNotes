# ENTER YOUR CODE HERE  -------------------->
# sys.setrecursionlimit(1000)

# ''' #   0.7 sec average INTEST    -   best for Codechef
import atexit,io,os,sys
ss=io.BytesIO()
_write=ss.write
ss.write=lambda s:_write(s.encode())
atexit.register(lambda:os.write(1,ss.getvalue()))
y_in=open(0).read().split("\n")
def y_inf():
    for y_id in range(len(y_in)):
        yield y_id
y_ino=y_inf()
input=lambda:y_in[next(y_ino)]
# '''

''' #   1.1 sec average INTEST
import sys
input=sys.stdin.readline
# input=lambda:sys.stdin.readline().rstrip("\r\n")
# '''

''' # REGION FASTIO   1.7 sec average INTEST    -   best for Codeforces
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
        self.write=lambda s:self.buffer.write(s.encode("ascii"))
        self.read=lambda:self.buffer.read().decode("ascii")
        self.readline=lambda:self.buffer.readline().decode("ascii")
if sys.version_info[0]<3:
    sys.stdin,sys.stdout=FastIO(sys.stdin),FastIO(sys.stdout)
else:
    sys.stdin,sys.stdout=IOWrapper(sys.stdin),IOWrapper(sys.stdout)
input=lambda:sys.stdin.readline().rstrip("\r\n")
# END REGION '''

#   2.1 sec average INTEST
tcs = 1
for tc in range(tcs):
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        ans += (int(input()) % k == 0)
    print(ans)

#       <----------------------------------------

# ENTER YOUR NOTES HERE -------------------->
'''
        // -- Template by A_*_A -- //
                                            '''
#       <----------------------------------------
