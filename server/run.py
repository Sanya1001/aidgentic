

form_data_path = 'server/form_data.csv'

def store_data(form_data: dict):

  form_data['processed'] = False

  with open(form_data_path, 'w') as f:
    # read current data
    existing_data = f.read()

    # append new data
    f.write(form_data)

    # write to file
    f.write(existing_data)


  pass


def invoke():


  return [{
    "org_id": "",
    "suggestions": ""
  }]




