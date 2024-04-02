from aws_cdk.assertions import Template


def test_bucket_logical_id(template: Template):
    logical_ids = template.to_json()["Resources"].keys()
    assert "MyBucketF68F3FF0" in logical_ids
