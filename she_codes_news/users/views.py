from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'userProfile'
    queryset = CustomUser.objects.all()

    def get_object(self):
        UserName = self.kwargs.get("username")
        return get_object_or_404(CustomUser, username=UserName)

class EditProfileView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/editProfile.html'

    def get_object(self):
        UserName = self.kwargs.get("username")
        return get_object_or_404(CustomUser, username=UserName)

    def get_success_url(self):
        success_url = reverse_lazy('users:userProfile', kwargs={'username': self.request.user.username})
        return success_url



