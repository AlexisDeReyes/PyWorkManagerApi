#!/usr/bin/env python3

"""Retrieves and prints words from a url

Usage:

    python modularity.py <URL>
"""

from urllib.request import urlopen
import sys


def fetch_words(url):
    """Fetches a list of words from a url

    Arguments:
        url {string} -- url you wish to retrieve words from

    Returns:
        list -- list of words decoded into string format
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_words(story_words):
    """Prints a list of words

    Arguments:
        story_words {list} -- list of words you wish to print
    """
    for words in story_words:
        print(words)


def main(url):
    """Main method, fetches words and prints them from a specific url

    Arguments:
        url {string} -- url you wish to print words from
    """
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    # argv[0] is the filename so we'll use the first one
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('http://sixty-north.com/c/t.txt')
