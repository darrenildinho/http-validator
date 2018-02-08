import requests
import json

# r = requests.get("http://www.bbc.co.uk/iplayer")
# t = requests.head("http://www.bbc.co.uk/iplayer")
#
# print(r.status_code)
#
# # print r.headers['Content-length']
# print(t.headers)



status_codes = []

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
    try:
        response = requests.head(url, timeout=10)
        status_code = response.status_code
        date = response.headers['Date']
        content_length = response.headers["Content-Length"]
    except Exception as e:
        details = {"URL": url, "Message": "invalid url"}
        jsonified_details = json.dumps(details, indent=4)
        response = [jsonified_details]
        return response

    details = {"URL": url, "Status_code": status_code, "Content_length": content_length, "Date": date}

    jsonified_details = json.dumps(details, indent=4)

    response = [jsonified_details, status_code]

    return response

def write_json_to_file(jsom):
    json_data = json.loads(jsom)
    url = json_data['URL']
    site = url.split("//")[1]
    if "www." in site:
        site_name = site.split(".")[1]
    else:
        site_name = site.split(".")[0]
    # file = open("llamas.txt", "w+")
    file = open("REPORT----"+site_name+".txt","w+")
    # with open("site-"+site+"---Response-details.txt","w") as file:
    file.write(jsom)

def status_codes_report(status_codes):


if __name__ == '__main__':
    urls = readInputUrls("urls")
    json_details = []
    for url in urls:
        response = retrieve_response_details(url)
        write_json_to_file(response[0])
        if len(response)>1:
            status_codes.append(response[1])

    print "done"