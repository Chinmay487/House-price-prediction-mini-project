import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


def main():
    housing = pd.read_csv('dataset.csv')
    y = housing['Price']
    x = housing[[column_name for column_name in housing.columns if column_name not in ['Price','Address']]]
    x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42,test_size=0.3)
    lr = LinearRegression()
    lr.fit(x_train,y_train)
    file = open('house_model.pkl','wb')
    pickle.dump(lr,file)
    file.close()

if __name__ == '__main__':
    main()

