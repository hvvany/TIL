# Review Project 2

#python #api #project #codereview



1. ## API문서와 requests 연습

   - 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
   - https://apidocs.bithumb.com/reference/현재가-정보-조회

   > 결과 예시

   ```python
   29812000
   ```

   > 내 코드

   ```python
   import requests
   
   
   def get_btc_krw():
       order_currency = "BTC"
       payment_currency = "KRW"
       url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"
   
       res = requests.get(url=url).json()
       data = res["data"]
       prev_closing_price = data["prev_closing_price"]
   
       return prev_closing_price
   
   
   if __name__ == "__main__":
       print(get_btc_krw())
   ```

   

2. ## 인기 영화 조회

   - 인기 영화 목록의 개수를 출력합니다.
   - requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
   - 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.

   > 결과 예시

   ```json
   20
   ```

   > 내가 작성한 코드

   ```python
   import requests
   
   
   def popular_count():
       pass 
       # 여기에 코드를 작성합니다.  
       base_url = 'https://api.themoviedb.org/3'
       path = '/movie/popular'
       params = {
           'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
           'language': 'ko-KR'
       }
       response = requests.get(base_url+path, params=params).json()
       results = response['results']
   
       return len(results)
   
   
       #아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       popular 영화목록의 개수 반환
       """   
       print(popular_count())
       #20
   ```

   

   > 전공자 작성 코드

   ```python
   import requests
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   API_KEY_TOKEN = os.getenv('my_api_key')
   
   def popular_count():
       pass 
       # 여기에 코드를 작성합니다.
       BASE_URL = 'https://api.themoviedb.org/3'
       path = '/movie/popular'
       params = {
           'api_key': API_KEY_TOKEN,
           'language': 'ko-KR'
       }
   
       response = requests.get(BASE_URL+path, params=params).json()
       result = response.get('results')
       return len(result)
   
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       popular 영화목록의 개수 반환
       """
       print(popular_count())
       # 20
   ```

   > 코드 리뷰

   - .env파일을 활용하였다. 나도 다음 블로그 내용으로 .env에 대해서 공부해봐야겠다.

   

   
   
3. ## 특정 조건에 맞는 인기 영화 조회

   - 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.
   - requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
   - 응답 받은 데이터 중 평점(`vote_average`)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성합니다.

   > 결과 예시

   ```json
   [
       {
           "adult": false,
           "backdrop_path": "/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg",
           "genre_ids": [
               28,
               18
           ],
           "id": 361743,
           "original_language": "en",
           "original_title": "Top Gun: Maverick",
           "overview": "최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…",
           "popularity": 8058.252,
           "poster_path": "/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg",
           "release_date": "2022-05-24",
           "title": "탑건: 매버릭",
           "video": false,
           "vote_average": 8.4,
           "vote_count": 1620
       },
       {
           "adult": false,
           "backdrop_path": "/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg",
           "genre_ids": [
               28,
               12,
               878
           ],
           "id": 634649,
           "original_language": "en",
           "original_title": "Spider-Man: No Way Home",
           "overview": "미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 사상 최악의 위기를 맞게 되는데…",
           "popularity": 1513.591,
           "poster_path": "/voddFVdjUoAtfoZZp2RUmuZILDI.jpg",
           "release_date": "2021-12-15",
           "title": "스파이더맨: 노 웨이 홈",
           "video": false,
           "vote_average": 8.1,
           "vote_count": 14255
       }
   ]
   ```

   > 내가 작성한 코드

   ```python
   import requests
   from pprint import pprint
   
   
   def ranking():
       pass 
       # 여기에 코드를 작성합니다.  
       base_url = 'https://api.themoviedb.org/3'
       path = '/movie/popular'
       params = {
           'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
           'language': 'ko-KR'
       }
       response = requests.get(base_url+path, params=params).json()
       high_vote_lst = []
       mv_lst = []
       results = response['results']
       for mv in results:
         high_vote_lst.append(mv['vote_average'])
       for score in sorted(high_vote_lst)[-1:-5:-1]:
         for i in range(len(results)):
           if len(mv_lst) == 5:
             break
           if results[i]['vote_average'] == score:
             mv_lst.append(results[i])
           
       return mv_lst
   
   
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
       (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
       """
       pprint(ranking())
       
       """
       [{'adult': False,
         'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
         'genre_ids': [28, 18],
         'id': 361743,
         'original_language': 'en',
         'original_title': 'Top Gun: Maverick',
         'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                     '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                     '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                     '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
         'popularity': 911.817,
         'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
         'release_date': '2022-06-22',
         'title': '탑건: 매버릭',
         'video': False,
         'vote_average': 8.4,
         'vote_count': 1463},
       ..생략..,
       }]
       """
   ```

   > 전공자 작성 코드

   ```python
   import requests
   from pprint import pprint
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   API_KEY_TOKEN = os.getenv('my_api_key')
   
   
   def vote_average_movies():
       pass 
       # 여기에 코드를 작성합니다.
       BASE_URL = 'https://api.themoviedb.org/3'
       path = '/movie/popular'
       params = {
           'api_key': API_KEY_TOKEN,
           'language': 'ko-KR'
       }
   
       response = requests.get(BASE_URL+path, params=params).json()
       result = response.get('results')
       new_res = []
       for res in result:
         if res.get('vote_average') >= 8.0:
           new_res.append(res)
       
       return new_res
   
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       popular 영화목록중 vote_average가 8 이상인 영화목록 반환
       (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
       """
       pprint(vote_average_movies())
       """
       [{'adult': False,
         'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
         'genre_ids': [28, 12, 878],
         'id': 634649,
         'original_language': 'en',
         'original_title': 'Spider-Man: No Way Home',
         'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                     '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                     '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                     '사상 최악의 위기를 맞게 되는데…',
         'popularity': 1842.592,
         'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
         'release_date': '2021-12-15',
         'title': '스파이더맨: 노 웨이 홈',
         'video': False,
         'vote_average': 8.1,
         'vote_count': 13954},
       ..생략..,
       }]
       """
   ```

   > 코드 리뷰

   - 거의 같다! 주소를 불러와서 API를 사용하는 방법 이외에 코드 구현은 크게 복잡하지 않아서 나와 비슷하다.

   

   

   

4. ## 특정 조건에 맞는 인기 영화 조회

   - 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.
   - requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
   - 응답 받은 데이터 중 평점(`vote_average`)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성합니다.

   > 결과 예시

   ```json
   [
       {
           "adult": false,
           "backdrop_path": "/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg",
           "genre_ids": [
               28,
               18
           ],
           "id": 361743,
           "original_language": "en",
           "original_title": "Top Gun: Maverick",
           "overview": "최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…",
           "popularity": 8058.252,
           "poster_path": "/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg",
           "release_date": "2022-05-24",
           "title": "탑건: 매버릭",
           "video": false,
           "vote_average": 8.4,
           "vote_count": 1620
       },
       {
           "adult": false,
           "backdrop_path": "/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg",
           "genre_ids": [
               28,
               12,
               878
           ],
           "id": 634649,
           "original_language": "en",
           "original_title": "Spider-Man: No Way Home",
           "overview": "미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 사상 최악의 위기를 맞게 되는데…",
           "popularity": 1513.591,
           "poster_path": "/voddFVdjUoAtfoZZp2RUmuZILDI.jpg",
           "release_date": "2021-12-15",
           "title": "스파이더맨: 노 웨이 홈",
           "video": false,
           "vote_average": 8.1,
           "vote_count": 14255
       }
   ]
   ```

   > 내가 작성한 코드

   ```python
   import requests
   from pprint import pprint
   
   
   def vote_average_movies():
       pass 
       # 여기에 코드를 작성합니다.  
       base_url = 'https://api.themoviedb.org/3'
       path = '/movie/popular'
       params = {
           'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
           'language': 'ko-KR'
       }
       response = requests.get(base_url+path, params=params).json()
       high_vote_lst = []
       results = response['results']
       for mv in results:
         if mv['vote_average'] >= 8:
           high_vote_lst.append(mv)
   
       return high_vote_lst
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       popular 영화목록중 vote_average가 8 이상인 영화목록 반환
       (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
       """
       pprint(vote_average_movies())
       """
       [{'adult': False,
         'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
         'genre_ids': [28, 12, 878],
         'id': 634649,
         'original_language': 'en',
         'original_title': 'Spider-Man: No Way Home',
         'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                     '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                     '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                     '사상 최악의 위기를 맞게 되는데…',
         'popularity': 1842.592,
         'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
         'release_date': '2021-12-15',
         'title': '스파이더맨: 노 웨이 홈',
         'video': False,
         'vote_average': 8.1,
         'vote_count': 13954},
       ..생략..,
       }]
       """
   ```

   > 전공자 작성 코드

   ```python
   import requests
   from pprint import pprint
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   API_KEY_TOKEN = os.getenv('my_api_key')
   
   
   def vote_average_movies():
       pass 
       # 여기에 코드를 작성합니다.
       BASE_URL = 'https://api.themoviedb.org/3'
       path = '/movie/popular'
       params = {
           'api_key': API_KEY_TOKEN,
           'language': 'ko-KR'
       }
   
       response = requests.get(BASE_URL+path, params=params).json()
       result = response.get('results')
       new_res = []
       for res in result:
         if res.get('vote_average') >= 8.0:
           new_res.append(res)
       
       return new_res
   
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       popular 영화목록중 vote_average가 8 이상인 영화목록 반환
       (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
       """
       pprint(vote_average_movies())
       """
       [{'adult': False,
         'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
         'genre_ids': [28, 12, 878],
         'id': 634649,
         'original_language': 'en',
         'original_title': 'Spider-Man: No Way Home',
         'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                     '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                     '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                     '사상 최악의 위기를 맞게 되는데…',
         'popularity': 1842.592,
         'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
         'release_date': '2021-12-15',
         'title': '스파이더맨: 노 웨이 홈',
         'video': False,
         'vote_average': 8.1,
         'vote_count': 13954},
       ..생략..,
       }]
       """
   ```

   > 코드 리뷰

   - 거의 같다! 주소를 불러와서 API를 사용하는 방법 이외에 코드 구현은 크게 복잡하지 않아서 나와 비슷하다.

   

5. ## 영화 조회 및 추천 영화 조회

   - 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
   - requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
   - 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
   - 추천 영화 목록을 리스트로 반환하는 함수를 작성합니다.

   > 결과 예시

   ```json
   ["조커", "1917", "조조 래빗", "원스 어폰 어 타임 인… 할리우드", "... 생략" ,"펄프픽션"]
   ```

   > 내가 작성한 코드

   ```python
   import requests
   from pprint import pprint
   
   
   def recommendation(title):
       # 여기에 코드를 작성합니다.  
       base_url = 'https://api.themoviedb.org/3'
       path = '/search/movie'
       params = {
           'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
           'language': 'ko-KR',
           'query': title
       }
       response = requests.get(base_url+path, params=params).json()
       if len(response['results']) < 1:
           return None
       mv_id = response['results'][0]['id']
   
       base_url_2 = 'https://api.themoviedb.org/3'
       path_2 = f'/movie/{mv_id}/recommendations'
       params_2 = {
           'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
           'language': 'ko-KR'
       }
       response_2 = requests.get(base_url_2+path_2, params=params_2).json()
       results_2 = response_2['results']
       title_lst = []
       for i in range(len(results_2)):
           title_lst.append(results_2[i]['title'])
       return title_lst
   
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
       추천 영화가 없을 경우 []를 반환
       영화 id 검색에 실패할 경우 None을 반환
       (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
       """
       pprint(recommendation('기생충'))
       # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
       pprint(recommendation('그래비티'))
       # []
       pprint(recommendation('검색할 수 없는 영화'))
       # None
   ```

   > 전공자 작성 코드

   ```python
   import requests
   from pprint import pprint
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   API_KEY_TOKEN = os.getenv('my_api_key')
   
   def recommendation(title):
       pass 
       # 여기에 코드를 작성합니다.
       BASE_URL = 'https://api.themoviedb.org/3'
       path = '/search/movie'
       params = {
           'api_key': API_KEY_TOKEN,
           'language': 'ko-KR',
           'query': title
       }
   
       response = requests.get(BASE_URL+path, params=params).json() 
       result = response.get('results')
       
       # 영화 이름 검색 결과 없을 시, None 반환
       if result == []:
           return None
       
       # 영화 이름 검색 첫번째 결과의 id 값
       res_id = result[0].get('id')
       movie_id = res_id
       
       BASE_URL2 = 'https://api.themoviedb.org/3'
       path2 = f'/movie/{movie_id}/recommendations'
       params2 = {
           'api_key': 'f813cc9773fb55369f6d3e1dae17ba81',
           'language': 'ko-KR',
           'query': title
       }
       
       response_for_recommend = requests.get(BASE_URL2+path2, params=params2).json()
       result_for_recommend = response_for_recommend.get('results')
       
       titles_for_recommend = []
       
       for result in result_for_recommend:
           titles_for_recommend.append(result.get('title'))
           
       if titles_for_recommend == []:
           return []
       else:
           return titles_for_recommend
        
   
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
       추천 영화가 없을 경우 []를 반환
       영화 id 검색에 실패할 경우 None을 반환
       (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
       """
       pprint(recommendation('기생충'))
       # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
       pprint(recommendation('그래비티'))
       # []
       pprint(recommendation('검색할 수 없는 영화'))
       # None
   ```

   > 코드 리뷰

   - 거의 같다! 주소를 불러와서 API를 사용하는 방법 이외에 코드 구현은 크게 복잡하지 않아서 나와 비슷하다.

   

6. ## 출연진 및 연출진 데이터 조회

   - 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
   - requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
   - 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
   - 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
   - `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.

   > 결과 예시

   ```json
   {
       "cast": [
           "Song Kang-ho",
           "Lee Sun-kyun",
           "Cho Yeo-jeong",
           "Choi Woo-shik",
           "Park So-dam",
           "Lee Jung-eun",
           "Jang Hye-jin"
       ],
       "crew": [
           "Bong Joon-ho",
           "Park Hyun-cheol",
           "Han Jin-won",
           "Kim Seong-sik",
           "Lee Jung-hoon",
           "Yoon Young-woo"
       ]
   }
   ```

   > 내가 작성한 코드

   ```python
   import requests
   from pprint import pprint
   
   
   def credits(title):
       pass 
       # 여기에 코드를 작성합니다.  
       base_url = 'https://api.themoviedb.org/3'
       path = '/search/movie'
       params = {
           'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
           'language': 'ko-KR',
           'query': title
       }
       response = requests.get(base_url+path, params=params).json()
       if len(response['results']) < 1:
           return None
       mv_id = response['results'][0]['id']
   
       base_url_2 = 'https://api.themoviedb.org/3'
       path_2 = f'/movie/{mv_id}/credits'
       params_2 = {
           'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
           'language': 'ko-KR'
       }
       response_2 = requests.get(base_url_2+path_2, params=params_2).json()
       dic = {}
       dic['cast'] = []
       dic['crew'] = []
       for i in range(len(response_2['cast'])):
           if response_2['cast'][i]['cast_id'] < 10:
               dic['cast'].append(response_2['cast'][i]['name'])
       for i in range(len(response_2['crew'])):
           if response_2['crew'][i]['department'] == 'Directing':
               dic['crew'].append(response_2['crew'][i]['name'])
   
       return dic
       
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
       영화 id 검색에 실패할 경우 None을 반환
       """
       pprint(credits('기생충'))
       # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
       pprint(credits('검색할 수 없는 영화'))
       # None
   ```

   > 전공자 작성 코드

   ```python
   import requests
   from pprint import pprint
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   API_KEY_TOKEN = os.getenv('my_api_key')
   
   
   def credits(title):
       pass 
       # 여기에 코드를 작성합니다.  
       BASE_URL = 'https://api.themoviedb.org/3'
       path = '/search/movie'
       params = {
           'api_key': API_KEY_TOKEN,
           'language': 'ko-KR',
           'query': title
       }
       
       response = requests.get(BASE_URL+path, params=params).json() 
       result = response.get('results')
       
       # 영화 이름 검색 결과 없을 시, None 반환
       if result == []:
           return None
       
       # 영화 이름 검색 첫번째 결과의 id 값
       res_id = result[0].get('id')
       movie_id = res_id
       
           # 여기에 코드를 작성합니다.  
       BASE_URL2 = 'https://api.themoviedb.org/3'
       path2 = f'/movie/{movie_id}/credits'
       params2 = {
           'api_key': 'f813cc9773fb55369f6d3e1dae17ba81',
           'language': 'ko-KR',
           'query': title
       }
       
       response_for_credits = requests.get(BASE_URL2+path2, params=params2).json()
       
       cast_list_response = response_for_credits.get('cast')
       crew_list_response = response_for_credits.get('crew')
       
       cast_list = []
       crew_list = []
       
       for c in cast_list_response:
           if c.get('cast_id') < 10:
               cast_list.append(c.get('name'))
               
       for c in crew_list_response:
           if c.get('department') == 'Directing':
               crew_list.append(c.get('name'))
       
       return_dict = {}
       return_dict['cast'] = cast_list
       return_dict['crew'] = crew_list
       
       return return_dict
       
       
   
   
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       """
       제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
       영화 id 검색에 실패할 경우 None을 반환
       """
       pprint(credits('기생충'))
       # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
       pprint(credits('검색할 수 없는 영화'))
       # None
   ```

   > 코드 리뷰

   - 거의 같다! 주소를 불러와서 API를 사용하는 방법 이외에 코드 구현은 크게 복잡하지 않아서 나와 비슷하다.

   
