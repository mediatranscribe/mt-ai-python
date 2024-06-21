import sys

sys.path.append("../")

from mtai.mt import MT

secret_key = "secret_key_here"
mt = MT(secret_key=secret_key)
print(mt.descriptions.list())
print(mt.descriptions.create_from_title(title="Python Programming Language"))
print(
    mt.descriptions.create_from_title_summary(
        "Python", "Python is a programming language"
    )
)
print(mt.descriptions.get_description_by_id("664e033837511b57fa93dd2e"))
print(mt.descriptions.delete_description_by_id("664e033837511b57fa93dd2e"))

# Static Use
from mtai.descriptions import Description

print(Description.list())
print(Description.create_from_title(title="Python Programming Language"))
print(
    Description.create_from_title_summary("Python", "Python is a programming language")
)
print(Description.get_description_by_id("66410eea2514d4ad390ebad0"))
print(Description.delete_description_by_id("66410eea2514d4ad390ebad0"))
