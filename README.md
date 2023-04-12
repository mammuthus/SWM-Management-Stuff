# SolarWinds Administration Scripts

This repository contains a collection of scripts that simplify SolarWinds administration processes. These scripts are designed to streamline specific tasks and processes within SolarWinds products.

## Creds

To use the scripts in this repository, you'll need to provide your SolarWinds credentials in the script.

```python
user = os.environ['userdomain'] + '\\' + os.getlogin()
swis = orionsdk.SwisClient(hostname, user, keyring.get_password(credentialname,user))
```
Replace ```hostname``` with the hostname or IP address of your SolarWinds server.

Replace ```credentialname``` with the name of the credential that you want to use.
