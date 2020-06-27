import datetime

import numpy as np
from bert_serving.client import BertClient
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
import pymongo
from django.http import JsonResponse

# Create your views here.
from pymongo import collection


@login_required(login_url="sign_in_view")
def home_view(request):
    simArr = []
    print("---------SUBMIT REQUEST RECEIVED-----------");
    print("reading values from GET request...")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        claim = request.POST.get('claim')
        # contact_message  = request.POST.get('contact_message')
        ipc = request.POST['ipc']
        sector = request.POST['sector']
        insertPat = insertPatent(name, email, title, desc, claim, ipc, sector)
        # simArr.append(similarity)
        sim = (insertPat[0] * 100)
        print("calling insert values...")
        print("received values from GET request are...")
        print("values are successfully inserted to db")
        print("----------SUBMIT REQUEST PROCESSED-----------")
        print(" -name:   ", name)
        print(" -email:  ", email)
        print(" -title:  ", title)
        print(" -desc:   ", desc)
        print(" -claim:  ", claim)
        print(" -ipc:    ", ipc)
        print(" -sector: ", sector)
        context = {
            "similarity": sim,
            "print": insertPat[1],
        }
        return render(request, 'bert_result.html', context)
    return render(request, 'index.html')


@login_required(login_url="sign_in_view")
def logout_account(request):
    """
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect("sign_in_view")
    else:
        return redirect("home_view")


def sign_in_view(request):
    if request.method == "POST":
        email = request.POST.get("sign-up-email")
        password = request.POST.get("sign-up-password")
        user = User.objects.get(email=email)
        context = {
            "email": email
        }
        if user:
            if user.password == password:
                messages.success(request, "Successfully logged in")
                login(request, user)
            else:
                messages.error(request, "Password not matched")
                return render(request, "account-sign-in-cover.html", context)
        else:
            messages.error(request, "Kullanıcı bulunamadı.")
        return render(request, 'index.html')
    return render(request, 'account-sign-in-cover.html')


def sign_up_view(request):
    if request.method == "POST":
        print("---------SIGN UP REQUEST RECEIVED-----------");
        print("reading values from GET request...")
        #username=request.POST.get['username']
        email = request.POST.get['email']
        password = request.POST.get['pass']
        password_confirm=request.POST.get['password_confirm']
        print("received values from GET request are...")
        print(" -email :   ", email)
        print(" -pass  :   ", password)
        print("calling insert values...")
        user = User(email=email, password=password, password_confirm=password_confirm)
        user.email = "deneme"
        user.save()
        # insertAccount(email, password)
        print("values are successfully inserted to db")
        print("----------SIGNUP REQUEST PROCESSED-----------")
    return render(request, 'account-sign-up-cover.html')


# def insertAccount(email, password):
#     client = pymongo.MongoClient("mongodb://localhost:27017/")
#     # Database name: testdb
#     db = client["deneme"]
#     # collection name : accounts
#     collection = db["user"]
#     # query
#     query = {"email": email, "pass": password}
#     # execute query
#     collection.insert_one(query)
#     # user = User()


def forgot_password_view(request):
    return render(request, 'account-forgot-password.html', {})


def patent_one_view(request):
    return render(request, 'patent-1.html', {})


def patent_second_view(request):
    return render(request, 'patent-2.html', {})


def patent_third_view(request):
    return render(request, 'patent-3.html', {})


def patent_fourth_view(request):
    return render(request, 'patent-4.html', {})


def patent_fifth_view(request):
    return render(request, 'patent-5.html', {})


def contact_view(request):
    return render(request, 'contact.html', {})


def who_we_are_view(request):
    return render(request, 'who_we_are.html', {})


def our_vision_view(request):
    return render(request, 'our_vision.html', {})


def result_view(request):
    return render(request, 'result.html', {})


def bert_result_view(request):
    return render(request, 'bert_result.html', {})


# def submit(request):
#     print("---------SUBMIT REQUEST RECEIVED-----------");
#     print("reading values from GET request...")
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         title = request.POST.get('title')
#         desc = request.POST.get('desc')
#         claim = request.POST.get('claim')
#         # contact_message  = request.POST.get('contact_message')
#         ipc = request.POST['ipc']
#         sector = request.POST['sector']
#         similarity = insertPatent(name, email, title, desc, claim, ipc, sector)
#         return render(request, 'bert_result.html', {'similarity': str(similarity)})
#     print("received values from GET request are...");
#     print(" -name:   ", name)
#     print(" -email:  ", email)
#     print(" -title:  ", title)
#     print(" -desc:   ", desc)
#     print(" -claim:  ", claim)
#     print(" -ipc:    ", ipc)
#     print(" -sector: ", sector)
#     print("calling insert values...")
#
#     print("values are successfully inserted to db")
#     print("----------SUBMIT REQUEST PROCESSED-----------");
#     return render(request, 'index.html')


def getDescriptionListFromDB():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Database name: testdb
    db = client["testdb"]
    # collection name : patent
    collection = db["patent"]
    result = collection.find()

    descriptions = []
    for i in result:
        descriptions.append(i)
    return descriptions


def insertPatent(name, email, title, desc, claim, ipc, sector):
    with BertClient(port=5555, port_out=5556, check_version=False, check_length=False) as bc:
        retRes = []
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        import math
        query_vec_1 = bc.encode([desc])[0]

        valuesInDB = getDescriptionListFromDB()
        similarity = 0
        mostsimilarid = 0

        for y in valuesInDB:
            x = y['desc']
            patent_id = y['_id']
            query_vec_2 = bc.encode([x])[0]
            cosine = np.dot(query_vec_1, query_vec_2) / (np.linalg.norm(query_vec_1) * np.linalg.norm(query_vec_2))
            local = 1 / (1 + math.exp(-100 * (cosine - 0.95)))
            retRes.append(str(local) + "-" + x)
            print(retRes)
            if local > similarity:
                similarity = local
                mostsimilarid = patent_id

        # Database name: testdb
        db = client["deneme"]
        # collection name : patent
        collection = db["patent"]
        # query
        query = {"name": name, "email": email, "title": title, "desc": desc, "claim": claim, "ipc": ipc,
                 "sector": sector, "sim": similarity, 'similar_id': mostsimilarid}
        # execute query
        collection.insert_one(query)
        return [similarity, retRes]


def controlUser(email, password):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["testdb"]
    collection = db["accounts"]
    query = {"email": email, "password": password}
    collection.find(query)
