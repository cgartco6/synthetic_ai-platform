from agents.strategic_agent import StrategicAgent
from agents.workflow_agent import WorkflowAgent
from agents.course_creator_agent import CourseCreatorAgent
from agents.content_agent import ContentAgent
from agents.assessment_agent import AssessmentAgent
from agents.validation_agent import ValidationAgent
from agents.teaching_agent import TeachingAgent

class Orchestrator:
    def __init__(self, memory):
        self.memory = memory
        self.agents = {
            "strategy": StrategicAgent(),
            "workflow": WorkflowAgent(),
            "creator": CourseCreatorAgent(),
            "content": ContentAgent(),
            "assessment": AssessmentAgent(),
            "validation": ValidationAgent(),
            "teaching": TeachingAgent()
        }

    def create_course(self, domain):
        plan = self.agents["strategy"].act(
            self.agents["strategy"].think(domain)
        )

        workflow = self.agents["workflow"].act(plan)

        syllabus = self.agents["creator"].act(workflow)

        lessons = self.agents["content"].act(syllabus)

        exams = self.agents["assessment"].act(lessons)

        validated = self.agents["validation"].act(lessons + exams)

        self.memory.save(domain, validated)

        return validated
