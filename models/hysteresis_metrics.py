"""Model-independent metrics for measured/predicted industrial hysteresis loops."""
import numpy as np

def _vectors(x,y):
    x=np.asarray(x,float); y=np.asarray(y,float)
    if x.ndim!=1 or y.ndim!=1 or x.size!=y.size or x.size<3:
        raise ValueError("x and y must be 1-D arrays of equal length >= 3")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("x and y must be finite")
    return x,y

def loop_area(x,y):
    """Absolute closed-loop area, |integral y dx|."""
    x,y=_vectors(x,y)
    if not (np.isclose(x[0],x[-1]) and np.isclose(y[0],y[-1])):
        x=np.r_[x,x[0]]; y=np.r_[y,y[0]]
    return float(abs(np.sum(.5*(y[1:]+y[:-1])*np.diff(x))))

def rmse(reference,prediction):
    a=np.asarray(reference,float); b=np.asarray(prediction,float)
    if a.shape!=b.shape or a.size==0: raise ValueError("equal non-empty shapes required")
    return float(np.sqrt(np.mean((a-b)**2)))

def branch_separation(x,y,split_index):
    """Mean absolute loading/unloading output gap on their common input range."""
    x,y=_vectors(x,y)
    if not 1<=split_index<len(x)-1: raise ValueError("invalid reversal index")
    def collapse(xx,yy):
        order=np.argsort(xx); xx,yy=xx[order],yy[order]
        ux,inv=np.unique(xx,return_inverse=True)
        return ux,np.bincount(inv,weights=yy)/np.bincount(inv)
    xa,ya=collapse(x[:split_index+1],y[:split_index+1])
    xb,yb=collapse(x[split_index:],y[split_index:])
    lo,hi=max(xa.min(),xb.min()),min(xa.max(),xb.max())
    grid=np.linspace(lo,hi,200)
    return float(np.mean(np.abs(np.interp(grid,xa,ya)-np.interp(grid,xb,yb))))
