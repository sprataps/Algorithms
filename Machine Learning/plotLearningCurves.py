'''
To check if the model is overfitting or underfitting,

1- check cross validation metrics :
        IF the model performs well on the training data but bad on the test set, the model is overfitting.
        If the model performs equally bad on both the test and training sets, the model is underfitting.

2- plot learning curves:
        The plots are of the model's performance on the training and testing sets as a function of training set size.

        If the model is underfitting the TRAINING DATA, adding more training instances doesn't help. Improve the features
        or use a complex model.

        If the curves on the training and validation set differ by a huge margin, it is a sign of overfitting. One way of improving
        overfitting is to get more data so that the validation error matches training error.
'''


from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def plotLearningCurves(model,X,Y):
    x_train,x_test,y_train,t_test=train_test_split(X,Y,test_size=.25)
    train_error,test_error=[],[]
    for i in range(len(x_train)):
        model.fit(x_train[:m],y_train[:m]) #fit the model on training instances with increasing instance size
        y_train_pred=model.predict(x_train[:m])

        y_test_pred=model.predict(x_test)
        train_error.append(mean_squared_error(y_train_pred,y_train[:m]))
        test_error_append(mean_squared_error(y_test_pred,y_test))
    plt.plot(np.sqrt(train_error),'r',label='train')
    plt.plot(np.sqrt(test_error),'b',label='test')
