from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View


class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', context={'form': form})

    def post(self, request):
        bound_form = UserCreationForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect(reverse('posts_list_url'))
        return render(request, 'registration/signup.html', context={'form': bound_form})
