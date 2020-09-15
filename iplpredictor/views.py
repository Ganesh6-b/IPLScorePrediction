from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import pickle
regressor = pickle.load(open('iplregressor.pkl', 'rb'))
# Create your views here.
def home(request):
    return render(request, 'home.html')
def score(request):
    if request.method == 'POST':
        bat_team = request.POST['bat_team']
        bowl_team = request.POST['bowl_team']
        overs = float(request.POST['overs'])
        runs = int(request.POST['runs'])
        wickets = int(request.POST['wickets'])
        temp_array = list()
        if bat_team != bowl_team:
            if bat_team == 'Chennai Super Kings':
                temp_array = temp_array + [1,0,0,0,0,0,0,0]
            elif bat_team == 'Delhi Daredevils':
                temp_array = temp_array +  [0,1,0,0,0,0,0,0]
            elif bat_team == 'Kings XI Punjab':
                temp_array = temp_array + [0,0,1,0,0,0,0,0]
            elif bat_team == 'Kolkata Knight Riders':
                temp_array = temp_array + [0,0,0,1,0,0,0,0]
            elif bat_team == 'Mumbai Indians':
                temp_array = temp_array + [0,0,0,0,1,0,0,0]
            elif bat_team == 'Rajanthan Royals':
                temp_array = temp_array + [0,0,0,0,0,1,0,0]
            elif bat_team == 'Royal Challengers Bangalore':
                temp_array = temp_array + [0,0,0,0,0,0,1,0]
            elif bat_team == 'Sunrisers Hyderabad':
                temp_array = temp_array + [0,0,0,0,0,0,0,1]
            if bowl_team == 'Chennai Super Kings':
                temp_array = temp_array + [1,0,0,0,0,0,0,0]
            elif bowl_team == 'Delhi Daredevils':
                temp_array = temp_array + [0,1,0,0,0,0,0,0]
            elif bowl_team == 'Kings XI Punjab':
                temp_array = temp_array + [0,0,1,0,0,0,0,0]
            elif bowl_team == 'Kolkata Knight Riders':
                temp_array =temp_array +  [0,0,0,1,0,0,0,0]
            elif bowl_team == 'Mumbai Indians':
                temp_array = temp_array + [0,0,0,0,1,0,0,0]
            elif bowl_team == 'Rajasthan Royals':
                temp_array = temp_array + [0,0,0,0,0,1,0,0]
            elif bowl_team == 'Royal Challengers Bangalore':
                temp_array = temp_array + [0,0,0,0,0,0,1,0]
            elif bowl_team == 'Sunrisers Hyderabad':
                temp_array = temp_array + [0,0,0,0,0,0,0,1]
        else:
            return HttpResponse("Enter the valid teams!!!")
#        cols = ['bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils','bat_team_Kings XI Punjab', 'bat_team_Kolkata Knight Riders','bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals','bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad','bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils','bowl_team_Kings XI Punjab', 'bowl_team_Kolkata Knight Riders','bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals','bowl_team_Royal Challengers Bangalore','bowl_team_Sunrisers Hyderabad', 'runs', 'wickets', 'overs']
        temp_array = temp_array + [overs, runs, wickets]
        data = np.array([temp_array])
        score_lst = []
        for i in range(10):
            scr = int(regressor.predict(data)[0])
            score_lst.append(scr)
        scores = int(sum(score_lst)/len(score_lst))
        scores_from = scores - 10
        scores_to = scores + 10
        context = {'score_from' : scores_from, "score_to" : scores_to}
        return render(request,'home.html', context = context)
    else:
        return render(request,'home.html')