# This Python script is importing modules from a custom package named `mtai`. Here's a breakdown of
# what the script is doing:
import sys

# Add the parent directory to the sys.path to import mtai module
sys.path.append("../")

from mtai.mt import MT
from mtai.bios import Bio  # Importing Bio class for static use

secret_key = "secret_key_here"
mt = MT(secret_key=secret_key)

# Dynamic use
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
print(
    mt.bios.create_bio_from_text(
        text="My name is Bashiru and I love Surfing", output_format="json"
    )
)
print(mt.bios.retrieve_bio_by_id("664e033837511b57fa93dd2e"))
print(mt.bios.delete_bio_by_id("664e033837511b57fa93dd2e"))

# Static use
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
print(
    Bio.create_bio_from_text(
        text="My name is Bashiru and I love Surfing", output_format="json"
    )
)
print(Bio.retrieve_bio_by_id("664e033837511b57fa93dd2e"))
print(Bio.delete_bio_by_id("664e033837511b57fa93dd2e"))

print(Bio)
