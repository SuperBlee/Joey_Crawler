"""
Joey's Crawler

This is the Crawler program for the pdf files and the Abstracts
"""

import openpyxl
import urlparse
import requests

def parseDoi(url):
    req = requests.get(url)
    loc = req.history[-1].headers["Location"]


if __name__ == "__main__":
    xls = openpyxl.load_workbook(filename= "data.xlsx")
    sheet_names_list = xls.get_sheet_names()
    i = 1
    netloc_set = set()
    sheet_names_list = sheet_names_list[1]
    for sheet_name in sheet_names_list:
        sheet = xls.get_sheet_by_name(sheet_name)
        i = 1
        print "Parsing...{}".format(sheet_name)
        while True:
            i += 1
            print "Parsing # {}".format(str(i))
            title_coordinate = 'B' + str(i)
            url_coordinate   = 'G' + str(i)
            if sheet[title_coordinate].value is None:
                break
            title, url = sheet[title_coordinate].value, sheet[url_coordinate].value
            parse_result = urlparse.urlparse(url)
            netloc = parse_result.netloc
            if netloc == "dx.doi.org":
                pass
            else:
                # TODO: Parse the ncbi
                pass


