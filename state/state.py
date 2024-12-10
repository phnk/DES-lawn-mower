from .sla_factory import SLAFactory
import random

MAX_SLA_RNG = 30
MAX_PAY_RNG = 30
MAX_COMPLETE_TIME = 30

class State:
    def __init__(self, seed, number_of_mowers, number_of_techs, p_violation, c_min, c_max, t_min, t_max, runtime):
        """
        what do we need to initiate with arguments?
        * seed
        * number of lawn mowers
        * number of technicians
        * violation probaility
        * number of customers
        * SLAs
        * lower bound for cutting the grass
        * upper bound for cutting the grass
        * speed of new lawning assigments
        * lawn mower allocation

        extra init that are always the same
        * all the factories
        * 
        """
        self.seed = seed
        self.max_number_of_mowers = number_of_mowers
        self.available_number_of_mowers = number_of_mowers
        self.number_of_techs = number_of_techs
        self.p_violation = p_violation
        self.c_min = c_min
        self.c_max = c_max
        self.t_min = t_min
        self.t_max = t_max
        self.running = True
        self.runtime = runtime
        self.time = 0

        self.sla_factory = SLAFactory()
        self.sla_list = []
        self.sla_log = []

        self.seed_rng(seed)

    def is_running(self):
        return self.running

    def stop_sim(self):
        self.running = False

    def get_SLA(self):
        new_sla = self.sla_factory.create_sla("GOLD", 3, self.max_number_of_mowers)
        self.sla_list.append(new_sla)
        # log somehow
        # self.sla_log.append(...)

        return new_sla.id

    def get_SLA_list(self, id):
        if id > len(self.sla_list):
            raise Exception("SLA id used is larger than the SLA list length in state")
        return self.sla_list[id]


    def take_mowers(self, num_mowers):
        if self.available_number_of_mowers < num_mowers:
            # TODO(carl): what do we do when we can't create the service? wait?
            return False
        else:
            self.available_number_of_mowers = self.available_number_of_mowers - num_mowers
            return True

    def return_mowers(self, num_mowers):
        if self.max_number_of_mowers < self.available_number_of_mowers + num_mowers:
            raise Exception("Max number of mowers is below the number of available mowers, we created mowers out of thin air")

        self.available_number_of_mowers += num_mowers

    def get_violation_rng(self):
        if random.uniform(0, 1) < self.p_violation:
            return True
        else:
            return False

    def get_pay_time(self):
        return random.uniform(0.5, 1) * MAX_PAY_RNG

    def get_next_SLA_time(self):
        return random.uniform(0.5, 1) * MAX_SLA_RNG

    def get_complete_time(self):
        return random.uniform(0.5, 1) * MAX_COMPLETE_TIME

    def get_runtime(self):
        return self.runtime

    def get_time(self):
        return self.time

    def update_time(self, ts):
        self.time += ts

    def seed_rng(self, seed):
        random.seed(seed)
