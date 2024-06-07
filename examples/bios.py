import sys

sys.path.append("../")

from mtai.mt import MT

secret_key = "secret_key_here"
mt = MT(secret_key=secret_key)
print(mt.bios.list())
print(
    mt.bios.create_mentor_mentee_bio(
        country="Ghana",
        job_title="architect",
        interests="swimming",
        is_mentor=False,
        max_length=300,
    )
)
print(mt.bios.creta_bio_from_text(text="My name is Bashiru and I love Surfing"))
print(mt.bios.retrieve_bio_by_id("664e033837511b57fa93dd2e"))
print(mt.bios.delete_bio_by_id("664e033837511b57fa93dd2e"))

# Static Use
from mtai.bios import Bio

print(Bio.list())
print(
    Bio.create_mentor_mentee_bio(
        country="Ghana",
        job_title="architect",
        interests="swimming",
        is_mentor=False,
        max_length=300,
    )
)
print(Bio.create_bio_from_text("My name is Bashiru and I love Surfing"))
print(Bio.retrieve_bio_by_id("664e033837511b57fa93dd2e"))
print(Bio.delete_bio_by_id("664e033837511b57fa93dd2e"))

print(Bio)
