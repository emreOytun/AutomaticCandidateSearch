from django.shortcuts import render, HttpResponse, redirect

from employeeSearching.models import Candidate
from github import Github

class GithubSearchingService() : 
    def __init__(self, access_token) :
        self.candidates = []
        self.g = Github(access_token)

    def __add_to_candidates(self, user) :
        newCandidate = Candidate(name = user.name, location = user.location, email = user.email, company = user.company, bio = user.bio, blog = user.blog, userHtmlUrl = user.html_url)
        self.candidates.append(newCandidate)

    def __save_candidates(self) :
        for candidate in self.candidates :
            candidate.save()

    def search(self, query, keyword, max_count) :  
        self.candidates = []
        count = 0

        if not query : 
            return
        
        if keyword :
            keyword = keyword.lower()
            keyword_list = keyword.split()
            for user in self.g.search_users(query):
                #print(user.name)
                #print(user.blog)
            
                if user.bio :
                    if keyword_list[0] in user.bio.lower() :
                        if not Candidate.objects.filter(userHtmlUrl = user.html_url).exists() :
                            self.__add_to_candidates(user)
                        print("BULUNDU1")
                        count += 1

                if count == max_count:
                    self.__save_candidates()
                    return

        else :
            for user in self.g.search_users(query):
                #print(user.name)
                #print(user.blog)
            
                if not Candidate.objects.filter(userHtmlUrl = user.html_url).exists() :
                    self.__add_to_candidates(user)
                    print("BULUNDU1")
                    count += 1

                if count == max_count:
                    self.__save_candidates()
                    return

# Create your views here.
def index(request) :
    #return HttpResponse("Anasayfa");
    context = {
        "candidates" : Candidate.objects.all()
    }

    return render(request, "index.html", context)

def searchGithub(request) :
    if request.method == "GET":
        return redirect("/")
    else :
        language = request.POST.get("language")
        location = request.POST.get("location")
        keyword = request.POST.get("keyword")
        
        searchEngine = GithubSearchingService("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")
        searchEngine.search("language:" + language + " location:" + location + " language:Kotlin language:Java language:Html", keyword, 1)
        return redirect("/")
