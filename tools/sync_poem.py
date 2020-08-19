import sys
import os
import pymongo


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from poem.models import Poem, Poet

client = pymongo.MongoClient("10.0.14.129")

db = client.wenxue

# for poet in db.poet.find():
#     del poet['_id']
#     print(poet)
#     if 'all' in poet:
#         poet['all'] = int(poet['all'])
#     else:
#         poet['all'] = 0
#     Poet.objects.create(**poet)

for poem in db.shici.find():
    del poem['_id']
    Poem.objects.create(**poem)

