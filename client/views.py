
from django.shortcuts import render
from housing_model.views import predict_price
import math

price = None
def home(request):
    return render(request,'input.html',{'page_title':'Home Page','result':False,'price':None})


def result(request):
    price = predict_price(
                    Avg_Area_Income=eval(request.POST['Avg_Area_Income']),
                    Avg_Area_House_Age=eval(request.POST['Avg_Area_House_Age']),
                    Avg_Area_Number_of_Rooms=eval(request.POST['Avg_Area_Number_of_Rooms']),
                    Avg_Area_Number_of_Bedrooms=eval(request.POST['Avg_Area_Number_of_Bedrooms']),
                    Area_Population=eval(request.POST['Area_Population'])
                    )
    return render(request,'input.html',{'page_title':'Home Page','result':True,'price':math.ceil(price)})



# Avg_Area_Income=100_000,
#                     Avg_Area_House_Age=2,
#                     Avg_Area_Number_of_Rooms=4.0,
#                     Avg_Area_Number_of_Bedrooms=3.0,
#                     Area_Population=10_000