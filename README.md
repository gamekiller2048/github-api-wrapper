# github-api-wrapper
python api wrapper for writing, creating, reading and deleting files in github


## Example Reading File

```python
import github

client = github.Client()
client.read_file('[YOUR REPOSITORY]', '[YOUR PATH TO FILE]')
```


## Example Writing File

```python
import github

client = github.Client()
client.update_file('[YOUR REPOSITORY]', '[YOUR PATH TO FILE]', '[CONTENT TO WRITE]', '[OPTIONAL COMMIT MESSAGE]')
```