import aws_cdk as cdk

from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from constructs import Construct


class MyStack(cdk.Stack):
    """
    Creates a Stack with:

    * A bucket with some extra configuration.
    * An IAM Role that can be assumed by a Lambda.
    * A policy tha allows the role get objects from the bucket.
    """

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(
            scope=self,
            id="MyBucket",
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            lifecycle_rules=[
                s3.LifecycleRule(
                    enabled=True,
                    abort_incomplete_multipart_upload_after=cdk.Duration.days(7),
                    transitions=[
                        s3.Transition(
                            storage_class=s3.StorageClass.INTELLIGENT_TIERING,
                            transition_after=cdk.Duration.days(60),
                        )
                    ],
                    noncurrent_version_expiration=cdk.Duration.days(30),
                    expiration=cdk.Duration.days(7),
                )
            ],
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
            versioned=True,
        )

        # In CDK it is not mandatory to specify the role name like in CloudFormation
        role = iam.Role(
            scope=self,
            id="MyLambdaRole",
            assumed_by=iam.ServicePrincipal(service="lambda.amazonaws.com"),
        )

        # This creates the policy that allows the role to get objects from the bucket
        bucket.grant_read(role)
