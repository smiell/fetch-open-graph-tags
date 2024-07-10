fetch-open-graph-tags

Description:
This repository contains a Python script that fetches and displays Open Graph meta tags from a specified webpage URL. Open Graph tags are crucial for defining how content is displayed when shared on social media platforms like Facebook, Twitter, and LinkedIn.

Open Graph Protocol
The Open Graph Protocol enables web pages to become rich objects in a social graph. For example, this allows for these pages to have a title, description, and image when they are shared on social media networks or messaged.

Usage
Clone the Repository

sql
Copy code
git clone https://github.com/smiell/fetch-open-graph-tags.git
cd fetch-open-graph-tags
Install Dependencies

Make sure you have Python installed, along with the required libraries:

Copy code
pip install requests beautifulsoup4
Run the Script

Execute the script and provide the --urlToCheck argument with the URL of the webpage you want to inspect:

Copy code
python fetch_open_graph_tags.py --urlToCheck="http://example.com"
Replace "http://example.com" with the actual URL of the webpage you want to check.

About
This script utilizes Python's requests library to fetch the HTML content of a webpage and BeautifulSoup for parsing the HTML to extract Open Graph meta tags. These tags include information such as the title, description, image, and URL of the webpage, which are crucial for optimizing how the webpage appears when shared on social media platforms.

Feel free to contribute, report issues, or suggest improvements to this repository.
