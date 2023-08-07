from django.shortcuts import render
import requests

def analyze_repository(request):
    if request.method == 'POST':
        repository_link = request.POST.get('repository_link')
        owner, repo_name = extract_owner_and_repo(repository_link)
        response = requests.get(f'https://api.github.com/repos/{owner}/{repo_name}')
        if response.status_code == 200:
            repository_data = response.json()
            return render(request, 'analyzer/preview.html', {'repository_data': repository_data})
        else:
            error_message = 'Unable to fetch repository details. Please check the link and try again.'
            return render(request, 'analyzer/error.html', {'error_message': error_message})
    else:
        return render(request, 'analyzer/index.html')

def extract_owner_and_repo(repository_link):
    parts = repository_link.split('/')
    owner = parts[-2]
    repo_name = parts[-1]
    return owner, repo_name