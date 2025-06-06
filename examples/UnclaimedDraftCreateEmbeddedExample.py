import json
from datetime import date, datetime
from pprint import pprint

from dropbox_sign import ApiClient, ApiException, Configuration, api, models

configuration = Configuration(
    username="YOUR_API_KEY",
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    unclaimed_draft_create_embedded_request = (
        models.UnclaimedDraftCreateEmbeddedRequest(
            client_id="b6b8e7deaf8f0b95c029dca049356d4a2cf9710a",
            requester_email_address="jack@dropboxsign.com",
            test_mode=True,
            files=[
                open("./example_signature_request.pdf", "rb").read(),
            ],
        )
    )

    try:
        response = api.UnclaimedDraftApi(api_client).unclaimed_draft_create_embedded(
            unclaimed_draft_create_embedded_request=unclaimed_draft_create_embedded_request,
        )

        pprint(response)
    except ApiException as e:
        print(
            "Exception when calling UnclaimedDraftApi#unclaimed_draft_create_embedded: %s\n"
            % e
        )
