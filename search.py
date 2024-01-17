import requests
from bs4 import BeautifulSoup
import resolveurl

def search_ina(query):
    search_url = f"https://ina.myvideolinks.net/?s={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='item')

    # Extract and display search results
    for idx, result in enumerate(results, start=1):
        title = result.find('h2', class_='title').text.strip()
        print(f"{idx}. {title}")

    # Prompt user to choose a result
    choice = int(input("Choose a result (enter the corresponding number): "))
    chosen_result = results[choice - 1]

    # Scrape streamtape.com urls from the chosen result's page
    choices_url = chosen_result.find('a', class_='btn')['href']
    choices_page = requests.get(choices_url)
    choices_soup = BeautifulSoup(choices_page.text, 'html.parser')
    streamtape_urls = [a['href'] for a in choices_soup.find_all('a', href=True, text='Streamtape')]

    # Display streamtape.com choices
    for idx, url in enumerate(streamtape_urls, start=1):
        print(f"{idx}. {url}")

    # Prompt user to choose a streamtape.com url
    streamtape_choice = int(input("Choose a Streamtape.com URL (enter the corresponding number): "))
    chosen_streamtape_url = streamtape_urls[streamtape_choice - 1]

    # Use ResolveURL to resolve and play the chosen streamtape.com url
    hmf = resolveurl.HostedMediaFile(chosen_streamtape_url)
    if hmf:
        resolved_url = hmf.resolve()
        print(f"Resolved URL: {resolved_url}")
    else:
        print("Failed to resolve URL. Please try again.")

# Example usage
if __name__ == "__main__":
    search_query = input("Enter search query: ")
    search_ina(search_query)

