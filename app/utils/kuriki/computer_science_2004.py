from app.kuriki.cluster import Cluster
from app.kuriki.clusters import Clusters
from app.kuriki.computer_science_outcome import ComputerScienceOutcome
from app.kuriki.general_learning_outcome import GeneralLearningOutcome
from app.kuriki.general_learning_outcomes import GeneralLearningOutcomes
from app.kuriki.science_outcome import ScienceOutcome
from app.kuriki.status import Status


class ComputerScience2004Cache:
    _loaded = False
    clusters: Clusters = Clusters()
    general_learning_outcomes: GeneralLearningOutcomes = GeneralLearningOutcomes()
    outcomes: list[ComputerScienceOutcome] = []
    cache: dict[str, dict[str, dict[str, str]]] = {}

    @classmethod
    def load(cls, db_cursor, table_name="computer_science_2004"):
        if cls._loaded:
            return

        db_cursor.execute(f"SELECT grade, cluster, title, teacher_notes FROM {table_name}_clusters")
        cls.clusters._clusters = [Cluster(*row) for row in db_cursor.fetchall()]

        db_cursor.execute(f"SELECT code, description FROM {table_name}_general_learning_outcomes")
        cls.general_learning_outcomes._general_learning_outcomes = [GeneralLearningOutcome(*row) for row in db_cursor.fetchall()]

        db_cursor.execute(f"SELECT outcome_id, grade, cluster, general_learning_outcome, specific_learning_outcome, status FROM {table_name}_curriculum")

        for row in db_cursor.fetchall():
            print(row)
            cluster = next((c for c in cls.clusters if c.get_id() == f"{row[1]}.{row[2]}"))
            general_learning_outcome = GeneralLearningOutcome(code="", description="")
            for general_learning_outcome in cls.general_learning_outcomes:
                if general_learning_outcome.code == row[3]:
                    general_learning_outcome = general_learning_outcome
                    break

            outcome = ComputerScienceOutcome(
                outcome_id=row[0],
                grade=row[1],
                specific_learning_outcome=row[4],
                cluster=cluster,
                general_learning_outcome=general_learning_outcome,
                status=Status(state=row[5]),
            )

            cls.outcomes.append(outcome)
            cls.cache[row[0]] = outcome.to_dict()

        cls._loaded = True
