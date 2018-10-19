#Author = Antony Peter
#Creation date = 1/22/2018
# Description = This is the main entry for the lvdanalyze script

from os.path import dirname, isdir
import os
import zipfile
from time import sleep
import tarfile
import shutil

from envcollector import EnvCollector
from check_environment import CheckEnvironment
from registeration import Register
# function to extract the zip file to the targetdir
def extract(file):
    if file.endswith('.zip'):
         with zipfile.ZipFile(file,'r') as zip_ref:
            zip_ref.extractall()
    elif file.endswith('.bz2'):
        bz2dir = os.path.join(os.getcwd(), file.split('.')[0])
        if isdir(bz2dir):
            pass
        else:
            with tarfile.open(file,"r:bz2") as tar:
                    tar.extractall()
    elif file.endswith('.tar'):
        tardir = os.path.join(os.getcwd(), file.split('.')[0])
        if isdir(tardir):
            pass
        else:
            with tarfile.open(file, "r:tar") as tar:
                tar.extractall()
try:

    zip_file_location = input("Enter the absolute path where xdlcollect.zip is downloaded \n")

    filelist = zip_file_location.split('\\')

    filename=filelist[-1]
    script_dir = os.getcwd()

    target_dir =  dirname(zip_file_location)

    #change to the directory where file is downloaded
    os.chdir(target_dir)

    extract(filename)

    #change path to extracted directory

    created_dir=filename.split('.')[0]
    os.chdir(created_dir)



# #get environment details for the customer environment
# get_environment_details()
#
    env = EnvCollector(os.getcwd())

    print('*****************************************LVDA Environment Details************************************************')

    print('\n')

    print('|{:<25}| {:>3}'.format("VDA Agent version",env.get_vda_version()))
    print('|{:<25}| {:>3}'.format("List of DDC", env.get_list_ddc()))
    print('|{:<25}| {:>3}'.format("Registered DDC", env.get_register_ddc()))
    print('|{:<25}| {:>3}'.format("Brokering Mode",env.get_brokeringmode()))
    print('|{:<25}| {:>3}'.format("IPV6 Registration status",env.get_ipv6_registration()))


    print('\n')
    print('*****************************************AD Integration Details************************************************')

    print('\n')

    print('|{:<25}| {:>3}'.format("Ldap Servers:Port",env.get_ldap_servers()))
    print('|{:<25}| {:>3}'.format("Domain join Method",env.get_join_method()))
    print('|{:<25}| {:>3}'.format("Linux VDA Machine SID",env.get_machine_sid()))

    #getting kerberos information
    print('{:^50}'.format('Kerberos Configuration'))

    conffile, keytabfile, cachefile = env.get_kerberos_configuration()
    print('|{:<25}| {:>3}'.format("Kerb Conf file", conffile))
    print('|{:<25}| {:>3}'.format("Kerb Ticket file", keytabfile))
    print('|{:<25}| {:>3}'.format("kerb Cache file", cachefile))

    print('*****************************************LVDA Os Details************************************************')
    env.get_os_details()
    #need to fix the xorg for all os to enable this
    #print('|{:<25}| {:>3}'.format("Xorg version", env.get_xorg()))

    #Check environment details
    print('*****************************************Checking the xdlcollect for supported configuration***************************************')
    chk = CheckEnvironment(env)
    chk.chk_supported_os()
    print("\n")
    #chk.chk_supported_xorg()

except Exception as err:
    print(err)
    print('Please enter the Absolute path to the xdlcollect.zip file.')

print("***********************************************************************************************************************************")
user_input = int(input("Is it a registration problem or launch failure problem that you are looking to solve ? If it's a registration issue press 1 else press 2 \n \
[1] -------------- > Registration issue. Please ensure you have collected logs after enabling verbose logs for vda -- https://support.citrix.com/article/CTX220130  \n \
[2] -------------- > Launch issue. Please ensure you have collected logs after enabling verbose logs for hdx using setlog command -- https://support.citrix.com/article/CTX220130 \n \
WAITING FOR YOUR INPUT FOR FURTHER PROCESSING OF LOGS \n"))

if user_input == 1:
    print( "*************************************Performing Analysis of Registration Issue**************************************************************")
    print("{:<7} | {:^31} | {:^60} | {:^30} | {:^30}".format('ISSUE COUNT', 'PATTERN MATCHED', 'ISSUE DESC', 'SOLUTION','CASE #'))
    reg = Register(os.getcwd())
    reg.read_log()
    reg.search_issue(script_dir)
else:
    pass

# while True:
#     sleep(1)
