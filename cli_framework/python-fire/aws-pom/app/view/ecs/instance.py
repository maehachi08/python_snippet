from prettytable import PrettyTable


class EcsInstanceView():
    def instance(self, instance_info: list):
        x = PrettyTable()
        x.field_names = ['InstanceID', 'IpAddress']

        for i in instance_info:
            x.add_row([i['instance_id'], i['instance_ip']])
        return x.get_string()

