from django.shortcuts import render

def bounty_list(request):
    return render(request, 'bounties/bounty_list.html', {})