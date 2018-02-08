import requests
import json
from collections import Counter
from argparse import ArgumentParser


status_codes = []

def readInputUrls(filename):
    with open(filename)as file:
        try:
            lines = file.readlines()
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

    print(jsonified_details)

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

    file = open("REPORT----"+site_name+".json","w+")
    file.write(jsom)

def status_codes_report(status_codes):
    statuses_list = []
    status_count = Counter(status_codes)
    unique_status_codes = list(set(status_codes))

    for status in unique_status_codes:
        statuses_list.append(json.dumps({"Status_code": status, "Number_of_responses": status_count[status]}))


    with open("Http-Status-Report.json", "w+") as report_file:
        statuses_list = map(lambda x: x + ',\n', statuses_list)
        report_file.writelines(statuses_list)

    for reported_status in statuses_list:
        print reported_status




if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-file', required=True, metavar='file', type=str, help="File containing list of urls to check")
    param = parser.parse_args()
    urls = readInputUrls(param.file)
    for url in urls:
        response = retrieve_response_details(url)
        write_json_to_file(response[0])
        if len(response)>1:
            status_codes.append(response[1])
    status_codes_report(status_codes)
    print "done"