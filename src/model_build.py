# step 3  Model Building and Evaluation
 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score

from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet,HuberRegressor,RANSACRegressor,TheilSenRegressor,SGDRegressor

score = []
def model_building(X_train,X_test,y_train,y_test):
  models = {'LinearRegression': LinearRegression(),
            'Ridge': Ridge(),
            'Lasso': Lasso(),
            'ElasticNet': ElasticNet(),
            'HuberRegressor': HuberRegressor(),
            'RANSACRegressor': RANSACRegressor(),
            'TheilSenRegressor': TheilSenRegressor(),
            'SGDRegressor': SGDRegressor()}

  for model_name, model in models.items():
        model.fit(X_train, y_train)  # Seen Data 
        y_pred = model.predict(X_test)   #Unseen Data
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        score.append(r2)

  return score

