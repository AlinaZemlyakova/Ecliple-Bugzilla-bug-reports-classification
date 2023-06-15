import pandas as pd
import csv, requests, time
from bs4 import BeautifulSoup
import multiprocessing

# scraping useful data from bug pages in a loop
def scrape_bug_data(bug_number):

    bug_url = f"https://bugs.eclipse.org/bugs/show_bug.cgi?id={bug_number}"
    while True:
        try:
            page = requests.get(bug_url)
            if page.status_code == 200:
                break
            else:
                return None
        except:
            time.sleep(5)
            continue

    soup = BeautifulSoup(page.content, "html.parser")
    title_element = soup.find(id="short_desc_nonedit_display")
    title = title_element.text.strip() if title_element else ""

    product_element = soup.find("td", attrs={"class": "field_value"}, id="field_container_product")
    product = product_element.text.strip() if product_element else ""

    component_element = soup.find("td", id="field_container_component")
    component = component_element.get_text(strip=True).split()[0] if component_element else ""

    votes_container = soup.find("span", id="votes_container")
    importance = votes_container.find_previous_sibling(text=True).strip() if votes_container else None

    description_element = soup.find("pre", attrs={"class": "bz_comment_text"})
    description = description_element.text.strip() if description_element else ""

    return [bug_number, bug_url, title, product, component, importance, description]

# functions for splitting data into separate files
# a preventive measure to avoid the loss of all collected data 
def scrape_bugs(start_bug_number, end_bug_number, bugs_in_one_file):
    bugs_data = []
    for bug_number in range(start_bug_number, end_bug_number + 1):
        print(f"Scraping bug number: {bug_number}")
        bug_data = scrape_bug_data(bug_number)
        if bug_data:
            bugs_data.append(bug_data)
        if len(bugs_data) == bugs_in_one_file:
            filename = f"bug_data_{start_bug_number}.csv"
            print("writing to file: {}".format(filename))
            write_to_csv(bugs_data, filename)
            bugs_data = []
    return bugs_data

def write_to_csv(data, csv_filename):
    with open(csv_filename, "w+", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["Bug Number", "Link", "Title", "Product", "Component", "Importance", "Description"]
        )
        writer.writerows(data)
        csvfile.close()

def main():
	start_bug_number = 1
	end_bug_number = 585000
	bugs_in_one_file = 10000
	num_processes = multiprocessing.cpu_count()

	pool = multiprocessing.Pool(processes=num_processes)
	results = []

	while start_bug_number <= end_bug_number:
       result = pool.apply_async(scrape_bugs, (start_bug_number, start_bug_number + bugs_in_one_file - 1,
                                                bugs_in_one_file))
       results.append(result)
	   start_bug_number += bugs_in_one_file

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()