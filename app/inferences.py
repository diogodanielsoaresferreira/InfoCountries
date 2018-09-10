from app.businessLogic import *

# Add inferences to database
def addRelations(relations):
    data = ""
    for relation in relations:
        for subject in relations[relation]:
            for obj in relations[relation][subject]:
                data += "<"+subject+"> <"+relation+"> <"+obj+"> . \n"
    print(data)
    query = """
            PREFIX countries: <""" + BASE_URL + """/countryProperty/>
            INSERT DATA {"""+data+"""}
            """
    ins = executeInsert(query)
    if len(ins) != 0:
        print(ins)

# Returns the reflexice inferences
def getReflexiveInferences():
    relations = {}
    newRelations = {}
    for relation in WIKIDATA_COUNTRY_RELATIONS:
        relations[WIKIDATA_BASEURL+relation[1]] = getAllCountriesByMetric(WIKIDATA_BASEURL+relation[1])

    for relation in relations:
        if relation not in newRelations:
            newRelations[relation] = {}

            for country1 in relations[relation]:
                for country2 in relations[relation][country1]:
                    if country2 not in newRelations[relation]:
                        newRelations[relation][country2] = []

                    newRelations[relation][country2] += [country1]

    return newRelations

# Query to get the best countries to invest
def getBestCountriesToInvest():
    query = """
        PREFIX countries: <""" + BASE_URL + """/countryProperty/>
        select ?countryURI
        WHERE{
            ?countryURI countries:45 ?unemploymentRate .
            ?countryURI countries:26 ?laborForce .
            ?countryURI countries:23 ?investment .
            ?countryURI countries:39 ?publicDebt .
            ?countryURI countries:20 ?inflationRate .
            ?countryURI countries:25 ?lifeExpectancy .
            ?countryURI countries:9 ?exports .
            filter(?unemploymentRate<10.0)
            filter(?laborForce>100000)
            filter(?investment>15.0)
            filter(?publicDebt<175.0)
            filter(?inflationRate<10.0)
            filter(?lifeExpectancy>75.0)
        }
        ORDER BY DESC(?exports)
        """

    results = executeQuery(query)
    predicates = []
    for result in results["results"]["bindings"]:
        predicates += [result["countryURI"]["value"]]
    return predicates

# Query to get the countries with more internet traffic
def getCountriesWithMoreInternetTraffic():
    query = """
            PREFIX countries: <""" + BASE_URL + """/countryProperty/>
            select ?countryURI
            WHERE{
                ?countryURI countries:43 ?mobileCelularUsers .
                ?countryURI countries:42 ?mainLinesInUse .
                ?countryURI countries:21 ?internetHosts .
                filter(?mobileCelularUsers>10000000)
                filter(?mainLinesInUse>10000000)
                filter(?internetHosts>1056950)
            }
            ORDER BY DESC(?internetHosts)
            """

    results = executeQuery(query)
    predicates = []
    for result in results["results"]["bindings"]:
        predicates += [result["countryURI"]["value"]]
    return predicates

# Query to get the best countries to live
def getBestCountriesToLive():
    query = """
            PREFIX countries: <""" + BASE_URL + """/countryProperty/>
            select ?countryURI
            WHERE{
                ?countryURI countries:45 ?unemploymentRate .
                ?countryURI countries:23 ?investment .
                ?countryURI countries:39 ?publicDebt .
                ?countryURI countries:20 ?inflationRate .
                ?countryURI countries:25 ?lifeExpectancy .
                ?countryURI countries:13 ?hiv_adult .
                ?countryURI countries:5 ?death_rate .
                filter(?unemploymentRate<10.0)
                filter(?investment>=15.0)
                filter(?publicDebt<=175.0)
                filter(?inflationRate<=10.0)
                filter(?lifeExpectancy>=75.0)
                filter(?hiv_adult<=0.40)
                filter(?death_rate<=11)
            }
            ORDER BY DESC(?lifeExpectancy)
            """

    results = executeQuery(query)
    predicates = []
    for result in results["results"]["bindings"]:
        predicates += [result["countryURI"]["value"]]
    return predicates