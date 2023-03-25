from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Questions, Friendship, UserProfile, QuestionsVerbal1, QuestionsVerbal3, QuestionsMath1, QuestionsVerbal2
from django.db.models import Q


@login_required
def friends(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    friend_requests = Friendship.objects.filter(friend=request.user, accepted=False)
    friends = Friendship.objects.filter(Q(user=request.user) | Q(friend=request.user), accepted=True)

    if request.method == 'POST':
        friend_username = request.POST.get('friend_username')
        friend = User.objects.filter(username=friend_username).first()

        if friend:
            friendship_request = Friendship.objects.filter(user=request.user, friend=friend).first()

            if not friendship_request:
                friendship = Friendship(user=request.user, friend=friend)
                friendship.save()

    return render(request, 'friends.html', {'friend_requests': friend_requests, 'friends': friends, 'user_profile':user_profile})

@login_required
def send_friend_request(request, username):
    friend = get_object_or_404(User, username=username)
    friendship, created = Friendship.objects.get_or_create(user=request.user, friend=friend)
    return redirect('myprofile')

@login_required
def accept_friend_request(request, friendship_id):
    friendship = get_object_or_404(Friendship, id=friendship_id, friend=request.user, accepted=False)
    friendship.accepted = True
    friendship.save()
    return redirect('myprofile')

@login_required()
def payment(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    users = User.objects.all()
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        user.is_staff = True
        user.save()
        return redirect('myprofile')
    else:
        users = User.objects.all()
        return render(request, 'payment.html', {'users': users, 'user_profile':user_profile})

@login_required()
def test(request):
    questions = Questions.objects.all()

    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.math_score = 0
    user_profile.verbal_score = 0
    user_profile.save()

    if request.method == 'POST':

        answers = []
        corrects = []
        for i in range(1, 15):
            question_1 = Questions.objects.get(number=i)
            correct_answer = question_1.correct
            corrects.append(correct_answer)

            answer1 = request.POST[f'answer{i}']
            answers.append(answer1)

        for j in range(1, 9):
            if answers[j-1] == corrects[j-1]:
                user_profile.verbal_score += 100
                user_profile.tokens += 100
                user_profile.save()

        for j in range(9, 15):
            if answers[j-1] == corrects[j-1]:
                user_profile.math_score += 114
                user_profile.tokens += 114
                user_profile.save()

        if user_profile.math_score > 100 and user_profile.verbal_score > 100:
            user_profile.numberoftest += 1
            user_profile.save()

        if request.user.is_staff:
            condition = 'sui'
            context = {'questions': questions, 'user_profile': user_profile, 'condition': condition}
            return render(request, 'test.html', context)
        else:
            return redirect('myprofile')

    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    context = {'questions':questions, 'user_profile': user_profile}

    return render(request, 'test.html', context)



@login_required()
def satverbaltest1(request):
    questions = QuestionsVerbal1.objects.all()

    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.verbal_score = 0
    user_profile.save()

    if request.method == 'POST':

        answers = []
        corrects = []
        for i in range(1, 5):
            question_1 = QuestionsVerbal1.objects.get(number=i)
            correct_answer = question_1.correct
            corrects.append(correct_answer)

            answer1 = request.POST[f'answer{i}']
            answers.append(answer1)

        for j in range(1, 5):
            if answers[j-1] == corrects[j-1]:
                user_profile.verbal_score += 300
                user_profile.tokens += 300
                user_profile.save()

        if user_profile.verbal_score > 100:
            user_profile.numberoftest += 1
            user_profile.save()

        if request.user.is_staff:
            condition = 'sui'
            context = {'questions': questions, 'user_profile': user_profile, 'condition': condition}
            return render(request, 'satverbaltest1.html', context)
        else:
            return redirect('myprofile')

    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    context = {'questions':questions, 'user_profile': user_profile}

    return render(request, 'satverbaltest1.html', context)

@login_required()
def satverbaltest2(request):
    questions = QuestionsVerbal2.objects.all()

    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.verbal_score = 0
    user_profile.save()

    if request.method == 'POST':

        answers = []
        corrects = []
        for i in range(1, 5):
            question_1 = QuestionsVerbal2.objects.get(number=i)
            correct_answer = question_1.correct
            corrects.append(correct_answer)

            answer1 = request.POST[f'answer{i}']
            answers.append(answer1)

        for j in range(1, 5):
            if answers[j-1] == corrects[j-1]:
                user_profile.verbal_score += 300
                user_profile.tokens += 300
                user_profile.save()

        if user_profile.verbal_score > 100:
            user_profile.numberoftest += 1
            user_profile.save()

        if request.user.is_staff:
            condition = 'sui'
            context = {'questions': questions, 'user_profile': user_profile, 'condition': condition}
            return render(request, 'satverbaltest2.html', context)
        else:
            return redirect('myprofile')

    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    context = {'questions':questions, 'user_profile': user_profile}

    return render(request, 'satverbaltest2.html', context)

@login_required()
def satmathtest1(request):
    questions = QuestionsMath1.objects.all()

    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.math_score = 0
    user_profile.save()

    if request.method == 'POST':

        answers = []
        corrects = []
        for i in range(1, 4):
            question_1 = QuestionsMath1.objects.get(number=i)
            correct_answer = question_1.correct
            corrects.append(correct_answer)

            answer1 = request.POST[f'answer{i}']
            answers.append(answer1)

        for j in range(1, 4):
            if answers[j-1] == corrects[j-1]:
                user_profile.math_score += 375
                user_profile.tokens += 375
                user_profile.save()

        if user_profile.math_score > 100:
            user_profile.numberoftest += 1
            user_profile.save()

        if request.user.is_staff:
            condition = 'sui'
            context = {'questions': questions, 'user_profile': user_profile, 'condition': condition}
            return render(request, 'satmathtest1.html', context)
        else:
            return redirect('myprofile')

    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    context = {'questions':questions, 'user_profile': user_profile}

    return render(request, 'satmathtest1.html', context)


@login_required()
def satmath(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'user_profile': user_profile}
    return render(request, 'satmath.html', context)

@login_required()
def satverbal(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'user_profile': user_profile}
    return render(request, 'satverbal.html', context)



@login_required()
def leaderboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)


    friendships = Friendship.objects.filter(Q(user=request.user) | Q(friend=request.user), accepted=True)
    friends_profile = []
    for friendship in friendships:
        friend = friendship.user if friendship.friend == request.user else friendship.friend
        friend_profile = UserProfile.objects.filter(user=friend).first()
        if friend_profile and friend_profile.profile_picture:
            friends_profile.append(friend_profile)

    context = {'user_profile': user_profile, 'friends_profile':friends_profile}
    return render(request, 'leaderboard.html', context)

@login_required()
def store(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    context = {'user_profile': user_profile}
    return render(request, 'store.html', context)

@login_required()
def myprofile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    if request.method == "POST" and request.FILES.get('profile_picture'):
        user_profile.profile_picture = request.FILES['profile_picture']
        user_profile.name = request.POST['name']
        user_profile.save()

    superscore = 0
    if user_profile.math_score:
        superscore = user_profile.math_score + user_profile.verbal_score

    name = user_profile.name

    context = {'user_profile': user_profile, 'superscore': superscore, 'name':name}
    return render(request, 'myprofile.html', context)

# auth
def signupsystem(request):
    if request.method == "GET":
        return render(request, 'signupsystem.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'signupsystem.html',
                          {'form': UserCreationForm, 'error': 'Passwords don\'t match!'})
        else:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                user_profile = UserProfile.objects.create(user=request.user)
                user_profile.math_score = 0
                user_profile.verbal_score = 0
                user_profile.tokens = 0
                user_profile.numberoftests = 0
                user_profile.save()

                return redirect('test')
            except IntegrityError:
                return render(request, 'signupsystem.html',
                              {'form': UserCreationForm, 'error': 'Username is already taken!'})


def loginsystem(request):
    if request.method == "GET":
        return render(request, 'index.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('myprofile')
        else:
            return render(request, 'index.html',
                          {'form': AuthenticationForm, 'error': 'Неверный логин и/или пароль'})


@login_required
def logoutsystem(request):
    if request.method == "POST":
        logout(request)
        return redirect('loginsystem')