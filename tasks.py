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

2. Task Breakdown: Divide the goals into smaller, manageable tasks that agents can execute.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
- Use this template as a guide to define each task in your CrewAI application.
- This template helps ensure that each task is clearly defined, actionable and aligned with the specific.

"""


class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
            Do something as part of task 1

            {self.__tip_section()}

            Make sure to use the most recent data as possible.

            Use this variable: {var1}
            And also this variable: {var2}
        """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )

    def task_2_name(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from task 1 and do something with it.

            {self.__tip_section()}

            Make sure to do something else.
        """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )
