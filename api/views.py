from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
import requests


def index(request):

    context = {}

    input = request.POST.get("foodName")

    if input:

        api_id = 'YOUR API ID'
        api_key = 'YOUR API KEY'
        body = '?results=0:1&fields=*&'
        url = 'https://api.nutritionix.com/v1_1/search/'+input + \
            body+'appId='+api_id+'&appKey='+api_key

        response = requests.get(url)

        meta_data = response.json()

        data1 = meta_data['hits']

        data2 = data1[0]

        data3 = data2['fields']

        # eventually reaching fields of api. Now, we can use data of nutritionxAPI

        nutrition_name = data3['item_name']
        nutrition_size = data3['nf_serving_size_unit']
        nutrition_calories = data3['nf_calories']
        nutrition_protein = data3['nf_protein']
        nutrition_carb = data3['nf_total_carbohydrate']
        nutrition_fat = data3['nf_total_fat']
        nutrition_sugar = data3['nf_sugars']

        context = {
            "nutrition_name": nutrition_name,
            "nutrition_size": nutrition_size,
            "nutrition_calories": nutrition_calories,
            "nutrition_protein": nutrition_protein,
            "nutrition_carb": nutrition_carb,
            "nutrition_fat": nutrition_fat,
            "nutrition_sugar": nutrition_sugar
        }

    return render(request, "indexAPI.html", context)
