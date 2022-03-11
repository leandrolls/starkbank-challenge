import starkbank
import os

#In webhook_url put url of server.
webhook_url = 'https://webhook.site/302404de-7031-4ff6-89e5-6f9952ee59c7'

def credentials_init():

    private_key_content = f"""
        -----BEGIN EC PARAMETERS-----
        BgUrgQQACg==
        -----END EC PARAMETERS-----
        -----BEGIN EC PRIVATE KEY-----
        {os.environ.get('pvk')}
        -----END EC PRIVATE KEY-----
        """

    project = starkbank.Project(
        environment="sandbox",
        id="4837316610752512",
        private_key=private_key_content)

    starkbank.user = project

