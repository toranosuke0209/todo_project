from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

def task_contact(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        send_mail(
            subject=f'Task Inquiry: {task.title}',  # タスクのタイトルを件名に含める
            message=f'Task details:\n{task.description}',  # タスクの説明を本文に含める
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['dayuantailang1@gmail.com'],  # 管理者のメールアドレス
            fail_silently=False,
        )
        return redirect('contact_success')
    return render(request, 'todo/task_contact.html', {'task': task})


#def task_contact(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        # メール送信処理をここに追加
        return redirect('contact_success')
    return render(request, 'todo/task_contact.html', {'task': task})

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

def contact(request):
    if request.method == 'POST':
        # ユーザーから送信されたデータを取得
        subject = request.POST.get('subject', 'No Subject')  # 件名
        message = request.POST.get('message', 'No Message')  # メッセージ
        sender_email = request.POST.get('email', 'no-reply@example.com')  # 送信者のメールアドレス

        # メールを送信
        send_mail(
            subject=subject,
            message=message,
            from_email=sender_email,  # ユーザーのメールアドレス
            recipient_list=['dayuantailang1@gmail.com'],  # 管理者のメールアドレス
            fail_silently=False,
        )

        # 成功ページにリダイレクト
        return redirect('contact_success')

    return render(request, 'todo/contact.html')


#def contact(request):
    if request.method == 'POST':
        send_mail(
            subject=f'Task Inquiry: {task.title}',  # タスクのタイトルを件名に含める
            message=f'Task details:\n{task.description}',  # タスクの説明を本文に含める
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['dayuantailang1@gmail.com'],  # 管理者のメールアドレス
            fail_silently=False,
        )
        return redirect('contact_success')
    return render(request, 'todo/contact.html')

def contact_success(request):
    return render(request, 'todo/contact_success.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'todo/signup.html', {'form': form})

def send_welcome_email(user_email):
    send_mail(
        'Welcome!',
        'Thank you for signing up.',
        'your_email@example.com',
        [user_email],
        fail_silently=False,
    )

