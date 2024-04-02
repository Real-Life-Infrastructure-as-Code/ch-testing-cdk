from aws_cdk.assertions import Template
from aws_cdk.assertions import Match


def test_bucket_lifecycle_config(template: Template):
    template.has_resource_properties(
        type="AWS::S3::Bucket",
        props={
            "LifecycleConfiguration": {
                "Rules": [
                    {
                        "AbortIncompleteMultipartUpload": {
                            "DaysAfterInitiation": 7
                        },
                        "ExpirationInDays": 7,
                        "NoncurrentVersionExpiration": {
                            "NoncurrentDays": Match.any_value()
                        },
                        "Status": "Enabled",
                        "Transitions": [
                            {
                                "StorageClass": "INTELLIGENT_TIERING",
                                "TransitionInDays": 60,
                            }
                        ],
                    }
                ]
            }
        }
    )
