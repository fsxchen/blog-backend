import sqlite3
import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from poem.models import Poem, Poet


conn = sqlite3.connect("./db.sqlite3")

cur1 = conn.execute("SELECT * FROM poem_poet;") 
cur2 = conn.execute("SELECT * FROM poem_poem;") 

# 同步poet
# for row in cur1:
#     id, total_num, age, poet_comment, name, url, total_url, poet_intr, add_time, all = row
#     Poet.objects.create(
#             total_num=total_num,
#             age=age,
#             poet_comment=poet_comment,
#             name=name,
#             url=url,
#             total_url=total_url,
#             poet_intr=poet_intr,
#             add_time=add_time,
#             all=all
#             )
# 
# print("OK")

for row in cur2:
    id, content, age, url, categ, title, comment, add_time, auth_name, auth = row
    auth_name = auth
    data = {
            "content": content,
            "age": age,
            "url": url,
            "categ": categ,
            "title": title,
            "comment": comment,
            "add_time": add_time,
            "auth_name": auth_name
            }
    p = Poet.objects.filter(name=auth).first()
    if p:
        data["auth"] = p
    Poem.objects.create(**data) 

print("OK")

