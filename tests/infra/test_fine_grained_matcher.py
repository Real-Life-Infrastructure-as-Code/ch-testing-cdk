from aws_cdk.assertions import Template
from aws_cdk.assertions import Match


def test_bucket_name(template: Template):
    template.has_resource_properties(
        type="AWS::S3::Bucket",
        props={
            "BucketName": Match.string_like_regexp(pattern="my-bucket-*")
        }
    )
