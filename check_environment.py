from envcollector import EnvCollector


class CheckEnvironment:

    def __init__(self,env):
        self.env = env

    def chk_supported_os(self):
        """ This checks for the supported OS against the mentioned int the Linux VDA docs"""
        SUPPORTED_OS = 0
        supported_vda = 0
        vda_version = self.env.get_vda_version()
        support_vda_version = ["7.15","7.16","7.17","7.18"]
        for i in support_vda_version:
            if  i in vda_version:
                print("VDA version is supported by this tool \n")
                supported_vda = 1

        if supported_vda == 0:
            print("VDA VERSION IS NOT SUPPORTED BY THIS TOOL. SO EXITING OUT THE CHECKS ")
            exit()

        if "7.15" in vda_version:
            supported_rhelcent_os = [
                "6.6","6.9","7.3"
            ]
            supported_ubuntu_os=[
                "16.0.4"
            ]
            supported_suse_os = [
                "11","12"
            ]
        elif "7.16" in vda_version:
            supported_rhelcent_os = [
                "6.8","6.9","7.3"
            ]
            supported_ubuntu_os=[
                "16.0.4"
            ]
            supported_suse_os = [
                "12"
            ]
        elif "7.17" in vda_version:

            supported_rhelcent_os = [
                "6.8","6.9","7.3"
            ]
            supported_ubuntu_os=[
                "16.0.4"
            ]
            supported_suse_os = [
                "12"
            ]
        elif "7.18" in vda_version:

            supported_rhelcent_os = [
                "6.8","6.9","7.4"
            ]
            supported_ubuntu_os=[
                "16.0.4"
            ]
            supported_suse_os = [
                "12"
            ]
        for i in supported_suse_os:
                if i in self.env.get_os():
                    print("OS version seems to be in supported list. Please crosss verify if",self.env.get_os(),"is in the supported list in https://docs.citrix.com/en-us/linux-virtual-delivery-agent/current-release/system-requirements.html" )
                    SUPPORTED_OS = 1
        for i in supported_rhelcent_os:
                if i in self.env.get_os():
                    print("OS version seems to be in supported list. Please crosss verify if",self.env.get_os(),"is in the supported list in https://docs.citrix.com/en-us/linux-virtual-delivery-agent/current-release/system-requirements.html" )
                    SUPPORTED_OS = 1
        for i in supported_ubuntu_os:
                if i in self.env.get_os():
                    print("OS version seems to be in supported list. Please crosss verify if", self.env.get_os(),"is in the supported list in https://docs.citrix.com/en-us/linux-virtual-delivery-agent/current-release/system-requirements.html")
                    SUPPORTED_OS = 1
        if SUPPORTED_OS == 0:
            print("WARNING : OS is not supported as per docs. Please reconfirm in corresponding linux vda documentation")

    def chk_supported_xorg(self):
    #    """Check for Supported Xorg version for the OS involved"""
        if "7.18" in self.env.get_vda_version():
            if "Red Hat Enterprise Linux Server release 7.4" in self.env.get_os():
                supported_xorg = 1.19
            elif "CentOS Linux release 7.4" in self.env.get_os():
                supported_xorg = 1.19

        if str(supported_xorg) in self.env.get_xorg():
            print("PASS: Xorg version is supported")
        else:
            print("WARNING : Not a supported version of Xorg. Please reconfirm from docs")