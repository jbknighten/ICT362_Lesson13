from django.shortcuts import render


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topic(request, topic_id):
    """Show a page for a specific learning topic."""
    context = {'topic_id': topic_id}
    return render(request, 'learning_logs/topic.html', context)