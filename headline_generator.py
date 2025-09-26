import random

class HeadlineGenerator:
    """
    A simple Python-based tool to generate synthetic headlines
    for experimentation and automation tasks.
    """

    def __init__(self):
        # Word banks (you can expand these)
        self.subjects = [
            "AI system", "Government", "Startup", "Research team",
            "Tech giant", "University", "Healthcare sector"
        ]
        self.verbs = [
            "launches", "develops", "invests in", "announces",
            "criticizes", "supports", "plans"
        ]
        self.objects = [
            "new policy", "robot assistant", "climate initiative",
            "smart device", "education program", "global project"
        ]
        self.extras = [
            "to boost innovation", "amid rising demand",
            "to cut costs", "for sustainable growth",
            "in record time", "to tackle challenges"
        ]

    def generate_headline(self):
        """Generate a random synthetic headline."""
        subject = random.choice(self.subjects)
        verb = random.choice(self.verbs)
        obj = random.choice(self.objects)
        extra = random.choice(self.extras)

        return f"{subject} {verb} {obj} {extra}"
