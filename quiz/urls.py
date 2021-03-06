from django.urls import path
from .views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('about', About.as_view(), name='about'),
    path('intro', Intro.as_view(), name='intro'),
    path('resetpassword/<str:token>', PasswordReset.as_view(), name='reset_password'),
    path('<slug:bubble_name>/forgotpassword', ForgotPassword.as_view(), name='forgot_password'),
    path('<slug:bubble_name>/requestpassword', RequestPassword.as_view(), name='request_password'),
    path('<slug:bubble_name>/logout', Logout.as_view(), name='logout'),
    path('<slug:bubble_name>', Home.as_view(), name='home'),
    path('<slug:bubble_name>/settings', Settings.as_view(), name='settings'),
    path('<slug:bubble_name>/newquestion', NewQuestion.as_view(), name='new_question'),
    path('<slug:bubble_name>/quiz/<int:quiz_id>', QuizView.as_view(), name='quiz'),
    path('<slug:bubble_name>/questionlist', QuestionList.as_view(), name='question_list'),
    path('<slug:bubble_name>/questionedit/<int:question_id>', EditQuestion.as_view(), name='edit_question'),
]