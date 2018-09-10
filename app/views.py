from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from app.presentationLogic import *
from app.wikidataInterface import *
from app.inferences import *

'''
    Home page of InfoCountries
'''
@login_required(login_url='/login/')
def home(request):
    countries = getListOfCountries()
    return render(
        request,
        'app/home.html',
        {
            'title': 'Countries',
            'year': datetime.now().year,
            'countries': countries
        }
    )

@login_required(login_url='/login/')
def predicates(request):
    predicates = getListOfPredicates()
    return render(
        request,
        'app/predicates.html',
        {
            'title': 'Predicates',
            'year': datetime.now().year,
            'predicates': predicates
        }
    )

# Tries to create new predicates with data from wikidata
@login_required(login_url='/login/')
def reload(request, country):

    country_name = getCountryName(country)
    wikiCountry = getWikidataCountryEntity(country_name)
    try:
        createCountryNewPredicates(country, wikiCountry)
    except Exception as e:
        print(e)
        print("Could not gather data from country "+str(country))
    return redirect('country', country=country)

# Tries to create new relations between countries with data from wikidata
@login_required(login_url='/login/')
def relations(request, country):
    country_name = getCountryName(country)
    wikiCountry = getWikidataCountryEntity(country_name)
    try:
        createCountriesRelations(country, wikiCountry)
    except Exception as e:
        print(e)
        print("Could not gather data from country " + str(country))
    return redirect('country', country=country)

@login_required(login_url='/login/')
def country(request, country):
    hasWiki = checkCountryHasWikidata(country)
    hasRelations = checkCountryHasWikidataRelations(country)
    metrics = getParsedMetricsOfCountry(country)

    # Tries to get the image URL from wikidata
    try:
        country_name = getCountryName(country)
        wikiCountry = getWikidataCountryEntity(country_name)
        image_URL = getWikidataImageURL(wikiCountry)
    except Exception as e:
        image_URL = ""
        print(e)
        print("Could not gather data from country "+str(country))
    favo = checkIfFavorite(request.user.id, country)
    return render(
        request,
        'app/country.html',
        {
            'title': country_name,
            'year': datetime.now().year,
            'country_id': country,
            'metrics': metrics,
            'image': image_URL,
            'has_wiki': hasWiki,
            'has_relations': hasRelations,
            'favorite': favo
        }
    )

@login_required(login_url='/login/')
def metric(request, metric):
    try:
        # If first element is int, is local metric
        test = int(metric[0])
        url = BASE_URL+"/countryProperty/"+metric

    # Otherwise, it is wikidata metric
    except Exception as e:
        url = WIKIDATA_BASEURL+metric

    countries = getParsedAllCountriesByMetric(url)
    metric_name = getMetricName(url)
    if metric_name==None:
        metric_name="Metric"
    return render(
        request,
        'app/metrics.html',
        {
            'title': metric_name,
            'metric': url,
            'year': datetime.now().year,
            'countries': countries
        }
    )

@login_required(login_url='/login/')
def inferences(request, success):
    refInferences = getParsedReflexiveInferences()
    return render(
        request,
        'app/inferences.html',
        {
            'title': "Inferences",
            'year': datetime.now().year,
            'inferences': refInferences,
            'success': True if success=="success" else False
        }
    )

@login_required(login_url='/login/')
def statistics(request):
    tolive = getParsedCountriesToLive()
    nettraffic = getParsedCountriesMoreInternetTraffic()
    toinvest = getParsedCountriesToInvest()
    return render(
        request,
        'app/statistics.html',
        {
            'title': "Statistics",
            'tolive': tolive,
            'toinvest': toinvest,
            'nettraffic': nettraffic,
            'year': datetime.now().year,
        }
    )    

@login_required(login_url='/login/')
def saveinferences(request):
    addRelations(getReflexiveInferences())
    return redirect('inferences', success="success")

@login_required(login_url='/login/')
def favorites(request):
    favorites = getParsedFavoriteCountries(request.user.id)
    return render(
        request,
        'app/favorites.html',
        {
            'title': "Favorites",
            'year': datetime.now().year,
            'favorites': favorites
        }
    )

@login_required(login_url='/login/')
def changeFavorite(request, country):
    favo = checkIfFavorite(str(request.user.id), country)
    if favo:
        removeFromFavorites(str(request.user.id), country)
    else:
        addToFavorites(str(request.user.id), country)
    return redirect('country', country=country)

'''
    Register page
'''
def registar(request):

    # If form is valid, register new user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()
    return render(request,
                  'app/registar.html',
                  {
                      'title': 'Register',
                      'form': form,
                      'year': datetime.now().year
                   })