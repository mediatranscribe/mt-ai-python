# Descriptions

## Import
```python
from mtai.descriptions import Description
```
## Description.create_from_title(title)

```python
Description.create_from_title(title="Python Programming Language")
```
*Arguments*

- `title`: provide your descriptive title.

*Returns*

JSON data from mtai API.

## Description.create_from_title_summary(title, summary)
```python
Description.create_from_title_summary("Python", "Python is a programming language")
```

*Arguments*

- `title`: provide your descriptive title.
- `summary`: your short summary
  
*Returns*

JSON data from mtai API.

## Description.list()
```python
Description.list()
```

*Returns*

JSON data from mtai API.

## Description.get_description_by_id(id)
```python
Description.get_description_by_id("66410eea2514d4ad390ebad0")
```

*Arguments*

- `id`: description id.

*Returns*

JSON data from mtai API.

## Description.delete_description_by_id(id)
```python
Description.delete_description_by_id("66410eea2514d4ad390ebad0")
```

*Arguments*

- `id`: description id.

*Returns*

JSON data from mtai API.