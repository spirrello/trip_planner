# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind.  Identify the specific outcome your tasks are aiming
  to achieve.
- Break down the outcome into actional tasks, assigning each task to the
  appropriate agent.
- Ensure tasks are descriptive, providing clear instructiosn and expected deliverables.

Goal:
- Develop a detailed iteinerary, including city selelction, attractions
  and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itinerary.

2. Task Breakdown: Divide the goals into smaller, manageable tasks that agents
   can execute.
    - Itinerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analyze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
- Use this template as a guide to define each task in your CrewAI application.
- This template helps ensure that each task is clearly defined, actionable and aligned with the specific.


Template:
-------------
def (task_name)(self, agent, [parameters]):
    return Task(
        description=dedent(
            f'''
        **Task** [Provide a concise name or summary of thet task.]
        **Description**: [Detailed description of what the agent is expected to do,
        including actionalable steps and expected output.]

        **Parameters**:
        - [Parameter 1]: [Description of parameter 1]
        - [Parameter 2]: [Description of parameter 2]

        **Note**: [Optional section for incentives or encouragement for high-quality
        work.  This can include a tip or commission for exceptional work.]
        '''
        ),
        expected_output="The expected output of the task",
        agent=agent,
    )

"""


class TravelDetails:
    def __init__(
        self,
        origin: str,
        cities: str,
        travel_dates: str,
        interests: str,
    ):
        self.origin = origin
        self.city = ""
        self.cities = cities
        self.travel_dates = travel_dates
        self.interests = interests


class TravelTasks:
    # Add this tip section always to your tasks as it helps align the goal.
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    # When definiting the description, it is important to be clear on what the final output should be.
    def plan_itinerary(self, agent, travel_plan: TravelDetails):
        return Task(
            description=dedent(
                f"""
                    **Task**: Develop a 7-Day Travel Itinerary
                    **Description**: Expand the city guide into a full  7-day travel
                    itinerary with detailed per-day plans, including weather forecasts,
                    places to eat, packing suggestions, and a budget breakdown.  You
                    MUST suggest actual places to visit, actual hostels to stay, and
                    actual restaurants to eat at.  This itinerary should cover all
                    aspects of the trip, from arrival to deparrture, integrating the
                    city guide information with practical travel logistics.

                    {self.__tip_section()}

                    **Parameters**:
                    - City: {travel_plan.city}
                    - Travel Date: {travel_plan.travel_dates}
                    - Interests: {travel_plan.interests}

                    **Note**: {self.__tip_section()}

                """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )

    def identify_city(self, agent, travel_plan: TravelDetails):
        return Task(
            description=dedent(
                f"""
                    **Task**: Identify The Best City For The Trip
                    **Description**: Analyze and pick the best city for the trip based
                    on specific criteria such as weather patterns, seasonal events and
                    travel costs.  This task involves comparing multiple cities,
                    considering factors like current weather conditions, upcoming
                    cultural or seasonal events, and overall travel expenses.  Your
                    final answer must be a detailed report on the chosen city and
                    including actual flight costs, weather forecast and attractions.

                    **Parameters**:
                    - Origin: {travel_plan.origin}
                    - Cities: {travel_plan.cities}
                    - Interests: {travel_plan.interests}
                    - Travel Date: {travel_plan.travel_dates}

                    **Note**: {self.__tip_section()}

                    Make sure to do something else.
                """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )

    def gather_city_info(self, agent, travel_plan: TravelDetails):
        return Task(
            description=dedent(
                f"""
                    **Task**: Gather In-depth City Guide Information
                    **Description**: Compile an in-depth guide for the selected city,
                    gathering information about key attractions, local customs, special
                    events and daily activity recommendations.  This guide should
                    provide a thorough overview of what the city has to offer, including
                    hidden gems, culstural hotspots, must-visit landmarks, weather
                    forecasts and high-level cost estimates.

                    **Parameters**:
                    - Origin: {travel_plan.origin}
                    - City: {travel_plan.city}
                    - Interests: {travel_plan.interests}
                    - Travel Date: {travel_plan.travel_dates}

                    **Note**: {self.__tip_section()}
                """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )
