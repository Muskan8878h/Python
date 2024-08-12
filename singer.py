from collections import Counter

def count_favorite_singers(num_songs, singers):
    # Count the occurrences of each singer
    singer_counts = Counter(singers)

    # Find the maximum count
    max_count = max(singer_counts.values())

    # Count the number of singers with the maximum count
    num_favorite_singers = sum(count == max_count for count in singer_counts.values())

    return num_favorite_singers

if __name__ == "__main__":
    # Input: Number of songs
    num_songs = int(input())

    # Input: List of singers for each song
    singers = list(map(int, input().split()))

    # Output: Number of favorite singers
    result = count_favorite_singers(num_songs, singers)
    print(result)