import json,os,urllib.request
M=100000;X=100
C,E,S,D=131072,262144,524288,1048576
V=(0,100,320,330,500,900,0)
N=(33,31,18,14,-14,-18,-31,-33)
G=(1,-1,16,-16,15,17,-15,-17)
B=(15,17,-15,-17)
R=(1,-1,16,-16)
W=[15]*128
W[0]=13;W[7]=14;W[4]=12;W[112]=7;W[119]=11;W[116]=3
T=[[0]*64 for _ in[0]*8]
P=[0]*2048
for r in range(8):
 for f in range(8):
  i=8*r+f;c=min(f,7-f)+min(r,7-r)
  T[1][i]=(0,0,4,8,14,24,40,0)[r]+(0,0,0,10,15,10,5,0)[r]*(f in(3,4))
  T[2][i]=6*c-20;T[3][i]=4*c-8;T[5][i]=2*c-6
  T[4][i]=(r==6)*15+(r==0)*(f in(3,4))*5
  T[6][i]=(20,25,10,0,0,10,25,20)[f] if r<1 else max(-50,-15*r)
  T[7][i]=8*c-24
  for t in(1,2,3,4,5,6):
   w=V[t]+T[t][i]
   P[256*r+16*f+t]=w
   P[256*(7-r)+16*f+t+8]=-w
bd=bytearray(128)
bd[0:8]=4,2,3,5,6,3,2,4
bd[16:24]=1,1,1,1,1,1,1,1
bd[96:104]=9,9,9,9,9,9,9,9
bd[112:120]=12,10,11,13,14,11,10,12
sd=0;cw=15;ep=-1;hm=0;kg=[4,116]
PF=[0]*19;sp=0
TT={}
KL=[0]*200
HI=[0]*2**21
nd=ab=lm=0
z=lambda i:(PF[i]>0)*(8*~-PF[i]+10*((PF[i-1]|PF[i+1])<1))
def pu(i,dd):
 global sp
 a=z(i-1)+z(i)+z(i+1)
 PF[i]+=dd
 sp+=(z(i-1)+z(i)+z(i+1)-a)*(1-2*(i>8))
def rs():
 global sc,np,wb,bb,sp,hs,us
 sc=np=wb=bb=sp=0;PF[:]=[0]*19
 for q in range(128):
  p0=bd[q]
  if p0:
   sc+=P[q*16+p0];t=p0&7
   if t>1:np+=V[t]
   if t==1:PF[9*(p0>7)+(q&7)]+=1
   elif t==3:wb+=p0<8;bb+=p0>7
 sp=sum((1-2*(i>8))*z(i)for i in range(18))
 hs=[];us=[]
rs()
def at(q,y):
 e=y<<3;w=16-32*y
 for d in(w-1,w+1):
  t=q-d
  if not t&136 and bd[t]==1+e:return 1
 for d in N:
  t=q+d
  if not t&136 and bd[t]==2+e:return 1
 for d in G:
  t=q+d
  if not t&136 and bd[t]==6+e:return 1
 for ds,k in((B,3),(R,4)):
  for d in ds:
   t=q+d
   while not t&136:
    p2=bd[t]
    if p2:
     if p2==k+e or p2==5+e:return 1
     break
    t+=d
 return 0
def gn(cps):
 O=[]
 for f in range(128):
  pc=bd[f]
  if not pc or pc>>3!=sd:continue
  t=pc&7
  if t==1:
   w2=16-32*sd;r=f>>4;ls=6-5*sd;one=f+w2
   if not bd[one]:
    if r==ls:O+=f|one<<7|5<<14,
    elif not cps:
     O+=f|one<<7,
     if r==1+5*sd and not bd[one+w2]:O+=f|one+w2<<7|D,
   for d in(w2-1,w2+1):
    to=f+d
    if to&136:continue
    tp=bd[to]
    if tp and tp>>3!=sd:
     O+=f|to<<7|C|(5<<14 if r==ls else 0),
    elif to==ep:O+=f|to<<7|C|E,
   continue
  if t<3 or t==6:
   for d in(N if t==2 else G):
    to=f+d
    if to&136:continue
    tp=bd[to]
    if not tp:
     if not cps:O+=f|to<<7,
    elif tp>>3!=sd:O+=f|to<<7|C,
   if t==6 and not cps:
    y=112*sd+4;u=sd^1
    if not at(y,u):
     if cw>>2*sd&1 and not bd[y+1]and not bd[y+2]and not at(y+1,u)and not at(y+2,u):O+=y|y+2<<7|S,
     if cw>>2*sd+1&1 and not bd[y-1]and not bd[y-2]and not bd[y-3]and not at(y-1,u)and not at(y-2,u):O+=y|y-2<<7|S,
   continue
  for d in(B if t==3 else R if t==4 else G):
   to=f+d
   while not to&136:
    tp=bd[to]
    if not tp:
     if not cps:O+=f|to<<7,
    else:
     if tp>>3!=sd:O+=f|to<<7|C,
     break
    to+=d
 return O
def mk(m):
 global sd,cw,ep,hm,sc,np,wb,bb,us,hs,sp
 f=m&127;t=m>>7&127;pc=bd[f];u=sd
 cs=t+32*u-16 if m&E else t
 cap=bd[cs]
 us+=(m,cap,cw,ep,hm,sc,np,wb,bb,sp),
 if cap:
  bd[cs]=0;sc-=P[cs*16+cap];c7=cap&7
  if 1<c7<6:
   np-=V[c7]
   if c7==3:
    if cap<8:wb-=1
    else:bb-=1
  if c7==1:pu(9*(cap>7)+(cs&7),-1)
 bd[f]=0
 pr=m>>14&7
 pl=pr|u<<3 if pr else pc
 if pr:pu(9*u+(f&7),-1);np+=V[pr]
 elif pc&7<2 and cap:pu(9*u+(f&7),-1);pu(9*u+(t&7),1)
 bd[t]=pl
 sc+=P[t*16+pl]-P[f*16+pc]
 if pc&7==6:kg[u]=t
 if m&S:
  r=t-f>>1;x=f+3 if t>f else f-4;rk=bd[x];bd[x]=0;bd[f+r]=rk
  sc+=P[(f+r)*16+rk]-P[x*16+rk]
 cw&=W[f]&W[t]
 ep=f+t>>1 if m&D else -1
 hm=0 if pc&7==1 or cap else hm+1
 sd=u^1
 hs+=(bytes(bd),sd,cw,ep),
 if at(kg[u],u^1):um();return 0
 return 1
def um():
 global sd,cw,ep,hm,sc,np,wb,bb,sp
 m,cap,c0,e0,h0,s0,n0,w0,b0,s9=us.pop()
 hs.pop()
 sd^=1;u=sd
 f=m&127;t=m>>7&127
 pr=m>>14&7
 pc=1|u<<3 if pr else bd[t]
 bd[f]=pc;bd[t]=0
 if pc&7==6:kg[u]=f
 if cap:
  bd[t+32*u-16 if m&E else t]=cap
  if cap&7==1:PF[9*(cap>7)+((t+32*u-16 if m&E else t)&7)]+=1
 if m&S:
  r=t-f>>1;x=f+3 if t>f else f-4;bd[x]=bd[f+r];bd[f+r]=0
 if pr:PF[9*u+(f&7)]+=1
 elif pc&7<2 and cap:PF[9*u+(t&7)]-=1;PF[9*u+(f&7)]+=1
 cw=c0;ep=e0;hm=h0;sc=s0;np=n0;wb=w0;bb=b0;sp=s9
# eval: material+PST, king activity, bishop pair, tempo
def ev():
 i=6400-min(np,6400)
 a=kg[0];b=kg[1]
 r0=(a>>4)*8+(a&7);r1=(7-(b>>4))*8+(b&7)
 s=sc+((T[7][r0]-T[6][r0])-(T[7][r1]-T[6][r1]))*i//6400
 s+=30*((wb>1)-(bb>1))
 return s-sp-s*2*sd
def rp():
 i=len(hs)-3;s=max(len(hs)-1-hm,0)
 while i>=s:
  if hs[i]==hs[-1]:return 1
  i-=2
 return 0
A8="abcdefgh";I8="12345678"
def sn(m):
 f=m&127;t=m>>7&127
 return A8[f&7]+I8[f>>4]+A8[t&7]+I8[t>>4]+(" pnbrq"[m>>14&7]if m>>14&7 else"")
def so(ms,t2,k0,k1):
 r=[];i=0
 for m in ms:
  if m==t2:s=1<<30
  else:
   s=100000+10*(V[bd[m>>7&127]&7]or 100)-(bd[m&127]&7)if m&C else 0
   pr=m>>14&7
   if pr:s+=350000+V[pr]
   elif not s:s=50000 if m==k0 else 40000 if m==k1 else HI[m]
  r+=(s,-i,m),;i+=1
 r.sort(reverse=1)
 return r
def qs(a,b2,y):
 global nd,ab
 nd+=1
 if lm and nd>=lm:ab=1;return 0
 if y>=X:return ev()
 u=sd
 if at(kg[u],u^1):
  st=-M-1;ms=gn(0)
 else:
  st=ev()
  if st>=b2:return st
  if st>a:a=st
  ms=gn(1)
 best=st;lg=0
 for s,ni,m in so(ms,0,0,0):
  if mk(m):
   lg+=1
   v=-qs(-b2,-a,y+1)
   um()
   if ab:return 0
   if v>best:best=v
   if v>=b2:return v
   if v>a:a=v
 if st<-M and not lg:return -M+y
 return best
# main search: PVS, TT, null-move, LMR, killer moves
def gs(d,a,b2,y):
 global nd,ab,hs,sd
 nd+=1
 if lm and nd>=lm:ab=1;return 0
 if y>0 and(hm>=100 or rp()):return 0
 if ck:=at(kg[sd],sd^1):d+=1
 if d<1 or y>=X:return qs(a,b2,y)
 k=hs[-1]
 e=TT.get(k)
 t2=0
 if e:
  if e[0]>=d:
   s=e[2]-y if e[2]>M-X else e[2]+y if e[2]<-M+X else e[2]
   if e[1]==1 or(e[1]==2 and s>=b2)or(e[1]==3 and s<=a):return s
  t2=e[3]
 a0=a
 if d>=3 and b2<M-1000 and np>900 and not ck:
  sd^=1;hs+=(bytes(bd),sd,cw,ep),
  v=-gs(d-3,-b2,-b2+1,y+1)
  hs.pop();sd^=1
  if ab:return 0
  if v>=b2:return v
 k0=KL[y*2];k1=KL[y*2+1]
 best=-M-1;bm=0;lg=0
 for s,ni,m in so(gn(0),t2,k0,k1):
  if mk(m):
   lg+=1
   if d>=3 and lg>3 and not m&245760:
    v=-gs(d-2,-a-1,-a,y+1)
    if v>a:v=-gs(d-1,-b2,-a,y+1)
   else:v=-gs(d-1,-b2,-a,y+1)
   um()
   if ab:return 0
   if v>best:best=v;bm=m
   if v>a:a=v
   if a>=b2:
    if not m&245760:
     if KL[y*2]!=m:KL[y*2+1]=KL[y*2];KL[y*2]=m
     HI[m]+=d*d
    break
 if not lg:return -M+y if at(kg[sd],sd^1)else 0
 TT[k]=(d,3 if best<=a0 else 2 if best>=b2 else 1,best+y if best>M-X else best-y if best<-M+X else best,bm)
 return best
def go(md,bg):
 global nd,ab,lm
 TT.clear();nd=ab=lm=0
 KL[:]=[0]*200
 ms=[um()or m for m in gn(0)if mk(m)]
 if not ms:return 0
 order=[(0,i,m)for i,m in enumerate(ms)]
 best=order[0]
 for d in range(1,md+1):
  lm=bg if d>1 else 0
  ab=0;a=-M-1;res=[]
  for j,(s0,i,m)in enumerate(order):
   if mk(m):
    v=-gs(d-1,-M-1,-a,1)
    um()
    if ab:break
    if v>a:a=v
    res+=(-v,j,m),
  if ab:break
  res.sort()
  order=res;best=res[0]
  if best[0]<=-M+X:break
 return best[2]
def post(h,b):
 return json.load(urllib.request.urlopen(urllib.request.Request(os.environ["MAKEFUN_ENV_URL"]+h,data=json.dumps(b).encode(),headers={"content-type":"application/json"})))
if __name__=="__main__":
 B0=bytes(bd)
 g=post("/game",{})
 while g["status"]!="done":
  while g["status"]=="your_move":
   bd[:]=B0;sd=0;cw=15;ep=-1;hm=0;kg=[4,116];rs()
   for u0 in g["moves"]:
    for m in gn(0):
     if sn(m)==u0 and mk(m):break
   g=post("/move",{"game":g["game"],"move":sn(go(40,400000))})
  g=post("/game",{})
