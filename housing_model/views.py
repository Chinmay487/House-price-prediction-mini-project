
import pickle

# Create your views here.
def say_hello():
    print('Hello')

# Avg. Area Income,Avg. Area House Age,Avg. Area Number of Rooms,Avg. Area Number of Bedrooms,Area Population,Price,Address


def predict_price(**features):
    file=open('house_model.pkl', 'rb')
    lr=pickle.load(file)  #used to read data from file
    file.close()
    prediction = lr.predict([[ parameter for parameter in [value for value in features.values()] ]])
    return prediction

