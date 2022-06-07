import cloudscraper
import requests

from rich import print

BASE_URL = 'https://www.blinkist.com/'

scraper = cloudscraper.create_scraper()


def get_free_daily(locale):
    # see also: https://www.blinkist.com/en/content/daily
    response = scraper.get(
        BASE_URL + 'api/free_daily',
        params={'locale': locale}
    )
    return response.json()


# auth ↓
# auth_req = scraper.get(
#     'https://www.blinkist.com/api/mickey_mouse/setup?pathname=/en/nc/new-reader/the-4-stages-of-psychological-safety-en&search=&locale=en')
# print(auth_req.json())


def get_chapters(book_slug):
    url = f"https://www.blinkist.com/api/books/{book_slug}/chapters"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0',  # needed
        'x-requested-with': 'XMLHttpRequest',  # needed
        # 'Cookie': '_dd_s=rum=1&id=87797166-003c-439e-b75e-8e656785182a&created=1654611369308&expire=1654616987146; _pk_id.1.a1f5=d5a80e8194c75db8.1654611370.1.1654616087.1654611373.; bk_c_n=778d8375-4686-4c75-add8-69eb32c05049; internal_session=false; _blinkist-webapp_session=WURSOGJRVlVaSWxINVJFRllmNXN6ZTk1aytTYlBvcUVtUUoyNUZzUmRITTMwdHhyWlhVeEJFSFZXRURKRG9NVVdVMnlvbGZhQmRMcUFDZmp5V1ljVXhUMVJYMmRVelgxYkpJZmJ5QkgvTDdOTzNSczROUjVXTUhKcktCeHcyRTJoUjdrc2Vad2Z2QkZVNEpnbDg1cTRHUFE2UzRTakkvZldyR1JzaTdFTUlhb3lGR1VwUFlhUkVjT0ozSVZwSHYyOGZyalRmTDVkTnNKV1AvdFlMckoyOHNUN1h6cmRLNzkwa3dwSVAzRUJNM0JBSUh4cUNlRDlBc05Ga2lJUUIxa2lVSFBIVFNDQTlPWkE1LzNIdVhvamFmdlh2MjM4alNQZzkreEM0WkRuZ2xsc3l0S0JCejlvQW1pVi9aR28xZEtnNHd0bUNxazdOMGltMU9jUWsvanF3encvK3R0cXNXaUwxdVdPQ3FxVkUrMzZSbnhWYjNCVGdqWGJPTVJyZUhPVUQvSWFrRjR5cVFVRHIxckp6VmhUNEVCN25DYkhmNm1WSU00MFRGUE1HRT0tLUY3S2JldzUyYWZiaVAzZzdKOVVCdFE9PQ%3D%3D--3825ef7d5557fe235d7c56fba832b15758b96357; G_ENABLED_IDPS=google; modal-wdyhau-survey=1; new_onboarding=1; locale=en; __cf_bm=PPzM_.DFRoCsbOXhhSWzd.Z4rmXmDOJ4OEwiGwSPWFY-1654615985-0-AQ9Q2O2bwh2SjvmXLE3ETkBxzR2Zla5XonE1FlE/OSfz/mwh4qguzD86ZWeufBtCQdi3XiuxwQTV4nqoxgxrpeHWnfoN+hKWu4jA/N+AwKzQz3XwTZcL2U/uuNmlnTxldRuF1IcYg+YAiKFUFNPErQdDQZw2AuCkc0F04fEobl+WChS1u6hSUpm+J0dXUNUP6Q==; coupon_code=freedaily; __cf_bm=U1cjkF7EAuc8U0zHUD8AdkpNxft2755lkwqUGVXVf98-1654616460-0-AdCt7qmGL6eNnwhBnS8OMWXFP8Z9KDmgTZtMDHNSVPcK6cROEVN61xYVycvf6hOYdat3lDW95FcoZhlg9H8EUqpGrQuKeajGQgpBakGk1079; _blinkist-webapp_session=c08rU1VNcjZ0SjgzKzdtUFdnemMzZUxaVTU2R3ozNDAxc2lxUWp3eGo3QUgxbk4xWVkzaHhHWituNWZKOHJlcjQzK1p1dTZ3NW1DSnAzWHNDU0JvdVJyWFpVbFA1MG8yRmNSUDRZdHN4T2tSRDZ3b2thbHdIOTNGTDB4cldaSXJJdWRROG1SNnNNRVlaYjJIMVdWOGxWSlF3c2NpTEhjNERsWjYxMlNtWjMzOGZONDRsWW14TnBjcmdWYlYyTndkN2tCc3hiblpPcGswdW1uekpMNlRVU2RveEpBWmRPT2dtTk1QYTF3ZGdVbyt3MEJPYWE5SUVLSGlTekN0K3hLVWlVOGduTkpPdkUvQmRMQXBpZjVoMG90Z0c2aStCYThEYVRqNGVxYW1WeEdVZkVLOHpMQ1lPR2poaTFmcmI3RE9XNXVXQzROZDZWeEFHQ3hyS1hibmdBPT0tLS9RMEtJUmdoUm9UQUJUbFMwVlhvNHc9PQ%3D%3D--3030290cac36f512b8b859f6571d257978b08b7c; bk_c_n=371064e0-2874-4061-8c8f-0de7f99d6873',
    }

    response = requests.request("GET", url, headers=headers)
    response.raise_for_status()
    return response.json()['chapters']


def get_chapter(book_id, chapter_id):
    url = f"https://www.blinkist.com/api/books/{book_id}/chapters/{chapter_id}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0',  # needed
        'x-requested-with': 'XMLHttpRequest',  # needed
        # 'Cookie': '_dd_s=rum=1&id=87797166-003c-439e-b75e-8e656785182a&created=1654611369308&expire=1654616987146; _pk_id.1.a1f5=d5a80e8194c75db8.1654611370.1.1654616087.1654611373.; bk_c_n=778d8375-4686-4c75-add8-69eb32c05049; internal_session=false; _blinkist-webapp_session=WURSOGJRVlVaSWxINVJFRllmNXN6ZTk1aytTYlBvcUVtUUoyNUZzUmRITTMwdHhyWlhVeEJFSFZXRURKRG9NVVdVMnlvbGZhQmRMcUFDZmp5V1ljVXhUMVJYMmRVelgxYkpJZmJ5QkgvTDdOTzNSczROUjVXTUhKcktCeHcyRTJoUjdrc2Vad2Z2QkZVNEpnbDg1cTRHUFE2UzRTakkvZldyR1JzaTdFTUlhb3lGR1VwUFlhUkVjT0ozSVZwSHYyOGZyalRmTDVkTnNKV1AvdFlMckoyOHNUN1h6cmRLNzkwa3dwSVAzRUJNM0JBSUh4cUNlRDlBc05Ga2lJUUIxa2lVSFBIVFNDQTlPWkE1LzNIdVhvamFmdlh2MjM4alNQZzkreEM0WkRuZ2xsc3l0S0JCejlvQW1pVi9aR28xZEtnNHd0bUNxazdOMGltMU9jUWsvanF3encvK3R0cXNXaUwxdVdPQ3FxVkUrMzZSbnhWYjNCVGdqWGJPTVJyZUhPVUQvSWFrRjR5cVFVRHIxckp6VmhUNEVCN25DYkhmNm1WSU00MFRGUE1HRT0tLUY3S2JldzUyYWZiaVAzZzdKOVVCdFE9PQ%3D%3D--3825ef7d5557fe235d7c56fba832b15758b96357; G_ENABLED_IDPS=google; modal-wdyhau-survey=1; new_onboarding=1; locale=en; __cf_bm=PPzM_.DFRoCsbOXhhSWzd.Z4rmXmDOJ4OEwiGwSPWFY-1654615985-0-AQ9Q2O2bwh2SjvmXLE3ETkBxzR2Zla5XonE1FlE/OSfz/mwh4qguzD86ZWeufBtCQdi3XiuxwQTV4nqoxgxrpeHWnfoN+hKWu4jA/N+AwKzQz3XwTZcL2U/uuNmlnTxldRuF1IcYg+YAiKFUFNPErQdDQZw2AuCkc0F04fEobl+WChS1u6hSUpm+J0dXUNUP6Q==; coupon_code=freedaily; __cf_bm=U1cjkF7EAuc8U0zHUD8AdkpNxft2755lkwqUGVXVf98-1654616460-0-AdCt7qmGL6eNnwhBnS8OMWXFP8Z9KDmgTZtMDHNSVPcK6cROEVN61xYVycvf6hOYdat3lDW95FcoZhlg9H8EUqpGrQuKeajGQgpBakGk1079; _blinkist-webapp_session=c08rU1VNcjZ0SjgzKzdtUFdnemMzZUxaVTU2R3ozNDAxc2lxUWp3eGo3QUgxbk4xWVkzaHhHWituNWZKOHJlcjQzK1p1dTZ3NW1DSnAzWHNDU0JvdVJyWFpVbFA1MG8yRmNSUDRZdHN4T2tSRDZ3b2thbHdIOTNGTDB4cldaSXJJdWRROG1SNnNNRVlaYjJIMVdWOGxWSlF3c2NpTEhjNERsWjYxMlNtWjMzOGZONDRsWW14TnBjcmdWYlYyTndkN2tCc3hiblpPcGswdW1uekpMNlRVU2RveEpBWmRPT2dtTk1QYTF3ZGdVbyt3MEJPYWE5SUVLSGlTekN0K3hLVWlVOGduTkpPdkUvQmRMQXBpZjVoMG90Z0c2aStCYThEYVRqNGVxYW1WeEdVZkVLOHpMQ1lPR2poaTFmcmI3RE9XNXVXQzROZDZWeEFHQ3hyS1hibmdBPT0tLS9RMEtJUmdoUm9UQUJUbFMwVlhvNHc9PQ%3D%3D--3030290cac36f512b8b859f6571d257978b08b7c; bk_c_n=371064e0-2874-4061-8c8f-0de7f99d6873',
    }

    response = requests.request("GET", url, headers=headers)
    response.raise_for_status()
    return response.json()


# free_daily = get_free_daily(locale='en')
# book = free_daily['book']
# print(book['title'])

# chapters = get_chapters(book['slug'])

# chapters = [
#     {
#         'id': '628223936cee0700089119ca'
#     }
# ]

book_id = '628223936cee0700089119c9'
chapter_id = '628223936cee0700089119ca'

chapter = get_chapter(book_id=book_id, chapter_id=chapter_id)
print(chapter)
