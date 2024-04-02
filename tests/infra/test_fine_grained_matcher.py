from aws_cdk.assertions import Template
from aws_cdk.assertions import Match


def test_bucket_name(template: Template):
    template.has_resource_properties(
        type="AWS::S3::Bucket",
        props={
            "LifecycleConfiguration": {
                "Rules": [
                    {
                        "AbortIncompleteMultipartUpload": {"DaysAfterInitiation": Match.any_value()},
                        "ExpirationInDays": Match.any_value(),
                        "NoncurrentVersionExpiration": {"NoncurrentDays": Match.any_value()},
                        "Status": "Enabled",
                        "Transitions": [
                            {
                                "StorageClass": "INTELLIGENT_TIERING",
                                "TransitionInDays": Match.any_value(),
                            }
                        ],
                    }
                ]
            }
        }
    )
