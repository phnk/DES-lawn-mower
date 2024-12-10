MAX_GRASS_LENGTH_VARIANCE = 2
MIN_GRASS_LENGTH_VARIANCE = 1/2
PAYMENT_STATUS_OPTIONS = ["PAYMENT_PENDING", "PAYMENT_COMPLETE", "PAYMENT_FAILED"]
STATUS_OPTIONS = ["NOT_STARTED", "ON_GOING", "COMPLETED", "FAILURE", "VIOLATION"]
SERVICE_LEVEL_OPTIONS = ["GOLD", "SILVER", "BRONZE", "IRON"]

class SLA:
    def __init__(self, id, service_level, target_grass_length, num_lawn_mowers):
        '''
        What does an SSL include?
        id
        sevice_level
        target grass length
        maximum grass length
        min grass length
        payment_status - PAYMENT_PENDING, PAYMENT_COMPLETE, PAYMENT_FAILED
        status - NOT_STARTED, ON_GOING, COMPLETED, FAILURE, VIOLATION
        number of lawn mowers
        '''
        self.id = id

        if service_level not in SERVICE_LEVEL_OPTIONS:
            raise Exception("service_level not in SERVICE_LEVEL_OPTIONS")
        self.service_level = service_level

        self.target_grass_length = target_grass_length
        self.max_grass_length = target_grass_length * MAX_GRASS_LENGTH_VARIANCE
        self.min_grass_length = target_grass_length * MIN_GRASS_LENGTH_VARIANCE

        # payment status is always PAYMENT_PENDING when its created
        self.payment_status = "PAYMENT_PENDING"
        # status is always NOT_STARTED when the SLA is created
        self.status = "NOT_STARTED"
        # number of lawn mowers needed to be free to start it
        self.required_mowers = num_lawn_mowers

    def change_payment_status(self, new_payment_status):
        if new_payment_status not in PAYMENT_STATUS_OPTIONS:
            raise Exception("new payment status not in PAYMENT_STATUS_OPTIONS")

        self.payment_status = new_payment_status


    def set_status(self, new_status):
        if new_status not in STATUS_OPTIONS:
            raise Exception("new status not in STATUS_OPTIONS")

        self.status = new_status

    def number_of_lawn_mowers(self):
        return self.required_mowers

    def complete_SLA(self):
        self.set_status("COMPLETED")
        released_mowers = self.required_mowers
        self.required_mowers = 0
        return released_mowers

