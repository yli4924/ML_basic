n,p,k = 100, 8, 3
X=np.random.random([n,k])
W=np.random.random([k,p])
Y=np.random.random([n,p])
max_itr=1000
alpha=0.0001
Lambda=0.01

def F(X,W):
    return np.matmul(X, W)

def cost(Y_est, Y, W, Lambda):
    E = Y_est - Y
    return E, np.linalg.norm(E,2)+Lambda*np.linalg.norm(W, 2)

def gradient(E, X, W, Lambda):
    return 2*np.matmul(X.T, E) + Lambda*2*W

def fit(W, X, Y, alpha, Lambda, max_itr):
    for i in range(max_itr):
        
        Y_est=F(X,W)
        E, c= cost(Y_est, Y, W, Lambda)
        Wg=gradient(E, X, W, Lambda)
        W=W - alpha * Wg
        if i%100==0:
            print(c)
        
    return W

X=np.concatenate( (X, np.ones((n,1))), axis=1 ) 
W=np.concatenate( (W, np.random.random((1,p)) ), axis=0 )

W = fit(W, X, Y, alpha, Lambda, max_itr)
