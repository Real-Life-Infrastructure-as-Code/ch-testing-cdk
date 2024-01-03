from aws_cdk.assertions import Template


# snapshot is a fixture provided by syrupy
def test_template_snapshot(snapshot, template: Template):
    assert template.to_json() == snapshot
