# step 2 ; Data preprocseing and cleaning

def data_preprocessing(df):
  '''

  step 1 : Feature Engerning and selection

  step 2 : split the dataset into Independent and Dependent columns I.e X and Y

  step 3 : Use train and test split i.e. split the dataset into seen and unseen
  (seen Date : train data and unseen data : test data )

  step 4 : Use scaling technique/ Normalization Techique

  step 5 : return seen and unseen data
  '''

  # step 1 : Feature Engerning and selection
  # Feature Engineering : Create a new feature based on existing feature

  df['Water  (component 4)(kg in a m^3 mixture)'] = df['Water  (component 4)(kg in a m^3 mixture)'] / (df['Cement (component 1)(kg in a m^3 mixture)'] + df['Blast Furnace Slag (component 2)(kg in a m^3 mixture)'] + df['Fly Ash (component 3)(kg in a m^3 mixture)'] )

  # step 2 : split the data set into X and y

  target_col  = 'Concrete compressive strength(MPa, megapascals) '
  X = df.drop(columns = [target_col]) # Independent colunm
  y = df[target_col] # Dependent column


  # step 3 : split the dataset into seen and unseen (train and test data)
  from sklearn.preprocessing import  MinMaxScaler,StandardScaler,RobustScaler
  from sklearn.model_selection import train_test_split
  X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                  test_size = 0.3,
                                                  random_state = 1)


  X_train.shape,X_test.shape,y_train.shape,y_test.shape

  # use scaling / Normalization technique
  '''
  * Scaling for traing data : fit_transform()
  * Scaling for testing data : transform()
  '''
  sc = MinMaxScaler()
  X_train = sc.fit_transform(X_train) # seen data 
  X_test = sc.transform(X_test)       # unseen data 

  #Step5: Return seen and unseen data
  return X_train, X_test, y_train, y_test
