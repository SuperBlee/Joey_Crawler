# Joey's Crawler

Zeyu Li

Mar.1, 2017

**For Joey**

1. Please install BeautifulSoup and other package if needed on server.

2. Please rename the xlsx file to "data.xlsx"

3. Please run "abstract_extract.py". Don't run "jcrawler.py", that is an unsuccessful try.

4. Please do other modifications if needed. I did not consider compatibility, heiheihei.

5. Enjoy!

Zeyu


This is for Joey's project. It's function is as follows:

_1_: Collecting the URLs from an Excel file.

_2_: For some of the URLs, download all the linked pdf files in the page.

_3_: For some of the URLs, download the abstract mentioned on the page.

**Note**:
The `openpyxl` files open files in following manner: it can only fetch the value by the coordinate of the cells
such as `'A1'`, `'A1':'C2'`, etc.

From `A1` to `G1`, the attribute names are
`Author Names`, `Title`, `Journal`, `DOI`, `PMID`, `Year`, `Link`.