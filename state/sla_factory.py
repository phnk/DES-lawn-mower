from .sla import SLA

class SLAFactory:
    def __init__(self):
        self.i = 0

    def create_sla(self, service_level, target_grass_length, number_of_lawn_mowers):
    # id, service_level, target_grass_length
        sla = SLA(self.i, service_level, target_grass_length, number_of_lawn_mowers)
        self.i = self.i + 1
        return sla
