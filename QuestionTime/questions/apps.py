from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    name = 'QuestionTime.questions'

    def ready(self):
        import QuestionTime.questions.signals