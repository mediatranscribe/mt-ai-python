# Bios

## Import
```python

from mtai.bios import Bio
```
## Bio.create_mentor_mentee_bio(country, job_title, interests, is_mentor=False, max_length=300)

```python
Bio.create_mentor_mentee_bio(
    country="Ghana",
    job_title="architect",
    interests="swimming",
    is_mentor=False,
    max_length=300,
)

```
*Arguments*

- `country`: provide your description.
  `job_title`: provide your description.
  `interests`: provide your descriptiion.
  `is_mentor`: False.
  `max_length`: 300.

*Returns*

JSON data from mtai API.

## Bio.create_bio_from_text(text, output_format, max_length=300)
```python
Bio.create_bio_from_text(
    text="My name is Bashiru and I love Surfing",
    output_format="json",
    max_length=300

)
```

*Arguments*

- `text`: provide your description.
  `output_format`: json
  `max_length`: 300
  
*Returns*

JSON data from mtai API.

## Bio.list()
```python
Bio.list()
```

*Returns*

JSON data from mtai API.

## Bio.get_Bio_by_id(id)
```python
Bio.get_Bio_by_id("664e033837511b57fa93dd2e")
```

*Arguments*

- `id`: Bio id.

*Returns*

JSON data from mtai API.

## Bio.delete_Bio_by_id(id)
```python
Bio.delete_Bio_by_id("664e033837511b57fa93dd2e")
```

*Arguments*

- `id`: Bio id.

*Returns*

JSON data from mtai API.