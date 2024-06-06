# Tags

## Import
```python
from mtai.tags import Tag
```
## Tag.create_from_title(title)

```python
Tag.create_from_title(title="Python Programming Language")
```
*Arguments*

- `title`: provide your descriptive title.

*Returns*

JSON data from mtai API.

## Tag.create_from_title_summary(title, summary)
```python
Tag.create_from_title_summary("Python", "Python is a programming language")
```

*Arguments*

- `title`: provide your descriptive title.
- `summary`: your short summary
  
*Returns*

JSON data from mtai API.

## Tag.list()
```python
Tag.list()
```

*Returns*

JSON data from mtai API.

## Tag.get_tag_by_id(id)
```python
Tag.get_tag_by_id("664e033837511b57fa93dd2e")
```

*Arguments*

- `id`: tag id.

*Returns*

JSON data from mtai API.

## Tag.delete_tag_by_id(id)
```python
Tag.delete_tag_by_id("664e033837511b57fa93dd2e")
```

*Arguments*

- `id`: tag id.

*Returns*

JSON data from mtai API.