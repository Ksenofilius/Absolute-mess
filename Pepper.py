import requests
from bs4 import BeautifulSoup
import re

def search_pepper(keyword, max_results=10):
    # URL with search
    url = f"https://www.pepper.pl/search?q={keyword}"
    
    # Headers to simulate a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Get the page
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # HTML parsing
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all active offers
        threads = soup.find_all('article', class_='thread')
        
        results = []
        for thread in threads:
            # Check if an offer expired
            expired = thread.find('span', class_='cept-show-expired-thread')
            if not expired:
                title_element = thread.find('a', class_='cept-tt')
                if title_element:
                    title = title_element.text.strip()
                    link = 'https://www.pepper.pl' + title_element['href']
                    results.append({'title': title, 'link': link})
                    
                    if len(results) >= max_results:
                        break
        
        return results
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Use the script
if __name__ == "__main__":
    from datetime import datetime
    
    print("Welcome to the Pepper.pl search tool!")
    keyword = input("Enter what you're looking for (e.g. headphones, laptop, phone): ")
    max_results = input("How many results would you like to see? (default: 10): ")
    
    # Check if user provided number of searches
    try:
        max_results = int(max_results)
    except ValueError:
        max_results = 10
    
    print(f"\nSearching for offers: {keyword}...")
    results = search_pepper(keyword, max_results)
    
    # Set a static filename
    filename = "pepper_results.txt"
    
    # Save results in a file
    with open(filename, 'w', encoding='utf-8') as f:
        # Save date and time
        f.write(f"Date of search: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Results for: {keyword}\n")
        f.write("-" * 50 + "\n\n")
        
        if results:
            for i, result in enumerate(results, 1):
                f.write(f"{i}. {result['title']}\n")
                f.write(f"   Link: {result['link']}\n\n")
        else:
            f.write("Did not find any active offers.\n")
        
        f.write("\n" + "-" * 40)  # Divider
    
    # Show results from console
    print(f"\nFound offers for: {keyword}")
    print("-" * 50)
    
    if results:
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['title']}")
            print(f"   Link: {result['link']}")
            print()
    else:
        print("Did not find any active offers.")
    
    print(f"\nResults saved to: {filename}")
    input("\nPress Enter to exit...")
