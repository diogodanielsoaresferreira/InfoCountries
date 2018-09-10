from wikidata.client import Client
import requests
from lxml import etree
from app.dbInterface import *
from app.businessLogic import getCountryURIByName

# Queries the wikidata with the REST API with sparql query
def queryWiki(query):
    response = requests.get("https://query.wikidata.org/bigdata/namespace/wdq/sparql?query=" + query)
    response.encoding = 'utf-8'
    content = response.text

    parser = etree.XMLParser(encoding='utf-8')
    root = etree.fromstring(content.encode('utf-8'), parser=parser)

    results = root.findall('.//{http://www.w3.org/2005/sparql-results#}result')
    dict_results = []
    for result in results:
        res = result.findall('{http://www.w3.org/2005/sparql-results#}binding')
        binding = []
        for bind in res:
            if (bind.find('{http://www.w3.org/2005/sparql-results#}uri') != None):
                binding += [{bind.get('name'): bind.find('{http://www.w3.org/2005/sparql-results#}uri').text}]
            elif (bind.find('{http://www.w3.org/2005/sparql-results#}literal') != None):
                binding += [{bind.get('name'): bind.find('{http://www.w3.org/2005/sparql-results#}literal').text}]
        dict_results += [binding]
    return dict_results

# Splits the path from the wikidata entity
def getWikidataEntity(path):
    return path.split("http://www.wikidata.org/entity/")[1]

# Return all countries on wikidata, with it's name and URI, in form (country, countryLabel)
def getAllWikidataCountries():

    query = """
        SELECT ?country ?countryLabel WHERE {
        
            ?country wdt:P31 wd:Q3624078 .
        
            SERVICE wikibase:label {
               bd:serviceParam wikibase:language "en"
            }
        }
    """
    return queryWiki(query)

# Returns the data in form (country, countryLabel) of one country in wikidata
def getWikidataCountry(country_name):
    query="""
        SELECT ?country ?countryLabel WHERE {
            ?country wdt:P31 wd:Q3624078 .
            ?country rdfs:label ?countryLabel .
            FILTER (lang(?countryLabel) = "en")
            filter(regex(?countryLabel,"^"""+country_name+"""$", "i"))
        }
    
    """
    result = queryWiki(query)
    if len(result)>0:
        return result[0]
    return None

# Get the country entity, given a label of the country
def getWikidataCountryEntity(label):
    try:
        wikidataCountry = getWikidataCountry(label)[0]["country"]
    except:
        return None
    client = Client()
    entity = client.get(getWikidataEntity(wikidataCountry))
    return entity

# Returns the url of the image of an entity
def getWikidataImageURL(entity):
    client = Client()
    flag_img_prop = client.get('P41')
    flag_file = entity[flag_img_prop]
    return flag_file.image_url

# Creates new predicates given a country URI and a country wikidata entity
def createCountryNewPredicates(country, countryEntity):

    client = Client()

    newRelations = []
    newValues = []


    for predicate in WIKIDATA_PREDICATES:
        pred = client.get(predicate[1])
        print()
        print(predicate[0])
        print(pred)

        if pred in countryEntity:
            for element in countryEntity.getlist(pred):
                predid = pred.id
                elementid = element.id
                elementlabel = element.label
                print(country, predid, element)
                newRelations += [(country, predid, elementid)]
                print(element.id, nameof, elementlabel)
                newValues += [(elementid, nameof, elementlabel)]

        else:
            print("No data was found")

    data = ""
    for metric in newRelations:
        data += "<"+BASE_URL+"/country/"+metric[0] + "> <" + WIKIDATA_BASEURL+metric[1] + "> <" + WIKIDATA_BASEURL+metric[2] + "> .\n"
    for metric in newValues:
        data += "<" + WIKIDATA_BASEURL + metric[0] + "> <" + nameof + "> \"" + str(metric[2]) + "\" .\n"

    data += "<"+BASE_URL+"/country/"+country + "> <"+BASE_URL+"/hasWikidata>"+" \"True\" .\n"

    update = """INSERT DATA{""" + data + """}"""
    ins = executeInsert(update)
    if len(ins) != 0:
        print(ins)

    return newRelations

# Checks if the country has results updated with wikidata data
def checkCountryHasWikidata(country_id):
    query = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        select ?name
        WHERE{
            ?subject <"""+BASE_URL+"""/hasWikidata> "True" .
            filter(?subject=<""" + BASE_URL+"/country/"+country_id + """>) .
        }
        """
    results = executeQuery(query)
    if len(results["results"]["bindings"])>0:
        return True
    return False

# Creates new relations between countries
def createCountriesRelations(countryURI, countryEntity):

    client = Client()

    newData = ""

    for rel in WIKIDATA_COUNTRY_RELATIONS:
        pred = client.get(rel[1])

        if pred in countryEntity:
            for element in countryEntity.getlist(pred):
                elementlabel = element.label
                print(elementlabel)
                countriesURI = getCountryURIByName(str(elementlabel))
                if(len(countriesURI)==0):
                    print("Could not find country "+str(elementlabel)+" in local database")
                else:
                    country2URI = countriesURI[0]
                    print(country2URI)
                    newData += "<"+BASE_URL+"/country/"+countryURI+"> <" + WIKIDATA_BASEURL+rel[1] +"> <"+country2URI+"> . \n"

    newData += "<" + BASE_URL + "/country/" + countryURI + "> <" + BASE_URL + "/hasRelations>" + " \"True\" .\n"
    print(newData)
    update = """INSERT DATA{""" + newData + """}"""
    ins = executeInsert(update)
    if len(ins) != 0:
        print(ins)

# Checks if the country has relations with other countries updated with wikidata data
def checkCountryHasWikidataRelations(country_id):
    query = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        select ?subject
        WHERE{
            ?subject <"""+BASE_URL+"""/hasRelations> "True" .
            filter(?subject=<""" + BASE_URL+"/country/"+country_id + """>) .
        }
        """
    results = executeQuery(query)
    if len(results["results"]["bindings"])>0:
        return True
    return False