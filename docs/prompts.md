# Prompts

## Import
```python
from mtai.prompts import Prompt
```
## Prompt.ask_question(prompt)

```python
Prompt.ask_question(prompt="What is the capital of India?")
```
*Arguments*

- `prompt`: provide your description.

*Returns*

JSON data from mtai API.

## Prompt.list()
```python
Prompt.list()
```

*Returns*

JSON data from mtai API.

## Prompt.get_prompt_by_id(id)
```python
Prompt.get_prompt_by_id("664e033837511b57fa93dd2e")
```

*Arguments*

- `id`: prompt id.

*Returns*

JSON data from mtai API.

## Prompt.delete_prompt_by_id(id)
```python
Prompt.delete_prompt_by_id("664e033837511b57fa93dd2e")
```

*Arguments*

- `id`: prompt id.

*Returns*

JSON data from mtai API.