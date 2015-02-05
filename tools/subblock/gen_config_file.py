#!/usr/bin/env python2.7

import os
from jinja2 import Environment, FileSystemLoader
import socket
from random import randint as ri

try:
   template_dir=os.environ['FW_DIR']
   template_dir=template_dir+'/share/cobalt/etc/'
except KeyError:
    template_dir=os.path.realpath(__file__)
    template_dir=template_dir.split("bin")[0]
    template_dir=template_dir+'/share/cobalt/etc/'
except:
    template_dir='/projects/JCESR/fireworks/share/cobalt/etc/'

conf_vars={}
conf_vars.update(os.environ)

def get_calced_cobalt_vars():
    part_name=conf_vars['COBALT_PARTNAME']
    job_size=part_name.split('-')[-1]
    return {'max_jobsize':job_size}

def gen_password():
    """Generate a weak password"""
    def gc(x1,x2):
        return chr(ri(x1,x2))
    def gi(i1,i2):
        return str(ri(i1,i2))
    password=[[gi(1,256),gc(48,57),gc(65,90),gc(97,122)][ri(0,3)] for i in range(ri(8,12))]
    password=''.join(password)
    return {'password':password}

def get_net_cfg():
    """This isn't the safest way of doing this, but the port returned should
    be free again in a minute"""
    host_name=socket.gethostname()
    ip_address=socket.gethostbyname(host_name)
    local_socket=socket.socket()
    local_socket.bind((host_name,0))
    local_port=local_socket.getsockname()[1]
    local_socket.close()
    return {'srv_host_name':host_name,'srv_ip_address':ip_address,'srv_local_port':local_port}

def gen_cobalt_cfg():
    fs_loader = FileSystemLoader(template_dir)
    env = Environment(loader=fs_loader)
    template = env.get_template('cobalt.conf.tmpl')
    config=template.render(**conf_vars)
    return config    

def main():
    net_cfg={}
    try:
        components=conf_vars['COBALT_COMPONENTS']
        for component in components.split():
            net_cfg[component]=get_net_cfg()
        conf_vars.update(net_cfg)
        cobalt_calcd_vars=get_calced_cobalt_vars()
        conf_vars.update(cobalt_calcd_vars)
        password_cfg=gen_password()
        conf_vars.update(password_cfg)
        cobalt_config=gen_cobalt_cfg()
        run_cfg_name=conf_vars['COBALT_CONFIG_FILES']
        run_cfg=open(run_cfg_name,'w')
        run_cfg.write(cobalt_config)
        run_cfg.close()
    except  (IOError, OSError) as e:
        print ('Failed to generate cobalt.conf: {}.'.format(e))
        exit(1)

if __name__=='__main__':
    main()
