import sys

sys.path.append("../")

from mtai.mt import MT

secret_key = "secret_key_here"
mt = MT(secret_key=secret_key)
print(mt.bios.list())
print(mt.bios.create_from_title(title="Python Programming Language"))
print(mt.bios.create_from_title_summary("Python", "Python is a programming language"))
print(mt.bios.get_Bio_by_id("664e033837511b57fa93dd2e"))
print(mt.bios.delete_Bio_by_id("664e033837511b57fa93dd2e"))

# Static Use
from mtai.bios import Bio

print(Bio.list())
print(Bio.create_from_title(title="Python Programming Language"))
print(Bio.create_from_title_summary("Python", "Python is a programming language"))
print(Bio.get_tab_by_id("664e033837511b57fa93dd2e"))
print(Bio.delete_Bio_by_id("664e033837511b57fa93dd2e"))

print(Bio)
