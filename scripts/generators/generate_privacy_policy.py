"""
Automated Privacy Policy generator for STAKC GDPR Template.
Usage: python scripts/generators/generate_privacy_policy.py --output docs/privacy_policy.md
"""
import argparse
import os
from datetime import datetime

TEMPLATE = """
# Privacy Policy

_Last updated: {date}_

## Introduction
This Privacy Policy describes how {project_name} ("we", "us", or "our") collects, uses, and protects your personal data in compliance with the GDPR.

## Data Collected
- Personal identification data
- Usage data
- Consent records
- Audit logs

## Purposes
- Service provision
- Legal compliance
- Security and fraud prevention
- Analytics and improvements

## User Rights
- Access, export, and deletion of data
- Consent management
- Data breach notification

## Data Security
- Encryption
- Access controls
- Audit trail

## Contact
For any privacy-related requests, contact: {contact_email}

---
*Generated automatically by STAKC GDPR Template*
"""

def main():
    parser = argparse.ArgumentParser(description="Generate Privacy Policy")
    parser.add_argument("--output", type=str, default="docs/privacy_policy.md", help="Output file path")
    parser.add_argument("--project-name", type=str, default=os.getenv("PROJECT_NAME", "STAKC Project"))
    parser.add_argument("--contact-email", type=str, default="dpo@localhost")
    args = parser.parse_args()

    policy = TEMPLATE.format(
        date=datetime.now().strftime("%Y-%m-%d"),
        project_name=args.project_name,
        contact_email=args.contact_email
    )

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(policy)
    print(f"Privacy Policy generated at {args.output}")

if __name__ == "__main__":
    main()
