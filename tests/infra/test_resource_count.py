import pytest

from aws_cdk.assertions import Template


@pytest.mark.parametrize(
    argnames=["type", "count"],
    argvalues=[
        ("AWS::S3::Bucket", 1),
        ("AWS::IAM::Role", 1),
        ("AWS::IAM::Policy", 1),
    ],
)
def test_resource_count(type, count, template: Template):
    template.resource_count_is(type=type, count=count)
