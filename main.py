from textwrap import dedent

from crewai import Crew
from dotenv import load_dotenv

from agents import TravelAgents
from tasks import TravelDetails, TravelTasks

load_dotenv()

# search_tool = DuckDuckGoSearchRun()

# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class TripCrew:
    def __init__(self, travel_details: TravelDetails):
        self.travel_details = travel_details

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.travel_details,
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.travel_details,
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.travel_details,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print("-------------------------------")
    origin = input(dedent("""From where will you be traveling from? """))
    cities = input(
        dedent("""Enter the cities you are interested in, separated by commas: """)
    )
    travel_dates = input(dedent("""Enter the travel dates: """))
    interests = input(dedent("""Enter your interests, separated by commas: """))

    trip_details = TravelDetails(origin, cities, travel_dates, interests)
    trip_crew = TripCrew(trip_details)

    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is you Trip Plan")
    print("########################\n")
    print(result)
