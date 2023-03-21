def f1_score(y, pred):
    tp, tn, fp, fn = 0, 0, 0, 0
    for i, j in zip(y, pred):
        if i ==1 and j == 1:
            tp += 1
        elif i == 1 and j ==0:
            fn += 1
        elif i ==0 and j == 0:
            tn += 1
        elif i ==0 and j ==1:
            fp += 1
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    return 2*precision*recall/(precision+recall)

class LogisticRegression:
    def __init__(self, iters=400, alpha=0.001) -> None:
        self.iters = iters
        self.alpha = alpha
 
    def log_likelihood(self,y,preds):
        loss0 = y*np.log(preds)
        loss1 = (1-y)*np.log(1-preds)
        return -np.mean(loss0+loss1)

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        preds = self.predict(X)
        cur_loss = self.log_likelihood(y, preds)
        for i in range(self.iters):
            gradients_w = np.matmul(X.T, preds-y)
            gradients_w = np.array([np.mean(grad) for grad in gradients_w])

            #self.weights = self.weights - alpha*np.dot(X.T, preds-y)
            self.weights = self.weights - alpha*gradients_w
            preds = self.predict(X)
            new_loss = self.log_likelihood(y, preds)
            if cur_loss < new_loss:
                break
            cur_loss = new_loss
    
    def predict(self, X):
        z = np.dot(X,self.weights)
        return 1/(1+np.exp(-z))
