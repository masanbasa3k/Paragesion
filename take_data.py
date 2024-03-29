import requests
from bs4 import BeautifulSoup

def get_paragraph_from_url(url):
    try:
        # Attempt to fetch content from the URL
        response = requests.get(url)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get text content from <p> tags and concatenate them
        paragraphs = soup.find_all('p')
        paragraph_text = '\n'.join([p.get_text() for p in paragraphs])
        
        return paragraph_text
    except Exception as e:
        print(f"An error occurred while fetching content from {url}: {e}")
        return ""

def concatenate_paragraphs_from_urls(urls):
    
    urls = urls.split(",")
    concatenated_paragraphs = ""
    for url in urls:
        # Get paragraph from each URL and concatenate them
        paragraph = get_paragraph_from_url(url)
        if paragraph:
            concatenated_paragraphs += paragraph + "\n\n"  # Add a blank line between paragraphs
    return concatenated_paragraphs


if __name__ == '__main__':
    # Test the function
    result = concatenate_paragraphs_from_urls("https://en.wikipedia.org/wiki/Duck_typing, https://en.wikipedia.org/wiki/Abstract_type")
    print(result)
