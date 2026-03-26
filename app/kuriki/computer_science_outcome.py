from dataclasses import dataclass

from app.kuriki.cluster import Cluster
from app.kuriki.status import Status
from app.kuriki.general_learning_outcome import GeneralLearningOutcome
from app.kuriki.outcome import Outcome


@dataclass(frozen=True)
class ComputerScienceOutcome(Outcome):
    cluster: Cluster
    general_learning_outcome: GeneralLearningOutcome  # These are letter codes
    status: Status

    def to_dict(self) -> dict:
        return {
            "outcome_id": self.outcome_id,
            "grade": self.grade,
            "specific_learning_outcome": self.specific_learning_outcome,
            "cluster": self.cluster.to_dict(),
            "general_learning_outcome": self.general_learning_outcome.to_dict(),
            "status": self.status.to_dict(),
        }
