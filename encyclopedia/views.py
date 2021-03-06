from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files import File
from . import util,forms
from random import choice

form = forms.NewSearchForm()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_page(request,title):
    page = util.get_entry(title)
    if page is None:
        # no page found
        return render(request,"encyclopedia/error.html",{
            "form":form
        })
    # page found
    return render(request,"encyclopedia/titlepage.html",{
        'title': title,
        'content': page,
        "form":form,
    })

def get_search_query(request):

    if request.method == "GET":
        form = forms.NewSearchForm(request.GET)

        if form.is_valid():
            searchquery = form.cleaned_data["search"].lower()
            all_entries = util.list_entries()


            files=[filename for filename in all_entries if searchquery in filename.lower()]


            if len(files) == 0:


                return render(request,"encyclopedia/search_results.html",{
                    'error' : "No results found",
                    "form":form
                })


            elif len(files) == 1 and files[0].lower() == searchquery:
                title = files[0]
                return get_page(request, title)

            else:

                title = [filename for filename in files if searchquery == filename.lower()]

                if len(title)>0:
                    return get_page(request, title[0])
                else:
                    return render(request,"encyclopedia/search_results.html",{
                        'results':files,
                        "form":form

                    })

        else:
            # not a valid request
            return index(request)


    return index(request)


def new_page(request):

    if request.method == "GET":
        create_form= forms.NewPageForm()
        return render(request, "encyclopedia/create_page.html",{
            "form":form,
            "create_form":create_form

        })
    else:
        create_form = forms.NewPageForm(request.POST)
        if create_form.is_valid():

            title = create_form.cleaned_data["pagename"]
            body = create_form.cleaned_data["body"]
            all_entries = util.list_entries()
            for filename in all_entries:
                if title.lower()== filename.lower():
                    create_form = forms.NewPageForm()
                    error_message="Title already exist '%s'. \n please try another title!" %filename
                    return render(request, "encyclopedia/create_page.html",{
                        "form":form,
                        "create_form":create_form,
                        "error":error_message
                    })

            util.save_entry(title,body)
            return get_page(request, title)

        else:

            return render(request, "encyclopedia/create_page.html",{
            "form":form,
            "create_form":create_form

        })


def edit_page(request):

    pagename = request.POST.get("edit")

    content = util.get_entry(pagename)

    edit_form = forms.EditPageForm(initial={'pagename': pagename, 'body':content})
    if edit_form.is_valid():

        return render (request, "encyclopedia/edit_page.html",{
                "title": pagename,
                "form":form,
                "edit_form":edit_form

            })
    else:
        return render (request, "encyclopedia/edit_page.html",{
                "title": pagename,
                "form":form,
                "edit_form":edit_form

        })


def save_page(request):

    edit_form = forms.EditPageForm(request.POST)

    if edit_form.is_valid():

        pagename = edit_form.cleaned_data["pagename"]
        content = edit_form.cleaned_data["body"]

        val = util.save_entry(pagename,content)

        return get_page(request, pagename)

    else:
        return render (request, "encyclopedia/edit_page.html",{
                "form":form,
                "edit_form":edit_form

        })


def random_page(request):

    return get_page(request,choice( util.list_entries()))
