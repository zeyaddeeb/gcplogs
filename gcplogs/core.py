import warnings

warnings.filterwarnings("ignore", message="_CLOUD_SDK_CREDENTIALS_WARNING")


class GCPLogs:
    def get_log_groups(self):
        return ["l1", "l2"]
