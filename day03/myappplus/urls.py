from django.conf.urls import url
from .views import (get_person_by_bank, rem_bankcard, get_engineer_by_desc,
                    get_engineer_by_des, get_engineer_by_language,
                    get_author_by_book,get_book_by_author)

urlpatterns = [
    url(r'^get_person_by_bank', get_person_by_bank),
    url(r'^remove_bankcard', rem_bankcard),
    url(r'^get_engineer_by_desc', get_engineer_by_desc),
    url(r'^get_engineer_by_des', get_engineer_by_des),
    url(r'^get_engineer_by_language', get_engineer_by_language),
    url(r'^get_author_by_book', get_author_by_book),
    url(r'^get_book_by_author', get_book_by_author),
]