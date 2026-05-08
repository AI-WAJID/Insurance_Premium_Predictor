from django.shortcuts import render, HttpResponse
import joblib

model = joblib.load('model/random_forest_regressor')
# Create your views here.
def index(req):
    #return HttpResponse('This is the home page.')
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def contact(req):
    return render(req, 'contact.html')

def login(req):
    return render(req, 'login.html')

def registration(req):
    return render(req, 'registration.html')

def prediction(req):
    if req.method == "POST":
        age = int(req.POST.get('age'))
        sex = int(req.POST.get('sex'))
        bmi = float(req.POST.get('bmi'))
        children = int(req.POST.get('children'))
        smoker = int(req.POST.get('smoker'))
        region = int(req.POST.get('region'))

        pred = model.predict([[age, sex, bmi, children, smoker, region]])
        prediction_value = round(float(pred[0]), 2)

        output = {
            'output': prediction_value
        }

        return render(req, 'prediction.html', output)

    else:
        return render(req, 'prediction.html')