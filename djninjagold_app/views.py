from django.shortcuts import render, redirect
import random, math

def index(request):
    if "total_gold" not in request.session:
        request.session["total_gold"] =0
    if  "activities" not in request.session:
        request.session["activities"]=[]

    return render(request, "index.html")

def process_money(request):
    print(request.POST)
    if request.POST['places'] == 'farm':
        total_gold = random.randint(10,20)
        request.session["total_gold"] += total_gold
        request.session["activities"].append(f"at the farm I earned {total_gold}")
    if request.POST['places'] == 'cave':
        total_gold = random.randint(5,10)
        request.session["total_gold"] += total_gold
        request.session["activities"].append(f"at the cave I found {total_gold}")
    if request.POST['places'] == 'house':
        total_gold = random.randint(2,5)
        request.session["total_gold"] += total_gold
        request.session["activities"].append(f"at the house my mum gave me {total_gold}")
    if request.POST['places'] == 'casino':
        total_gold = random.randint(-50, 50)
        request.session["total_gold"] += total_gold
        if total_gold >0:
            request.session["activities"].append(f"I went to the casino and won {total_gold}")
        else:
            request.session["activities"].append(f"I lost {abs(total_gold)} at the casino")
    return redirect("/")
def reset(request):
    request.session.clear()
    return redirect("/")

