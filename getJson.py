import requests
url = "https://ssip.tool.rcn.cloud/rest/hardware/?format=json"



def get_response(url):
    x=requests.get(url)

    f = str(x.content.decode())
    with open("data.json", "w") as data_file:
        data_file.write(f)
        data_file.close()


get_response(url)