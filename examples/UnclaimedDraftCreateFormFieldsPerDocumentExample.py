import json
from datetime import date, datetime
from pprint import pprint

from dropbox_sign import ApiClient, ApiException, Configuration, api, models

configuration = Configuration(
    username="YOUR_API_KEY",
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    form_fields_per_document_1 = models.SubFormFieldsPerDocumentText(
        document_index=0,
        api_id="uniqueIdHere_1",
        type="text",
        required=True,
        signer="1",
        width=100,
        height=16,
        x=112,
        y=328,
        name="",
        page=1,
        placeholder="",
        validation_type="numbers_only",
    )

    form_fields_per_document_2 = models.SubFormFieldsPerDocumentSignature(
        document_index=0,
        api_id="uniqueIdHere_2",
        type="signature",
        required=True,
        signer="0",
        width=120,
        height=30,
        x=530,
        y=415,
        name="",
        page=1,
    )

    form_fields_per_document = [
        form_fields_per_document_1,
        form_fields_per_document_2,
    ]

    unclaimed_draft_create_request = models.UnclaimedDraftCreateRequest(
        type="request_signature",
        test_mode=False,
        file_urls=[
            "https://www.dropbox.com/s/ad9qnhbrjjn64tu/mutual-NDA-example.pdf?dl=1",
        ],
        form_fields_per_document=form_fields_per_document,
    )

    try:
        response = api.UnclaimedDraftApi(api_client).unclaimed_draft_create(
            unclaimed_draft_create_request=unclaimed_draft_create_request,
        )

        pprint(response)
    except ApiException as e:
        print(
            "Exception when calling UnclaimedDraftApi#unclaimed_draft_create: %s\n" % e
        )
