#!/usr/bin/env python3

import aws_cdk as cdk

from cis_infra.cis_infra_stack import CisInfraStack


app = cdk.App()
CisInfraStack(app, "cis-infra")

app.synth()
