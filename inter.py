from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs
import sys 
#import  ipdb
config_file = sys.argv[1]
nr = InitNornir(config_file)
def basicconf(task):
    r=task.run(task=template_file,template="inter.j2",path=f"templates/")
    output=r.result
    send=output.splitlines()
    task.run(task=send_configs, configs=send)
def main():
        interface= nr.run(task=basicconf)
        print_result(interface)
if __name__ == '__main__':
        main()

