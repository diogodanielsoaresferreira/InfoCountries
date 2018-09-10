from app.dbInterface import *

# Get the URI's and labels of all countries
def getAllCountries():
    query = """
        PREFIX countries: <"""+BASE_URL+"""/countryProperty/>
        select ?country ?country_name
        WHERE{
            ?country countries:1 ?country_name
        }
        """
    results = executeQuery(query)
    countries = {}
    for result in results["results"]["bindings"]:
        countries[result["country"]["value"]] = result["country_name"]["value"]
    return countries

# Get the metrics of all countries
def getAllCountryMetrics():
    query = """
        PREFIX countries: <"""+BASE_URL+"""/countryProperty/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        select distinct ?predicate ?predicate_name
        WHERE{
            ?country countries:1 ?country_name .
            ?country ?predicate ?value .
            ?predicate foaf:name ?predicate_name .
        }
        """

    results = executeQuery(query)
    predicates = {}
    for result in results["results"]["bindings"]:
        predicates[result["predicate"]["value"]] = result["predicate_name"]["value"]
    return predicates

# Get the metrics URI and label all metrics of one country
def getMetricsOfCountry(country_uri):
    query = """
        PREFIX countries: <"""+BASE_URL+"""/countryProperty/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        select ?predicate ?value
        WHERE{
            ?country ?predicate ?value .
            filter(?country=<"""+country_uri+""">) .
        }
        """
    results = executeQuery(query)
    predicates = {}
    for result in results["results"]["bindings"]:
        if(result["predicate"]["value"] not in predicates):
            predicates[result["predicate"]["value"]] = [result["value"]["value"]]
        else:
            predicates[result["predicate"]["value"]] += [result["value"]["value"]]
    return predicates

# Get the name and URI of all the predicates
def getAllPredicateNames():
    query = """
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            select distinct ?predicate ?predicate_name
            WHERE{
                ?subject ?predicate ?value .
                ?predicate foaf:name ?predicate_name .
            }
            """

    results = executeQuery(query)
    predicates = {}
    for result in results["results"]["bindings"]:
        predicates[result["predicate"]["value"]] = result["predicate_name"]["value"]
    return predicates

# Get all countries that have one metric
def getAllCountriesByMetric(metric_uri):
    query = """
            PREFIX countries: <""" + BASE_URL + """/countryProperty/>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            select distinct ?country ?value
            WHERE{
                ?country ?metric ?value .
                filter(?metric=<"""+metric_uri+""">) .
            }
            """
    results = executeQuery(query)
    countries = {}
    for result in results["results"]["bindings"]:
        if (result["country"]["value"] not in countries):
            countries[result["country"]["value"]] = [result["value"]["value"]]
        else:
            countries[result["country"]["value"]] += [result["value"]["value"]]
    return countries

# Get name of subject(URI)
def getNameOfSubject(subject):
    query = """
                PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                select distinct ?name
                WHERE{
                    ?subject foaf:name ?name .
                    filter(?subject=<"""+subject+""">) .
                }
                """

    results = executeQuery(query)
    predicates = []
    for result in results["results"]["bindings"]:
        predicates += [result["name"]["value"]]
    return predicates

# Get country URI by its name
def getCountryURIByName(name):
    query = """
            PREFIX countries: <"""+BASE_URL+"""/countryProperty/>
            select ?countryURI
            WHERE{
                ?countryURI countries:1 ?name .
                filter(?name=\"""" + name + """\") .
            }
            """

    results = executeQuery(query)
    predicates = []
    for result in results["results"]["bindings"]:
        predicates += [result["countryURI"]["value"]]
    return predicates

# Get country name by its URI
def getNameCountryByURI(uri):
    query = """
            PREFIX countries: <""" + BASE_URL + """/countryProperty/>
            select ?name
            WHERE{
                ?countryURI countries:1 ?name .
                filter(?countryURI=<""" + uri + """>) .
            }
            """

    results = executeQuery(query)
    predicates = []
    for result in results["results"]["bindings"]:
        predicates += [result["name"]["value"]]
    return predicates

def getFavoriteCountries(user_id):
    query = """
        PREFIX base: <""" + BASE_URL + """/>
        select distinct ?country
        WHERE{
            ?user base:favorite ?country .
            filter(?user=<""" + BASE_URL+"/user/"+user_id + """>) .
        }
        """
    results = executeQuery(query)
    predicates = []
    for result in results["results"]["bindings"]:
        predicates += [result["country"]["value"]]
    return predicates

def addToFavorites(user_id, countryURI):
    data = "<"+BASE_URL+"/user/"+user_id+"> <"+BASE_URL+"/favorite"+"> <"+BASE_URL+"/country/"+countryURI+"> .\n"
    update = """INSERT DATA{""" + data + """}"""
    ins = executeInsert(update)
    if len(ins) != 0:
        print(ins)

def removeFromFavorites(user_id, countryURI):
    data = "<" + BASE_URL + "/user/" + user_id + "> <" + BASE_URL + "/favorite" + "> <" + BASE_URL + "/country/" + countryURI + "> .\n"
    update = """DELETE DATA{""" + data + """}"""
    ins = executeInsert(update)
    if len(ins) != 0:
        print(ins)