# github-api-wrapper
python api wrapper for writing, creating, reading and deleting files in github


## Example Reading File

```python
import github

client = github.Client(MY_USERNAME, MY_TOKEN)
client.read_file('[YOUR REPOSITORY]', '[YOUR PATH TO FILE]')
```


## Example Writing File

```python
import github

client = github.Client(MY_USERNAME, MY_TOKEN)
client.update_file('[YOUR REPOSITORY]', '[YOUR PATH TO FILE]', '[CONTENT TO WRITE]', '[OPTIONAL COMMIT MESSAGE]')
```


### Finding Your Access Token
Click top right profile

Go to Settings -> Developer settings -> Personal access tokens -> Tokens (classic)

Click Generate new token -> Generate new token (classic)

Select expiration & control option scopes **(make sure to check repo scope in order for access to private repositories)**

Click Generate token
