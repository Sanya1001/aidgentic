from typing import Annotated
from langchain.tools import tool
from typing import List
import json

DB_PATH= './data/submissions.json'
@tool
def search_disaster_knowledge_base(
        type: Annotated[str, "The type of disaster to search for. (e.g. earthquake, wildfire)"],
        location: Annotated[str, "The state acronym of the location to search for. (e.g. CA, NY)"],
) -> List[dict]:
    '''
    This tool searches the knowledge base for resource requirements for a given disaster type.
    '''
    print("called search_disaster_knowledge_base with disaster_info:", type, location)
    historical_data = {
        'earthquake': {
            'CA': [
                {'timestamp': '2024-06-21', 
                 'city': 'San Francisco', 
                 'topic': 'Earthquake',
                    'severity': 'High',
                    'affected_population': '10000',
                    'description': 'Earthquake in downtown San Francisco. Buildings have collapsed. People are trapped. Need immediate help.',
                 'resources': {
                     'firefighters': 100,
                     'medical_staff': 250,
                     'rescue_workers': 200,
                     'food': '$46,640',
                     'water': '$22,040',
                     'shelter': '$1,130,594',
                 }
                },
                {'timestamp': '2024-06-21', 
                 'city': 'Los Angeles', 
                 'topic': 'Earthquake',
                    'severity': 'High',
                    'affected_population': '5000',
                    'description': 'Earthquake in Los Angeles. People are stranded. Need immediate help.',
                'resources': {
                    'firefighters': 50,
                    'medical_staff': 100,
                    'rescue_workers': 100,
                    'food': '$23,320',
                    'water': '$11,020',
                    'shelter': '$565,297',
                    },
                }
            ]
        },
        'wildfire': {
            "california": [
                {
                    "people affected": 22000,
                    "date": 8-19-2021,
                    "personnel": 5120,
                    "daily_cost": 171,
                    "description": "The fire destroyed 1,005 structures and damaged 81 more, primarily in the US Highway 50 corridor and in the community of Grizzly Flats, 2/3 of which was destroyed by the fire.",
                    "food": "",
                    "water": "",
                    "shelter": "",
                },
                {
                    "people affected": 9500,
                    "date": 7-13-2021,
                    "personnel": 4000,
                    "daily_cost": 171,
                    "description": "",
                    "food": "",
                    "water": "",
                    "shelter": "",
                },
                {
                    "people affected": "30000",
                    "date": 10-11-2017,
                    "personnel": 2000,
                    "cost": 1300,
                    "description": "",
                    "food": "",
                    "water": "",
                    "shelter": "",
                }
            ]
        }
    }
    return historical_data.get(type.lower(), {}).get(location.upper(), [])
    

def read_database():
    '''
    This tool reads the database.
    '''
    print("Called read_database")
    with open(DB_PATH, 'r') as f:
        all_reports = json.load(f)
    #print(all_reports)
    reports_list = [report for report in all_reports if not report['read']]
    assert len(reports_list) > 0, "No new reports found"
    return reports_list
    

#@tool
def get_ngos_for_region(
    #region: Annotated[str, "The acronym of the state to search for NGOs. (e.g. CA, NY)"],
    region: str
) -> List[dict]:
    '''
    This tool returns a list of NGOs which cover the given region.
    '''
    print("Called get_ngos_for_region with region:", region)
    all_ngos = [
        {
            "name": "Red Cross US",
            "region": "us",
            "date": "6-22-2024",
            'description': 'provides emergency assistance, disaster relief, and disaster preparedness education in the United States',
            "resources": "shelter, first aid, food"
        },
        {
            "name": "United Nations Children's Fund",
            "region": "world",
            "date": "6-22-2024",
            "resources": "medical equipment, sanitation kits, temporary learning spaces, health services, including identifying and treating malnourished children and dispatching mobile health teams"
        },
        {
            "name": "World Food Program",
            "region": "world",
            "date": "6-22-2024",
            "resources": "food"
        },
        {
            "name": "California Fire Foundation",
            "region": "CA",
            "date": "6-22-2024",
            "resources": "funding support to survivors of large-scale disasters in California"
        },
        {
            'name': 'ShelterBox',
            'region': 'world',
            'date': '6-22-2024',
            'resources': 'emergency shelter, tools, and other essential items to people who have lost their homes as a result of disaster or conflict'
        },
        {
            'name': 'Florida Humane Society',
            'region': 'FL',
            'date': '6-22-2024',
            'resources': 'pet food, shelter, and medical care for pets in Florida'
        }
    ]
    return all_ngos

def ngo_output_to_list(output: str):
    '''
    This tool converts the output of the NGO router into a human-readable message.
    '''
    output_items = output.split(', ')
    ngos = []
    for i, item in enumerate(output_items):
        if ':' not in item and ngos:
            item = ngos[-1]['resources'] + ', ' + item
            ngos[-1]['resources'] = item
            continue
    
        key, val = item.split(': ')
        if key == 'name':
            ngos.append({key: val})
        else:
            ngos[-1][key] = val
    return ngos