from .models import Tweet
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TweetForm,UserRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')              # Get all the tweets in order of creation
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method=='POST':                      # If form is filled and submitted, we get post request
        form=TweetForm(request.POST,request.FILES)  # If file is uploaded in the form, we use request.FILES
        if form.is_valid():                         # Check if form is valid or not
            tweet=form.save(commit=False)           # save in the tweet but not in database
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm()        # Provide empty form to user

    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # Ensure tweet belongs to the logged-in user
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

def register(request):
    if request.method=='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])       # Set password for the user
            user.save()
            login(request,user)                                     # Login the user automatically
            return redirect('tweet_list')                           # Redirect to tweet_list page
    else:
        form=UserRegistration()

    return render(request,'registration/register.html',{'form':form})