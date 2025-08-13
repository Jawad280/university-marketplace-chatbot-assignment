## Process Log (Informal)

### Prompt Design
- Go through the Anthropic Prompt engineering practices
- Figure out base layout of the prompt
- Define different sections within the system prompt -> thinking, regulations, safety
- Order the prompt tags in order of importance

### Golden Test Design
- 3 tests per topic
- Think of cases whereby the chatbot should use toolcalls implicitly
- Vary the testcases, however there might be some overlap in scenarios
- layout the expectations to be clear and succint
- Evaluation methods must be discussed as well -> use another llm to verify ? Manual verification ? 
- Score-based evaluation so that we can visually project and see the changes easily and pitch to other stakeholders for improvements etc
- Think of collecting real-life testcases:
    - Human moderators can mark some chats + Chats that have been automatically marked (due to escalations)
    - These chats will be converted into testcases without expected answers on google sheets
    - Human moderators will proceed to fill up the expectations and update them accordingly
    - Allows for robust testcases that are more niche !

### Automation & Update Process
- Git for main version control of the code
- Keep versions & new features as a new branch -> new branch spin a new instance on GCP ? 
- GCP is the main deployment for backend
    - Easy to rollback instances
    - Load balancing capabilties
    - Ease of setup compared to Azure
    - More configs available on the Cloud Engine API
- Google Sheets to update and keep test-cases as its easier to update by non-developers too (Human moderators)
- Policy Change & Authorization
    - Maybe add a docs-like frontend with OAuth
    - Give access to only those able to make changes to the policy
    - Proposal -> Verification + Review by others -> ONLY updates the policy IF at least 2 sign off
    - Updated policy is on database 
    - All the proposal and reviews are commited to the database with timestamps
    - Upon update, the vector db will have to vectorize the document (automated) & now the document fetched for RAG will be updated as well