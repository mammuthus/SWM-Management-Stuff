import orionsdk
import os
import keyring

user = os.environ['userdomain'] + '\\' + os.getlogin()
swis = orionsdk.SwisClient("spbsws01", user, keyring.get_password("API_prod",user))

#to add user in a keychain:
#
# python
# import keyring
# import os
# user = os.environ['userdomain'] + '\\' + os.getlogin()
# keyring.set_password("API_prod", user, "xxxxx")
#
#xxxxx - password of the ad account