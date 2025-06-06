import json
from datetime import date, datetime
from pprint import pprint

from dropbox_sign import ApiClient, ApiException, Configuration, api, models

configuration = Configuration(
    username="YOUR_API_KEY",
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    form_field_rules_1_triggers_1 = models.SubFormFieldRuleTrigger(
        id="uniqueIdHere_1",
        operator="is",
        value="foo",
    )

    form_field_rules_1_triggers = [
        form_field_rules_1_triggers_1,
    ]

    form_field_rules_1_actions_1 = models.SubFormFieldRuleAction(
        hidden=True,
        type="change-field-visibility",
        field_id="uniqueIdHere_2",
    )

    form_field_rules_1_actions = [
        form_field_rules_1_actions_1,
    ]

    field_options = models.SubFieldOptions(
        date_format="DD - MM - YYYY",
    )

    form_field_rules_1 = models.SubFormFieldRule(
        id="rule_1",
        trigger_operator="AND",
        triggers=form_field_rules_1_triggers,
        actions=form_field_rules_1_actions,
    )

    form_field_rules = [
        form_field_rules_1,
    ]

    form_fields_per_document_1 = models.SubFormFieldsPerDocumentText(
        document_index=0,
        api_id="uniqueIdHere_1",
        type="text",
        required=True,
        signer="0",
        width=100,
        height=16,
        x=112,
        y=328,
        name="",
        page=1,
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

    merge_fields_1 = models.SubMergeField(
        name="Full Name",
        type="text",
    )

    merge_fields_2 = models.SubMergeField(
        name="Is Registered?",
        type="checkbox",
    )

    merge_fields = [
        merge_fields_1,
        merge_fields_2,
    ]

    signer_roles_1 = models.SubTemplateRole(
        name="Client",
        order=0,
    )

    signer_roles_2 = models.SubTemplateRole(
        name="Witness",
        order=1,
    )

    signer_roles = [
        signer_roles_1,
        signer_roles_2,
    ]

    template_create_embedded_draft_request = models.TemplateCreateEmbeddedDraftRequest(
        client_id="37dee8d8440c66d54cfa05d92c160882",
        message="For your approval",
        subject="Please sign this document",
        test_mode=True,
        title="Test Template",
        file_urls=[
            "https://www.dropbox.com/s/ad9qnhbrjjn64tu/mutual-NDA-example.pdf?dl=1",
        ],
        cc_roles=[
            "Manager",
        ],
        field_options=field_options,
        form_field_rules=form_field_rules,
        form_fields_per_document=form_fields_per_document,
        merge_fields=merge_fields,
        signer_roles=signer_roles,
    )

    try:
        response = api.TemplateApi(api_client).template_create_embedded_draft(
            template_create_embedded_draft_request=template_create_embedded_draft_request,
        )

        pprint(response)
    except ApiException as e:
        print(
            "Exception when calling TemplateApi#template_create_embedded_draft: %s\n"
            % e
        )
