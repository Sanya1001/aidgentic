from typing import Annotated
from langchain.tools import tool
from typing import List

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
                 'topic': 'Earthquak',
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
            
        }
    }
    return historical_data.get(type.lower(), {}).get(location.upper(), [])
    

def read_database():
    '''
    This tool reads the database.
    '''
    print("Called read_database")
    return [
        {'timestamp': '2025-04-21', 
         'state': 'CA',
         'city': 'San Francisco', 
         'topic': 'Earthquake',
            'severity': 'High',
            'affected_population': '5935',
            'description': 'Earthquake hit residential area in San Jose. Buildings have collapsed and cars are on fire. People are trapped. Need immediate help.',
        },
            
            {'timestamp': '2025-04-21', 
             'state': 'CA',
            'city': 'Los Angeles', 
            'topic': 'Earthquake',
                'severity': 'High',
                'affected_population': '5000',
                'description': 'Earthquake in Sacramento. Roads collapsed into deep holes and buildings collapsed. at least 1 neighborhood is on fire.', 
            }
    ]

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
        "name": "red-cross",
        "region": "us",
        "date": "6-22-2024",
        "resources": "shelter locations, first aid"
    },
    {
        "name": "red-cross",
        "region": "canada",
        "date": "6-22-2024",
        "resources": "shelter locations, first aid"
    },
    {
        "name": "United Nations Children's Fund",
        "region": "world",
        "date": "6-22-2024",
        "resources": "humanitarian assistance"
    },
    {
        "name": "World Food Program",
        "region": "world",
        "date": "6-22-2024",
        "resources": "food"
    },
    {
        "name": "California fire foundation",
        "region": "CA",
        "date": "6-22-2024",
        "resources": "funding"
    },
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