from aws_cdk.assertions import Template


def test_bucket(template: Template):
    template.has_resource_properties(
        type="AWS::S3::Bucket",
        props={
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
                ]
            },
            "BucketName": "my-bucket-56e143c0",
            "LifecycleConfiguration": {
                "Rules": [
                    {
                        "AbortIncompleteMultipartUpload": {"DaysAfterInitiation": 7},
                        "ExpirationInDays": 7,
                        "NoncurrentVersionExpiration": {"NoncurrentDays": 30},
                        "Status": "Enabled",
                        "Transitions": [
                            {
                                "StorageClass": "INTELLIGENT_TIERING",
                                "TransitionInDays": 60,
                            }
                        ],
                    }
                ]
            },
            "OwnershipControls": {"Rules": [{"ObjectOwnership": "BucketOwnerEnforced"}]},
            "PublicAccessBlockConfiguration": {
                "BlockPublicAcls": True,
                "BlockPublicPolicy": True,
                "IgnorePublicAcls": True,
                "RestrictPublicBuckets": True,
            },
            "VersioningConfiguration": {"Status": "Enabled"},
        },
    )
