import aws_cdk as cdk
import pytest

from aws_cdk.assertions import Template
from src.stack import MyStack


@pytest.fixture(scope="session", name="template")
def template_fixture() -> Template:
    """Create a fixture for the CDK Template."""

    # Create a new CDK App
    app = cdk.App()

    # Instantiate the Stack within the App scope
    stack = MyStack(
        scope=app,
        id="TestStack",
    )

    # Synthesize the stack to a template
    return Template.from_stack(stack)
