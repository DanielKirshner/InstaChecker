from bs4 import BeautifulSoup
from collections import Counter
from rich import print
from enum import Enum


# Configure the path to the HTML files
class FilePath(Enum):
    FOLLOWERS = "followers.html"
    FOLLOWING = "following.html"


def extract_usernames(file_path: str) -> Counter:
    try:
        usernames = Counter()
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            for link in soup.find_all('a', href=True):
                if "instagram.com" in link['href']:
                    usernames[link.text.strip()] += 1
    except FileNotFoundError:
        print(f"[bold red]Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"[bold red]An error occurred while reading '{file_path}': {e}")
    
    return usernames

def main():
    followers: Counter = extract_usernames(FilePath.FOLLOWERS.value)
    following: Counter = extract_usernames(FilePath.FOLLOWING.value)

    if not followers or not following:
        return

    not_following_back: Counter = following - followers

    print("\nAccounts you follow but who don't follow you back:")
    if not_following_back:
        for username in sorted(not_following_back):
            print(f"[bold yellow]{username}")
    else:
        print("[bold green]None! Everyone you follow follows you back.\n")


if __name__ == "__main__":
    main()
