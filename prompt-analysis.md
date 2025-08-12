## PROMPT ANALYSIS

Common Best practices for prompt engineering :

1. Clear & Direct
    - Contextual information is key -> what the results will be used for, what the output is meant for, workflow, end goal
    - Specificity -> ONLY & NOTHING ELSE
    - Sequential instructions

2. Multishot (use examples)
    - `<example>` tags can be used to provide 2/3 shots of examples
    - Relevant examples + Diverse -> edge case covering etc

3. Chain of Thought 
    - `<thinking>` tags can be used 
    - Allow the thinking to take place for more complex or rigid situations to enforce a certain rule
    - Go through a series of thought process checks before passing out information
    - Mimic an actual assistant/moderator

4. XML tags
    - Structured prompting -> `<instructions>, <example>, <formatting>, <thinking>`
    - Use nested tags for hierarchical content
    - Formatting a consistent response style

5. Role & System prompts
    - Role prompting improves accuracy and the tone of the chatbot
    - Defining its role can allow more focus on the regulations it is bounded by

6. Prefill responses
    - Provide a desired initial text for the chatbot to begin with 
    - Depends on scenarios

7. Long Context tips
    - `<document>` & `<source>` tags to wrap documents in the prompt which have larger context
    ```xml
    <documents>
        <document index="1">
            <source>user_sent_image.jpg</source>
            <document_content>
                {{USER_SENT_IMAGE}}
            </document_content>
        </document>
    </documents>
    ```
8. Chain complex prompts