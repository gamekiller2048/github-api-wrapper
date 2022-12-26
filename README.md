# github-api-wrapper
python api wrapper for writing, creating, reading and deleting files in github


## Example Reading File

```python
import github

client = github.Client()
client.read_file('[YOUR REPOSITORY]', '[YOUR PATH TO FILE]')
```
