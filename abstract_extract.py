"""
abstract extractor

This is the Crawler program for the pdf files and the Abstracts
"""

import openpyxl
import urlparse
import requests
import os
from bs4 import BeautifulSoup


if __name__ == "__main__":
    os.chdir("/home/ww8/Dropbox/Research/Joey's Crawler/")
    print os.getcwd()

    # Set the source file
    xls = openpyxl.load_workbook(filename= "./data_1.xlsx")
    sheet_names_list = xls.get_sheet_names()
    # sheet_names_list = sheet_names_list[1]
    for sheet_name in sheet_names_list:
        sheet = xls.get_sheet_by_name(sheet_name)

        # Set row index, index should start from 2, row#1 is column name
        row_index = 1

        print "Parsing from sheet...{sheetname}".format(sheetname = sheet_name)

        while True:
            row_index += 1
            print "   Parsing Row # {}".format(str(row_index))
            title_coordinate = 'B' + str(row_index)
            url_coordinate   = 'G' + str(row_index)
            pmid_coordinate  = 'E' + str(row_index)

            # Exit at the last row
            if sheet[url_coordinate].value is None:
                break

            # Fetch the values of title and url
            title, url, pmid = sheet[title_coordinate].value, \
                               sheet[url_coordinate].value, \
                               sheet[pmid_coordinate].value

            # Classify the url: from 'dx.doi.org' or 'www.ncbi.nlm.nih.gov'
            parse_result = urlparse.urlparse(url)
            netloc = parse_result.netloc

            # In case when the file is under "ncbi", we can fetch abstract text
            print netloc
            if netloc == 'www.ncbi.nlm.nih.gov':
                req = requests.get(url, timeout=2)
                text = req.text
                soup = BeautifulSoup(text, 'lxml')
                try:
                    abstract = str(soup.find_all('abstracttext')[0])[14:-15]
                    with open("./abstracts/"+str(pmid)+".txt", "w") as file:
                        file.write(abstract)
                except:
                    pass
