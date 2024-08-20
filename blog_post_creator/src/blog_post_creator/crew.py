from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FirecrawlScrapeWebsiteTool
from firecrawl import FirecrawlApp
from langchain_openai import ChatOpenAI

import os


@CrewBase
class BlogPostCreatorCrew():
    """BlogPostCreator crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'      

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[FirecrawlScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config['planner'],
            tools=[FirecrawlScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['planning_task'],
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
        )

    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'],
            output_file='blog_post.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the BlogPostCreator crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            output_log_file="new-logs.txt",
            planning=True,
            planning_llm=ChatOpenAI(model="gpt-4o")
        )