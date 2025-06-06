import json
from datetime import date, datetime
from pprint import pprint

from dropbox_sign import ApiClient, ApiException, Configuration, api, models

configuration = Configuration(
    username="YOUR_API_KEY",
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    signing_options = models.SubSigningOptions(
        default_type="draw",
        draw=True,
        phone=False,
        type=True,
        upload=True,
    )

    signers_1 = models.SubSignatureRequestSigner(
        name="Jack",
        email_address="jack@example.com",
        order=0,
    )

    signers_2 = models.SubSignatureRequestSigner(
        name="Jill",
        email_address="jill@example.com",
        order=1,
    )

    signers = [
        signers_1,
        signers_2,
    ]

    signature_request_edit_embedded_request = models.SignatureRequestEditEmbeddedRequest(
        client_id="b6b8e7deaf8f0b95c029dca049356d4a2cf9710a",
        message="Please sign this NDA and then we can discuss more. Let me know if you\nhave any questions.",
        subject="The NDA we talked about",
        test_mode=True,
        title="NDA with Acme Co.",
        cc_email_addresses=[
            "lawyer1@dropboxsign.com",
            "lawyer2@dropboxsign.com",
        ],
        files=[
            open("./example_signature_request.pdf", "rb").read(),
        ],
        signing_options=signing_options,
        signers=signers,
    )

    try:
        response = api.SignatureRequestApi(api_client).signature_request_edit_embedded(
            signature_request_id="fa5c8a0b0f492d768749333ad6fcc214c111e967",
            signature_request_edit_embedded_request=signature_request_edit_embedded_request,
        )

        pprint(response)
    except ApiException as e:
        print(
            "Exception when calling SignatureRequestApi#signature_request_edit_embedded: %s\n"
            % e
        )
