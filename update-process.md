## Update Process

This will outline the system workflow of updating our chatbot as features evolve.

_Feature Development_

    Feature Development → Branch Creation → Code & Prompt Update


_Testing_

    Automated Tests Triggered → Test Result Review


_Approval & Deployment_
    
    Prototype Deployment → Approval & Merge → Production Deployment

_Policy Update_

    Rollback Plan → Policy Update Process

### Base deployment strategy
1. Cloud Hosting:
    - Host the chatbot backend on GCP or Azure.
    - Azure AI Studio can manage models directly or deploy locally to our own server endpoints.
    - GCP can serve as the main conversational endpoint for the frontend app.
2. Scalability & Load Balancing:
    - GCP load balancers will allow us to scale easily and direct traffic efficiently.
3. Version Isolation:
    - Spin up separate GCP instances for each chatbot version (production, staging, prototype).
4. Knowledge Base Integration:
    - Maintain a Vector DB (Azure/AWS) for Retrieval-Augmented Generation (RAG) to keep responses aligned with updated marketplace content and policies.

### Version control & integration
- Source Control: Git + GitHub for managing chatbot code, prompts, and configurations.
- Branching Model:
    - Each new feature or update starts in its own branch.
    - Only merge into main when the branch has passed all automated tests and functions are stable.
- Instance Management: Each branch can deploy its own GCP instance for isolated testing before merging.

### Automated testing pipeline
- Test Storage: Maintain test-cases.json for structured test cases; optionally store in Google Sheets for easier updates by non-developers.
- Execution Flow:
    1. Python test runner fetches the latest test cases (via Sheets API or DB).
    2. Runs tests against the intended chatbot API endpoint.
    3. Collects raw results and stores them in a results database or sheet.
    4. Passes results to an LLM evaluator to check for expected elements and success criteria.
    5. Outputs scored results (percentage completion) and sends to stakeholders (Google Sheets + Email via SMTP/Twilio SendGrid).
- Automation: Run the pipeline as a scheduled GCP job or trigger it on pull requests.

### Deployment workflow for prompt updates
- Update prompt files or policy references in the backend branch.
- CI/CD pipeline spins up a `PROTOTYPE_VERSION_<number>` instance for each branch.
- Manually direct a portion of user traffic to the prototype instance (canary testing).
- Once validated, switch all production traffic to the new version.

### Rollback capabilities for failed updates
- Always keep at least two previous stable GCP instances running for instant rollback.
- Git rollback is straightforward—redeploy the last known stable branch if needed.
- This ensures minimal downtime in case of critical failures.

### Change approval process for policy updates
- Maintain an official private policy document in a single source of truth (PDF, Markdown, or TXT).
- Host it on an authentication-protected editing portal, with access limited to designated policy editors.
- Approval workflow:
    1. Policy editor submits proposed changes through the frontend portal
    2. Changes go to the relevant parties for review
    3. Once a stipulated number of authorized parties approve and digitally sign off, the updates can be done
    4. A record of each proposal, review, signature and update is stored with timestamps on the remote database for version history
    5. Approved version is stored
- Technical Update Steps (after approval):
    1. Tokenize and vectorize the new policy text.
    2. Push the embeddings to the Vector DB.
    3. Automatically refresh the {{POLICY_DOCUMENT}} variable in chatbot prompts for RAG access.