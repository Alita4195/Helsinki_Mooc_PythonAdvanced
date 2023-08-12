# Write your solution here:
class Series:
    def __init__(self, title: str, season_num: int, genres_list: list):
        self.title = title
        self.season_num = season_num
        self.genres = genres_list
        self.rating = []  # Extra list to store ratings
    
    def genre_string(self):
        return ", ".join(self.genres)

    def __str__(self):
        genre_string = self.genre_string()
        if self.rating:
            avg_rating = sum(self.rating) / len(self.rating)
            return f"{self.title} ({self.season_num} seasons)\ngenres: {genre_string}\n{len(self.rating)} ratings, average {avg_rating:.1f} points"
        else:
            return f"{self.title} ({self.season_num} seasons)\ngenres: {genre_string}\nno ratings"

    def rate(self, rating: int):
        self.rating.append(rating)

def minimum_grade(grade: float, series_list: list):
    selected_series = []
    for series in series_list:
        if series.rating:
            avg_rating = sum(series.rating) / len(series.rating)
            if avg_rating >= grade:
                selected_series.append(series)

    return selected_series


def includes_genre(genre: str, series_list: list):
    matching_series = []
    for series in series_list:
        if genre in series.genres:
            matching_series.append(series)

    return matching_series



if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    #print(s1,s2,s3)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)