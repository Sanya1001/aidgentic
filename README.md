# Sync
Always in sync for humanity

Introducing **Sync**: a robust multi-agent framework designed to streamline disaster response and resource allocation. 

With our intuitive web app, citizens and aid workers can easily submit _real-time reports_, which our regional reporting agent aggregates and analyzes. Sync then generates comprehensive reports and efficiently requests resources from appropriate NGOs based on recommendations from expert agents, ensuring timely and effective aid distribution. **Transform chaos into coordinated action with Sync — where every report makes a difference**.

## Motivation

The motivation for creating Sync stems from the pressing need to improve disaster response efficiency. We were inspired in particular by our awareness of ongoing wildfire situations in California. Research highlights that delays in disaster response are often due to fragmented communication, inefficient data aggregation, and slow resource allocation. Sync addresses these challenges by providing a seamless platform where real-time reports from citizens and aid workers are quickly aggregated and analyzed by intelligent agents. This enables a decentralized model of decision-making that is faster and more accurate. Our goal is to reduce response times, enhance coordination, and ultimately save lives and property in critical disaster scenarios, with a focus on the ongoing climate crisis. Our product also extends the reach of relief agencies by alerting them of relevant disaster scenes which fall in their area of practice, all without having to directly hire ground-level reporters and data collectors

## Challenges and Takeaways

- **Real-time Synchronization Across Multiple Devices**: Ensuring that data updates and reports are synchronized in real-time across multiple devices required robust backend-frontend architecture and efficient data handling techniques
- **Structured Output from agents for cost projections and optimal NGO routing**: Developing a multi-agent system that can communicate and share information effectively was a challenging but rewarding experience. We also had to ensure that agent outputs were consistent and structured enough to be used by other agents and to be served to the frontend.

## Multi-Agent Architecture
- Our novel multi agent system is represented by a state graph. Each node in the graph represents an expert agent. Our entry point nodes are agents who represent humanitarian report aggregators for specific regions. For example, we have one agent who oversees humanitarian crisis reports for the state of California. These regional reporters send a briefing of relevant issues to a cost and resource estimation agent, whose job is to determine which humanitarian resources are needed for the given situation. For example, the resource estimation node will request the appropriate number of fire fighters in response to a forest fire. The requests are then routed to the correct NGOs for the task by an NGO communicator/routing agent.

![Untitled-2024-03-06-2342](https://github.com/Sanya1001/aidgentic/assets/23709618/5544d4b5-ae69-4c44-a289-e9a0c49980d1)

## Techstack
LangChain and LangGraph were used to implement the multi agent system. Each agent was represented by individually tuned Anthropic Claude 3 Opus models.

NextJS and Tailwind were used to implement the front end and FastAPI was used to integrate with our backend agent sytem.
  
![Comparison](https://github.com/Sanya1001/aidgentic/blob/main/Sync/Slide12.jpg)

## Developers

[@uzairname](https://www.github.com/uzairname)
[@sanya1001](https://www.github.com/sanya1001)
[@sidb70](https://www.github.com/sidb70)



