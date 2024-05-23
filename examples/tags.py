import sys

sys.path.append("../")

from mtai.mt import MT

secret_key = "secret_key_here"
mt = MT(secret_key=secret_key)
print(mt.tags.list())
print(mt.tags.create_from_title(title="Python Programming Language"))
print(mt.tags.create_from_title_summary("Python", "Python is a programming language"))
print(mt.tags.get_tab_by_id("664e033837511b57fa93dd2e"))
print(mt.tags.delete_tag_by_id("664e033837511b57fa93dd2e"))

# Static Use
from mtai.tags import Tag

print(Tag.list())
print(Tag.create_from_title(title="Python Programming Language"))
print(Tag.create_from_title_summary("Python", "Python is a programming language"))
print(Tag.get_tab_by_id("664e033837511b57fa93dd2e"))
print(Tag.delete_tag_by_id("664e033837511b57fa93dd2e"))
