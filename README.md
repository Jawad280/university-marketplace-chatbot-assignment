## Introduction & Overview
Designing a chatbot for a university marketplace platform where students can - buy, sell & trade items - within campus community.
Chatbot needs to help users:
- Navigate Platform
- Resolve common issues
- Enforce community guidelines
- Escalate complex problems to human moderators

## Instructions for reviewing each component
1. Prompt Design & Engineering
    - `prompt.md` - A comprehensive system prompt with clear structure
    - `prompt-analysis.md` - Analysis of prompt design
2. Golden Test Design
    - `test-cases.json` - 15 test cases in structured JSON format
    - `testing-framework.md` - Documentation of testing approach
3. Automation & Update Process
    - `update-process.md` - Process documentation with workflow diagram
    - `automation-concept.py` - Basic code structure
4. Marketplace Domain Knowledge
    - `marketplace-insights.md` - Brief analysis of key chatbot requirements

## Assumptions made about university marketplace
- The platform is exclusive to verified university students, ensuring a closed community.
- Transactions are peer-to-peer; the platform and chatbot do not directly process payments.
- Integration with university systems (email verification, OAuth) is available for user authentication.
- Users have varying levels of technical proficiency but expect quick and clear assistance.
- The marketplace strictly prohibits the sale of plagiarized academic content and unsafe goods.

## Time breakdown of effort allocation
|**Component**|**Time Allocation**|
|---------|---------------|
|Overview| 15 mins|
|Prompt Design & Engineering| ~40 mins|
|Golden Test Design| ~20 mins|
|Automation & Update Process| ~45 mins|
|Marketplace Domain Knowledge| ~15 mins|

## Next steps if this were a real project
1. This proposal primarily addresses prompt engineering. To build a truly powerful and efficient chatbot, it’s essential to integrate as many tool calls as possible — beyond simple ones touched on here. Through extensive prototyping and testing, we can design complex tool calls that enhance the chatbot’s contextual understanding and functionality.

2. Retrieval-Augmented Generation (RAG) techniques can be expanded to include re-ranking and feeding in critical documents like FAQs, guidelines, and university policies, enabling the bot to provide accurate, up-to-date answers and reduce hallucinations.

3. Introducing agentic methods with multiple LLMs — where one model verifies or refines the output of another — can improve reliability and reduce errors.

4. Finally, benchmarking various models through real user A/B testing, especially focusing on the chatbot’s ability to politely de-escalate disputes, will help identify the most human-like and effective solution.

## Personal Reflection on most challenging component
Prompt engineering is inherently iterative and reactive, as there is no definitive formula for crafting the perfect prompt. It demands extensive testing and fine-tuning, making my current approach a baseline to be further refined through experimentation and incorporation of advanced prompt engineering techniques.

That said, the most complex and demanding aspect was designing the automation and update process. This area involves intricate system design with multiple interconnected components—backend infrastructure, relational and vector databases, authorized policy updates, and more. Ensuring seamless coordination and a reliable workflow is critical, and debugging such a distributed system presents significant challenges.

Developing a foundational workflow while considering all available resources was an intense yet rewarding exercise. Ultimately, seeing these diverse components integrate effectively to deliver the intended functionality is highly satisfying.

## Three alternative approaches considered and why they were rejected
1. Topic-based Chatbot
    - Implement a chatbot that guides users through predefined topics and common FAQs in a conversational format
    - Users navigate through structured topics to find relevant answers
    - Rejected: This approach is overly simplistic, lacks flexibility to handle diverse queries, and cannot facilitate escalation to human moderators when needed.

2. GPT wrapper with Minimal Prompting
    - Use a straightforward system prompt such as: “You are the official ABC University Marketplace Support Admin. Assist users with any queries about buying, selling, or navigating the app.”
    - Rejected: This method risks frequent hallucinations and provides insufficient domain-specific knowledge about the university marketplace, leading to inaccurate or unhelpful responses

3. Simple Monolithic Backend with Manual Updates
    - Maintain a straightforward backend with manual code updates for chatbot functionality
    - This allows tight control and potentially easier debugging compared to fully automated workflows
    - Rejected: Although easier initially, this approach does not scale well, becomes tedious with frequent updates, and lacks modularity, making onboarding new developers and long-term maintenance challenging

## My experience with university marketplaces (Buyer/Seller perspective)
In my first year, I co-developed a university marketplace app with a friend. The biggest challenge was acquiring users, as existing platforms like Carousell and Telegram groups dominated with their ease of use and community trust. Telegram groups particularly thrived due to their tight-knit community feel within dorms, fostering trust and accountability — users treated transactions like borrowing from friends rather than strangers.

Carousell, while less community-focused, offered a wider product range. I primarily used these channels during emergencies (e.g., last-minute textbook needs, urgent laptop charger), highlighting the importance of trust and convenience for student users.