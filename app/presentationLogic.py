from app.businessLogic import *
from app.wikidataInterface import *
from app.inferences import *

# Get all the metrics and values of one country
# Returned in the format: ({"uri": uri of predicate, "url": url of predicate, "label": name of predicate}, value of predicate in country)
def getParsedMetricsOfCountry(country):
    metrics = getMetricsOfCountry(BASE_URL+"/country/"+country)
    pred = getAllPredicateNames()
    parsedMetrics = []
    for metric in metrics:
        for value in metrics[metric]:
            for p in pred:
                if metric==p:
                    metric_name = value
                    pred_nameof = ""
                    url=""
                    if len(value.split("/"))>1:
                        # Check if URI is not from a country
                        metric_name = getNameOfSubject(value)
                        if len(metric_name)>0:
                            metric_name = metric_name[0]
                            pred_nameof="foaf:name"
                        else:
                            # URI is from a contry
                            metric_name = getNameCountryByURI(value)
                            url = value.split("/")[-1]
                            if len(metric_name)>0:
                                metric_name = metric_name[0]
                                pred_nameof = "countries:countryPredicate/1"

                    parsedMetrics += [({"uri":p ,"url":p.split("/")[-1],"label":pred[p]}, {"url":url, "uri": value,"value": metric_name, "pred_nameof":pred_nameof})]
                    continue
    return parsedMetrics

# Return list (URI, url, label) of all countries
def getListOfCountries():
    countries = getAllCountries()
    listCountries = [{"uri":uri.split("/", 7)[-1], "url":uri.split("/")[-1], "label":countries[uri]} for uri in countries]
    return listCountries

# Returns list with all countries that have a metric, and its value
# In the form {uri of country, label of country, url of country}, label)
def getParsedAllCountriesByMetric(metric_uri):
    parsedMetrics = []
    countries = getAllCountriesByMetric(metric_uri)
    allCountries = getAllCountries()
    for country in countries:
        label = country
        if(country in allCountries):
            label = allCountries[country]
        for value in countries[country]:
            pred_nameof = ""
            url = ""
            if len(value.split("/")) > 1:
                # Check if URI is not from a country
                names = getNameOfSubject(value)
                if len(names) > 0:
                    names = names[0]
                    pred_nameof="foaf:name"
                else:
                    # URI is from a contry
                    names = getNameCountryByURI(value)
                    url = value.split("/")[-1]
                    if len(names) > 0:
                        names = names[0]
                        pred_nameof="countries:countryPredicate/1"
            else:
                names = value
            parsedMetrics += [({"uri":country, "label":label, "url": country.split("/")[-1]}, {"url":url, "uri": value,"value": names, "pred_nameof":pred_nameof})]
    return parsedMetrics

# Returns the name of a country given an URI, if it exists
def getCountryName(country_id):
    names = getNameCountryByURI(BASE_URL+"/country/"+country_id)
    if len(names)>0:
        return names[0]
    else:
        return None

# Returns the name of one metric given an URI
def getMetricName(metric_id):
    metrics = getAllPredicateNames()
    name = [metrics[elem] for elem in metrics if elem==metric_id]
    if len(name)>0:
        return name[0]
    else:
        return None

# Return list of predicates
def getListOfPredicates():
    predicates = getAllPredicateNames()
    listPredicates = [{"name": predicates[elem], "id": elem.split("/")[-1]} for elem in predicates]
    return listPredicates

# Parse the reflexive inferences to get the label and url of each entity
def getParsedReflexiveInferences():
    relations = getReflexiveInferences()
    parsedRelations = {}
    for rel in relations:
        sub = getNameOfSubject(rel)
        if len(sub)>0:
            sub = sub[0]
        parsedRelations[rel] = {"label":sub, "url": rel.split("/")[-1], "content":{}}

        for entity1 in relations[rel]:
            name = getNameCountryByURI(entity1)
            if len(name)>0:
                name = name[0]
            parsedRelations[rel]["content"].update({entity1:{}})
            parsedRelations[rel]["content"][entity1].update({"label":name, "url": entity1.split("/")[-1], "content":{}})

            for entity2 in relations[rel][entity1]:
                name = getNameCountryByURI(entity2)
                if len(name)>0:
                    name = name[0]
                parsedRelations[rel]["content"][entity1]["content"].update({entity2:{}})
                parsedRelations[rel]["content"][entity1]["content"][entity2].update({"label":name, "url": entity2.split("/")[-1]})

    return parsedRelations

# Returns the favorite countries of one user
def getParsedFavoriteCountries(user_id):
    favos = getFavoriteCountries(str(user_id))
    parsedFavos = []
    for favo in favos:
        name = getNameCountryByURI(favo)[0]
        url = favo.split("/")[-1]
        uri = favo.split("/", 7)[-1]
        parsedFavos += [{"uri": uri, "url": url, "label": name}]
    return parsedFavos

def getParsedCountriesMoreInternetTraffic():
    netTraffic = getCountriesWithMoreInternetTraffic()
    parsednetTraffic = []
    for idx, country in enumerate(netTraffic):
        name = getNameCountryByURI(country)[0]
        url = country.split("/")[-1]
        uri = country.split("/", 7)[-1]
        parsednetTraffic += [{"uri": uri, "url": url, "label": name, "predURI": "rankMoreInternetTraffic", "value": str(idx+1)}]
    return parsednetTraffic

def getParsedCountriesToInvest():
    invest = getBestCountriesToInvest()
    parsedInvest = []
    for idx, country in enumerate(invest):
        name = getNameCountryByURI(country)[0]
        url = country.split("/")[-1]
        uri = country.split("/", 7)[-1]
        parsedInvest += [{"uri": uri, "url": url, "label": name, "predURI": "rankBestCountriesToInvest", "value": str(idx+1)}]
    return parsedInvest

def getParsedCountriesToLive():
    tolive = getBestCountriesToLive()
    parsedToLive = []
    for idx, country in enumerate(tolive):
        name = getNameCountryByURI(country)[0]
        url = country.split("/")[-1]
        uri = country.split("/", 7)[-1]
        parsedToLive += [{"uri": uri, "url": url, "label": name, "predURI": "rankBestCountriesToLive", "value": str(idx+1)}]
    return parsedToLive

def checkIfFavorite(user_id, country):
    favo = getFavoriteCountries(str(user_id))
    if BASE_URL+"/country/"+country in favo:
        return True
    return False
