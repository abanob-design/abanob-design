from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"app2/index.html")


def user(request):

      user_list = user.objects.order_by('First')
      user_dic = {'use':user_list}
      return render (request,"app2/users.html",context=user_dic)
