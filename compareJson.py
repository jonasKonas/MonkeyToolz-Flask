import json

def get_info(full_part_code):
    partCode = ((full_part_code).split()[-1]).upper()
    print(partCode)
    
    # Opening JSON file
    f = open('data.json', 'r')
    #Load Json file
    data = json.load(f)
    for i in range(len(data)):
        if partCode == ((data[i])["part_number"]).upper():
            os_file = (data[i])["standard_software_file"]
            supplier = (data[i])["supplier"]
            part_number = (data[i])["part_number"]
            
            return os_file, supplier, part_number

    else:    
        error = "No part code in the database. Check if part code is spelled correctly."
        return error

#print(get_os("Cisco c927-4"))