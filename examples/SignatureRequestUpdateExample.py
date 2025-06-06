import json
from datetime import date, datetime
from pprint import pprint

from dropbox_sign import ApiClient, ApiException, Configuration, api, models

configuration = Configuration(
    username="YOUR_API_KEY",
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    signature_request_update_request = models.SignatureRequestUpdateRequest(
        signature_id="2f9781e1a8e2045224d808c153c2e1d3df6f8f2f",
        email_address="john@example.com",
    )

    try:
        response = api.SignatureRequestApi(api_client).signature_request_update(
            signature_request_id="fa5c8a0b0f492d768749333ad6fcc214c111e967",
            signature_request_update_request=signature_request_update_request,
        )

        pprint(response)
    except ApiException as e:
        print(
            "Exception when calling SignatureRequestApi#signature_request_update: %s\n"
            % e
        )
