import requests
import json

# r = requests.get("http://www.bbc.co.uk/iplayer")
# t = requests.head("http://www.bbc.co.uk/iplayer")
#
# print(r.status_code)
#
# # print r.headers['Content-length']
# print(t.headers)

def readInputUrls(filename):
    with open(filename)as file:
        try:
            # read the lines from file into variable
            lines = file.readlines()
            #remove any special characters eg \n
            lines = [x.strip() for x in lines]
        except IOError as e:
            print ("Problem reading lines from file"+ e)
        return lines


def retrieve_response_details(url):
    response = requests.head(url)
    status_code = response.status_code
    date = response.headers['Date']
    content_length = response.headers["Content-Length"]

    details = {"URL": url, "Status_code": status_code, "Content_length": content_length, "Date": date}

    jsonified_details = json.dumps(details)

    return jsonified_details

def write_json_to_file(jsom):
    json_data = json.loads(jsom)
    url = json_data['URL']
    site = url.split("//")[1]
    site_name = site.split(".")[0]
    # file = open("llamas.txt", "w+")
    file = open("REPORT----"+site_name+".txt","w+")
    # with open("site-"+site+"---Response-details.txt","w") as file:
    file.write(jsom)


if __name__ == '__main__':
    urls = readInputUrls("urls")
    json_details = []
    for url in urls:
        json_details = retrieve_response_details(url)
        write_json_to_file(json_details)
