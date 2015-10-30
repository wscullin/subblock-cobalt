#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader
import socket
from random import randint as ri
import functools


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

def block_size(block_name):
    return(int(block_name.split('-')[-1]))

def block_size_compare(a,b):
    return block_size(a)-block_size(b)
        
def gen_subblock_config():

    try:
        minsize=int(conf_vars['COBALT_SUBLOCK_MINSIZE'])
    except:
        minsize=1

    try:
        subblock_names=conf_vars['COBALT_PARTNAME_CHILDREN']
        subblock_names=subblock_names.split(':')[-1].replace(' ','')
        print subblock_names
        # The minimum valid block length is 15 chars
        if len(subblock_names) >= 15:
            subblock_names=subblock_names.split(',')
            subblock_names.sort(key=functools.cmp_to_key(block_size_compare))
            try:
                smallest_size=conf_vars['COBALT_SUBLOCK_PARENTSIZE']
            except KeyError:
                smallest_size=block_size(subblock_names[0])
            if smallest_size >= 32:
                smallest_size=str(smallest_size)
            else:
                smallest_size='128'
            sb=['%s:%d' %(sb,minsize) for sb in subblock_names if sb.endswith(smallest_size)]
            sb=','.join(sb)
        else:
            print "Setting sublock target to %s" %(conf_vars['COBALT_PARTNAME'])
            sb='%s:%d' %(conf_vars['COBALT_PARTNAME'],minsize)
    except KeyError:
        print "Config generator defaulting to COBALT_PARTNAME"
        sb='%s:%d' %(conf_vars['COBALT_PARTNAME'],minsize)
 
    return {'subblock_config':sb}    

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
        subblock_cfg=gen_subblock_config()
        conf_vars.update(subblock_cfg)
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
