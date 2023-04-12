# SWM-Management-Stuff
Scripts that simplify SolarWinds administration processes

# Creds
user = os.environ['userdomain'] + '\\' + os.getlogin()
swis = orionsdk.SwisClient(hostname, user, keyring.get_password(credentialname,user))
