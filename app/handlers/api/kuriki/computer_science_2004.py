from app.handlers.kuriki import KurikiBaseHandler
from app.utils.kuriki.computer_science_2004 import ComputerScience2004Cache


class KurikiComputerScienceAPIHandler(KurikiBaseHandler):
    def initialize(self):
        super().initialize()
        ComputerScience2004Cache.load(self.cur)


class KurikiComputerScienceClustersAPIHandler(KurikiComputerScienceAPIHandler):
    def get(self):
        try:
            self.write(
                {
                    "status": "success",
                    "data": ComputerScience2004Cache.clusters.to_dict(),
                }
            )
        except Exception as e:
            self.write_error_response(e)


class KurikiComputerScienceGeneralLearningOutcomesAPIHandler(KurikiComputerScienceAPIHandler):
    def get(self):
        try:
            self.write(
                {
                    "status": "success",
                    "data": ComputerScience2004Cache.general_learning_outcomes.to_dict(),
                }
            )
        except Exception as e:
            self.write_error_response(e)


class KurikiComputerScienceOutcomesAPIHandler(KurikiComputerScienceAPIHandler):
    def get(self):
        try:
            outcome_id = self.get_argument("id", None)

            if outcome_id:
                if result := ComputerScience2004Cache.cache.get(outcome_id):
                    self.write({"status": "success", "data": result})
                else:
                    self.set_status(404)
                    self.write({"status": "error", "message": "Outcome not found"})
            else:
                self.write(
                    {
                        "status": "success",
                        "data": ComputerScience2004Cache.cache,
                    }
                )
        except Exception as e:
            self.write_error_response(e)

    @staticmethod
    def _get_outcome(outcome_id: str):
        if result := ComputerScience2004Cache.cache.get(outcome_id):
            return result
        else:
            return None
