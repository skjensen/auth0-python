from .rest import RestClient


class DeviceCredentials(object):

    """Auth0 connection endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def _url(self, id=None):
        url = 'https://%s/api/v2/device-credentials' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def get(self, user_id, client_id, type, fields=None, include_fields=True):
        """List device credentials.

        Args:
            user_id (str): The user_id of the devices to retrieve.

            client_id (str): The client_id of the devices to retrieve.

            type (str): The type of credentials (public_key, refresh_token).

            fields (list, optional): A list of fields to include or exclude
                (depending on include_fields) from the result, empty to
                retrieve all fields

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise
                (defaults to true)


        See: https://auth0.com/docs/api/management/v2#!/Device_Credentials/get_device_credentials
        """

        params = {
            'fields': fields and ','.join(fields) or None,
            'include_fields': str(include_fields).lower(),
            'user_id': user_id,
            'client_id': client_id,
            'type': type,
        }
        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Create a device public key.

        Args:
            body (dict): parameters for creating the public key (e.g: type,
                device_name, client_id, etc).
                Please see: https://auth0.com/docs/api/v2#!/Device_Credentials/post_device_credentials
        """
        return self.client.post(self._url(), data=body)

    def delete(self, id):
        """Delete credential.

        Args:
            id (str):  The id of the credential to delete


        See: https://auth0.com/docs/api/management/v2#!/Device_Credentials/delete_device_credentials_by_id
        """
        return self.client.delete(self._url(id))
