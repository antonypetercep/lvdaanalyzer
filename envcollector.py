from os.path import join
import re
class EnvCollector:

    def __init__(self,directory_path):
        self.dir_path = directory_path
        self.CTX_REG_DUMP = join(self.dir_path, 'xdl', 'ctxreg.dump')
        self.release_file = join(self.dir_path, 'system', 'release')
        self.sysinfo = join(self.dir_path, 'system', 'sysinfo')
        self.resolv = join(self.dir_path, 'system', 'resolv.conf')
        self.rpm_file = join(self.dir_path,'system','RPMs')

    def content_fetcher(self,keywork_to_match):
        with open(self.CTX_REG_DUMP, 'r') as regfile:
            for line in regfile:
                if keywork_to_match in line:
                    second_part = line.partition('-d')[2]
                    if second_part:
                            m = re.search('["].*["]', second_part)
                            return m.group()

    def get_list_ddc(self):
        return self.content_fetcher('ListOfDDCs')

    def get_vda_version(self):
        return self.content_fetcher('Citrix Virtual Desktop Agent')

    def get_join_method(self):
        return self.content_fetcher('DomainJoinMethod')

    def get_machine_sid(self):
        return self.content_fetcher('ComputerSIDForPolicy')
    def get_ipv6_registration(self):
        value = self.content_fetcher('ForceIpv6Registration').strip('\"')
        if value == '0x00000000':
            return 'Disabled'
        else:
            return 'Enabled'
    def get_kerberos_configuration(self):
        kerb_conf_file = self.content_fetcher('Krb5Conf')
        kerb_keytab_file = self.content_fetcher('Krb5Keytab')
        kerb_cache_file = self.content_fetcher('Krb5TicketCache')
        return kerb_conf_file, kerb_keytab_file, kerb_cache_file
    def get_ldap_servers(self):
        if self.content_fetcher('ListOfLDAPServers') != '""':
            return self.content_fetcher('ListOfLDAPServers')
        else:
            return self.content_fetcher('ListOfLDAPServersForPolicy')
    def get_register_ddc(self):
        return self.content_fetcher('RegisteredDdcFqdn')
    def get_brokeringmode(self):
        return self.content_fetcher('BrokeredSessionMode')
    def get_os_details(self):
        for line in open(self.release_file):
            if 'Description'  in line:
                os_version = line.split(':')[1].lstrip()
                print(os_version,end='')
        for line in open(self.sysinfo):
            if 'Hostname - Full:' in line:
                print(line, end='')
        for line in open(self.resolv):
            if 'nameserver' in  line:
                print(line, end='')
    def get_os(self):
        for line in open(self.release_file):
            if 'Description'  in line:
                os_version = line.split(':')[1].lstrip()
                return os_version
    def get_xorg(self):
        for line in open(self.rpm_file):
            if "xorg-x11-server-Xorg" in line:
                return line