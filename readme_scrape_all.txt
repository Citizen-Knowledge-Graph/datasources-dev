Scripts Overview

# Run every script with "python3 script_name" in the console.

0_topic_search.py Is meant to scrape all search terms from the API. Still incomplete.
1_save_search_results_to_html_by_keyword.py Use any search term to save the search results from Foerderdatenbank to html files in the html_files folder. 
2_extract_and_save_program_links_from_html.py Scrapes all urls from the result pages of the html_files folder in the main directory and saves to "program_links.json" in main folder.
3_scrape_funding_offer_links.py Scrapes all data and saves the "scraped_data.json" in main folder as a final step.
