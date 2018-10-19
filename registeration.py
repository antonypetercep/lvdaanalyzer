from os.path import join
import urllib.request as req

class Register:

    def __init__(self, root_dir):

        self.rootxdldir = root_dir
        self.log_dir = join(self.rootxdldir, 'xdl', 'logs', 'var_xdl')
        self.vda_log = join(self.log_dir, 'vda.log')
        self.out_log = join(self.log_dir, 'vda_out.log')
        self.start = "Citrix Broker Agent - Start"
        self.line_count = 0
        self.start_line = 0
        self.x = 0
        self.regissues_url = 'https://raw.githubusercontent.com/antonypetercep/lvdaanalyzer/master/reg_issues'

    def read_log(self):
        with open(self.vda_log, 'r') as f:
            for line in f:
                if self.start in line:
                    self.start_line = self.line_count
                self.line_count += 1
        with open(self.vda_log,'r') as new:
            with open(self.out_log,'w') as o:
                for ln in new:
                    if self.x >= self.start_line:
                        o.write(ln)
                    self.x += 1
    def download_reg_issues(self,dir):
        """This will download """
        req.urlretrieve(self.regissues_url, join(dir,'reg_issues'))

    def search_issue(self,scpt_dir):
        self.download_reg_issues(scpt_dir)
        with open(join(scpt_dir,'reg_issues'),'r') as f:
                lst = f.readlines()
                lst_stripped = []
                lst_pattern = []
                for item in lst:
                      lst_stripped.append(item.strip('\n'))
                      lst_pattern.append(item.split(',')[0])
                try:
                    with open(self.out_log,'r') as log:
                        count = 0
                        HIT = 0
                        for line in log:
                            #print(line)
                            for pattern in lst_pattern:
                                #print(pattern)
                                if pattern in line:
                                    count += 1
                                    HIT = 1
                                    for item in lst_stripped:
                                        if pattern in item:
                                            print("{:<11} | {} | {} | {} | {}".format(count,pattern,item.split(',')[1],item.split(',')[2],item.split(',')[3]))
                                else:
                                    pass
                        if not HIT:
                            print("No Known Registration Issues Found as per Database. Refer --> https://www.citrix.com/blogs/2015/10/21/troubleshooting-linux-vda-registration-issues/ for troubleshooting")
                except Exception as err:
                    print(err)
