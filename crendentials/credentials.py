import starkbank

webhook_url = ''

def credentials_init():
    private_key_content = """
        -----BEGIN EC PARAMETERS-----
        BgUrgQQACg==
        -----END EC PARAMETERS-----
        -----BEGIN EC PRIVATE KEY-----
        
        -----END EC PRIVATE KEY-----
        """

    project = starkbank.Project(
        environment="sandbox",
        id="",
        private_key=private_key_content)

    starkbank.user = project

