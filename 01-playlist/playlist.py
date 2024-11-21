from metaflow import FlowSpec, step, IncludeFile, Parameter


def script_path(filename):
    """
    이 튜토리얼의 디렉토리에 있는 파일의 절대 경로를 얻기 위한 함수입니다.
    이를 통해 튜토리얼을 어떤 디렉토리에서든 실행할 수 있습니다. (징짜?)
    """
    import os

    filepath = os.path.join(os.path.dirname(__file__))
    return os.path.join(filepath, filename)


class PlayListFlow(FlowSpec):
    """
    좋아하는 영화 재생 목록을 만드는 데 도움을 주는 플로우입니다.

    이 플로우는 다음 단계를 수행합니다:
    1) 영화에 대한 메타데이터가 포함된 CSV 파일을 가져옵니다.
    2) CSV에서 두 개의 열을 파이썬 리스트로 로드합니다.
    3) 병렬 브랜치에서:
       - A) 장르 매개변수로 영화를 필터링합니다.
       - B) 다른 장르에서 무작위로 영화를 선택합니다.
    4) 재생 목록의 상위 항목을 표시합니다.
    """

    movie_data = IncludeFile(
        "movie_data",
        help="영화 메타데이터 파일의 경로입니다.",
        default=script_path("movies.csv"),
    )

    # 장르를 선택하는 데 사용할 매개변수입니다. 이런게 있을 땐 -genre Comedy 이런식으로 사용할 수 있음
    genre = Parameter(
        "genre", help="특정 장르의 영화를 필터링합니다.", default="Sci-Fi"
    )

    recommendations = Parameter(
        "recommendations",
        help="재생 목록에서 추천할 영화의 수입니다.",
        default=5,
    )

    @step
    def start(self):
        """
        CSV 파일을 파싱하고 값을 리스트의 사전으로 로드합니다.
        """
        # 이 예제에서는 영화 제목과 장르만 필요합니다.
        columns = ["movie_title", "genres"]

        # 리스트의 사전으로 간단한 데이터 프레임을 만듭니다.
        self.dataframe = dict((column, list()) for column in columns)

        # CSV 헤더를 파싱합니다.
        lines = self.movie_data.split("\n")
        header = lines[0].split(",")
        idx = {column: header.index(column) for column in columns}

        # CSV 파일의 줄에서 데이터 프레임을 채웁니다.
        for line in lines[1:]:
            if not line:
                continue

            fields = line.rsplit(",", 4)
            for column in columns:
                self.dataframe[column].append(fields[idx[column]])

        # 병렬로 장르별 영화를 계산하고 보너스 영화를 선택합니다.
        self.next(self.bonus_movie, self.genre_movies)

    @step
    def bonus_movie(self):
        """
        이 단계에서는 다른 장르에서 무작위로 영화를 선택합니다.
        """
        from random import choice

        # 제공된 장르에 속하지 않는 모든 영화를 찾습니다.
        movies = [
            (movie, genres)
            for movie, genres in zip(
                self.dataframe["movie_title"], self.dataframe["genres"]
            )
            if self.genre.lower() not in genres.lower()
        ]

        # 무작위로 하나를 선택합니다.
        self.bonus = choice(movies)

        self.next(self.join)

    @step
    def genre_movies(self):
        """
        장르별로 영화를 필터링합니다.
        """
        from random import shuffle

        # 지정된 장르의 모든 영화 제목을 찾습니다.
        self.movies = [
            movie
            for movie, genres in zip(
                self.dataframe["movie_title"], self.dataframe["genres"]
            )
            if self.genre.lower() in genres.lower()
        ]

        # 제목을 무작위로 섞습니다.
        shuffle(self.movies)

        self.next(self.join)

    @step
    def join(self, inputs):
        """
        병렬 브랜치를 결합하고 결과를 병합합니다.
        """
        # 브랜치에서 관련 변수를 다시 할당합니다.
        self.playlist = inputs.genre_movies.movies
        self.bonus = inputs.bonus_movie.bonus

        self.next(self.end)

    @step
    def end(self):
        """
        재생 목록과 보너스 영화를 출력합니다.
        """
        print("장르 '%s'의 영화 재생 목록" % self.genre)
        for pick, movie in enumerate(self.playlist, start=1):
            print("선택 %d: '%s'" % (pick, movie))
            if pick >= self.recommendations:
                break

        print("보너스 선택: '%s' from '%s'" % (self.bonus[0], self.bonus[1]))


if __name__ == "__main__":
    PlayListFlow()
