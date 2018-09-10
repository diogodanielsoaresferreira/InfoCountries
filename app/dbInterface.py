"""

Create and insert dataset into the graphdb database

"""

import requests
import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient
from lxml import etree
from django.conf import settings

# Graphdb settings
ENDPOINT = "http://localhost:7200"
REPO_NAME = "countries"

# URI of known entities
BASE_URL = "http://www.ua.pt/ensino/uc/2380/projeto2"
WIKIDATA_BASEURL = "http://www.wikidata.org/wiki/"
nameof = "http://xmlns.com/foaf/0.1/name"

# Metrics used on the local data and his labels
METRICS = [
    ("Country", "<"+BASE_URL+"/countryProperty/1>"),
    ("Area(sq km)", "<"+BASE_URL+"/countryProperty/2>"),
    ("Birth rate(births/1000 population)", "<"+BASE_URL+"/countryProperty/3>"),
    ("Current account balance", "<"+BASE_URL+"/countryProperty/4>"),
    ("Death rate(deaths/1000 population)", "<"+BASE_URL+"/countryProperty/5>"),
    ("Debt - external", "<"+BASE_URL+"/countryProperty/6>"),
    ("Electricity - consumption(kWh)", "<"+BASE_URL+"/countryProperty/7>"),
    ("Electricity - production(kWh)", "<"+BASE_URL+"/countryProperty/8>"),
    ("Exports", "<"+BASE_URL+"/countryProperty/9>"),
    ("GDP", "<"+BASE_URL+"/countryProperty/10>"),
    ("GDP - per capita", "<"+BASE_URL+"/countryProperty/11>"),
    ("GDP - real growth rate(%)", "<"+BASE_URL+"/countryProperty/12>"),
    ("HIV/AIDS - adult prevalence rate(%)", "<"+BASE_URL+"/countryProperty/13>"),
    ("HIV/AIDS - deaths", "<"+BASE_URL+"/countryProperty/14>"),
    ("HIV/AIDS - people living with HIV/AIDS", "<"+BASE_URL+"/countryProperty/15>"),
    ("Highways(km)", "<"+BASE_URL+"/countryProperty/16>"),
    ("Imports", "<"+BASE_URL+"/countryProperty/17>"),
    ("Industrial production growth rate(%)", "<"+BASE_URL+"/countryProperty/18>"),
    ("Infant mortality rate(deaths/1000 live births)", "<"+BASE_URL+"/countryProperty/19>"),
    ("Inflation rate (consumer prices)(%)", "<"+BASE_URL+"/countryProperty/20>"),
    ("Internet hosts", "<"+BASE_URL+"/countryProperty/21>"),
    ("Internet users", "<"+BASE_URL+"/countryProperty/22>"),
    ("Investment (gross fixed)(% of GDP)", "<"+BASE_URL+"/countryProperty/23>"),
    ("Labor force", "<"+BASE_URL+"/countryProperty/24>"),
    ("Life expectancy at birth(years)", "<"+BASE_URL+"/countryProperty/25>"),
    ("Military expenditures - dollar figure", "<"+BASE_URL+"/countryProperty/26>"),
    ("Military expenditures - percent of GDP(%)", "<"+BASE_URL+"/countryProperty/27>"),
    ("Natural gas - consumption(cu m)", "<"+BASE_URL+"/countryProperty/28>"),
    ("Natural gas - exports(cu m)", "<"+BASE_URL+"/countryProperty/29>"),
    ("Natural gas - imports(cu m)", "<"+BASE_URL+"/countryProperty/30>"),
    ("Natural gas - production(cu m)", "<"+BASE_URL+"/countryProperty/31>"),
    ("Natural gas - proved reserves(cu m)", "<"+BASE_URL+"/countryProperty/32>"),
    ("Oil - consumption(bbl/day)", "<"+BASE_URL+"/countryProperty/33>"),
    ("Oil - exports(bbl/day)", "<"+BASE_URL+"/countryProperty/34>"),
    ("Oil - imports(bbl/day)", "<"+BASE_URL+"/countryProperty/35>"),
    ("Oil - production(bbl/day)", "<"+BASE_URL+"/countryProperty/36>"),
    ("Oil - proved reserves(bbl)", "<"+BASE_URL+"/countryProperty/37>"),
    ("Population", "<"+BASE_URL+"/countryProperty/38>"),
    ("Public debt(% of GDP)", "<"+BASE_URL+"/countryProperty/39>"),
    ("Railways(km)", "<"+BASE_URL+"/countryProperty/40>"),
    ("Reserves of foreign exchange & gold", "<"+BASE_URL+"/countryProperty/41>"),
    ("Telephones - main lines in use", "<"+BASE_URL+"/countryProperty/42>"),
    ("Telephones - mobile cellular", "<"+BASE_URL+"/countryProperty/43>"),
    ("Total fertility rate(children born/woman)", "<"+BASE_URL+"/countryProperty/44>"),
    ("Unemployment rate(%)", "<"+BASE_URL+"/countryProperty/45>")
    ]

# Predicates gathered from wikidata
WIKIDATA_PREDICATES = [
    ('Head of government', 'P6'),
    ('Officcial language', 'P37'),
    ('Anthem', 'P85'),
    ('Continent','P30'),
    ('Capital', 'P36'),
    ('Highest Point', 'P610'),
    ('Head of State', 'P35'),
    ('Head of Government', 'P6'),
    ('Member of', 'P463'),
    ('Currency', 'P38'),
    ('Top level internet domain', 'P78')
]

# Relations between countries gathered from wikidata
WIKIDATA_COUNTRY_RELATIONS = [
    ('Shares border', 'P47'),
    ('Diplomatic Relation', 'P530')
]



# Execute query
def executeQuery(query):
    client = ApiClient(endpoint=ENDPOINT)
    accessor = GraphDBApi(client)
    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query, repo_name=REPO_NAME)
    try:
        return json.loads(res)
    except Exception as e:
        print(res)
        return None

# Insert data on the database
def executeInsert(update):
    client = ApiClient(endpoint=ENDPOINT)
    accessor = GraphDBApi(client)
    payload_update = {"update": update}
    res = accessor.sparql_update(body=payload_update, repo_name=REPO_NAME)
    return res

# Inserts the predicates used for graphdb in the database, with its name
# Insert also the predicates gathered on wikidata
def createPredicates():
    data = ""
    for metric in METRICS:
        data += metric[1]+" <"+nameof+"> \""+metric[0]+"\" .\n"
    for metric in WIKIDATA_PREDICATES+WIKIDATA_COUNTRY_RELATIONS:
        data += "<"+WIKIDATA_BASEURL+metric[1]+"> <"+nameof+">"+"\""+metric[0]+"\" .\n"
    update = """INSERT DATA{""" + data + """}"""
    ins = executeInsert(update)
    if len(ins) != 0:
        print(ins)

# Creates a countries repository if it does not exist and populates it with countries' RDF data
def setupRepository():
    print("Setting up the repository")
    # Check if repository exists
    # if it already exists do nothing
    if repoExists():
        return False

    # Create repository
    createRepository()
    
    # Transform xml into RDF
    # and store in 'countries.nt'
    parseXMLtoRDF()

    # Populate newly created repository with RDF data
    importRDF()

    # Create predicates
    createPredicates()

    return True

# Check if the countries repository already exists
def repoExists():
    headers = {
        'Accept': 'application/json',
    }
    response = requests.get('http://localhost:7200/rest/repositories', headers=headers)
    repositories = json.loads(response.text)

    for repo in repositories:
        if 'countries' == repo['id']:
            return True
    return False

# Creates the countries repository
def createRepository():
    files = {
        'config': ('countries-config.ttl', open('app/helper_files/countries-config.ttl', 'rb')),
    }
    params = {
        'type': 'form-data'
    }

    res = requests.post('http://localhost:7200/rest/repositories', files=files, params=params)

# Convert XML countries data to RDF NT
def parseXMLtoRDF():
    # Get xslt transform and xml file
    try:
        xslt_file = etree.parse(settings.XML_FILES + 'countries_transform.xslt')
    except:
        raise FileNotFoundError('Could not find the countries tranform')

    # Create transform
    transform = etree.XSLT(xslt_file)

    # Get countries xml
    countries_tree = etree.parse(settings.XML_FILES + 'countries_data.xml')

    # Apply transform
    res = transform(countries_tree)
    res.write_output("app/nt_files/countries.nt")    

# Import new countries RDF data into the countries repository
def importRDF():
    data = ""

    with open('app/nt_files/countries.nt') as countries_nt:
        triples = countries_nt.readlines()
        for triple in triples:
            data += triple

    # Perform the insertion
    update = """INSERT DATA{"""+data+"""}"""
    ins = executeInsert(update)

    # If insert returns anything, there is an error
    if len(ins)>0:
        print(ins)

print("Setup Repository: " + str(setupRepository()))