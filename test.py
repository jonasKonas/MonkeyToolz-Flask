import json
from ssipResponse import get_response
url = "https://ssip.tool.rcn.cloud/rest/hardware/?format=json"
string = "NET31490-SOGEA-CARTERGATEHOUSE.CE1	R	2033	Cisco C927-4P		PR010667	/tftpboot/customer-conf/31490	Suresh Mogalapu		Billy Fenton		07/11/2022												"

get_response(url)
#Fetch from Json file the correct OS file:
def fetch_data(string_data):

  newList = string_data.split("\t")

  c_item = newList[0]
  part_number = newList[3].split()[-1]
  pick_ref = newList[5]
  aip_dir = newList[6]
  conf_eng = newList[7]
  conf_pm = newList[9]

  # Opening JSON file
  f = open('data.json', 'r')

  #Load Json file
  data = json.load(f)
  for i in range(len(data)):
    if part_number == ((data[i])["part_number"]):
      os_file = (data[i])["standard_software_file"]
      supplier = (data[i])["supplier"]
      return os_file, supplier, c_item, pick_ref, aip_dir, conf_eng, conf_pm

  else:    
    error = "No part code in the database. Check if part code is spelled correctly."
    return error



print(fetch_data(string))