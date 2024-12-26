from bs4 import BeautifulSoup
from typing import Set
from enum import Enum


# Configure the path to the HTML files
class FilePath(Enum):
    FOLLOWERS = "followers.html"
    FOLLOWING = "following.html"


def extract_usernames(file_path: str) -> Set[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        usernames = set()
        
        for link in soup.find_all('a', href=True):
            if "instagram.com" in link['href']:
                usernames.add(link.text.strip())                
        return usernames


def main():
    followers = extract_usernames(FilePath.FOLLOWERS.value)
    following = extract_usernames(FilePath.FOLLOWING.value)

    not_following_back = following - followers

    print("Accounts you follow but who don't follow you back:\n")
    print(sorted(not_following_back))


if __name__ == "__main__":
    main()
