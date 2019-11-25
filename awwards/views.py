def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        posts = Post.objects.all()
        posts = posts[::-1]
        a_post = random.randint(0, len(posts)-1)
        random_post = posts[a_post]
    except Post.DoesNotExist:
        posts = None
    return render(request, 'awwards/index.html', {'posts': posts, 'form': form, 'random_post': random_post})

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('index')
        else:
            form = SignupForm()
        return render(request,'registration/registration_form',{'form':form})


# Create your views here.
def index(request):
    return render(request,'awwards/index.html')