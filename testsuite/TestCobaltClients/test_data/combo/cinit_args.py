import time
import pwd
import os
"""
This module is use for generating combo cobalt client commands on a Brooklyn or real system
"""
test_argslist = [
    {"tc_name" : "delete_partions"                     , "command" : "partadm", "args" : "-d '*'"},
    {"tc_name" : "add_partition_ANL_R00_R01_2048"      , "command" : "partadm", "args" : "-a ANL-R00-R01-2048"},
    {"tc_name" : "enable_partition_ANL_R00_R01_2048"   , "command" : "partadm", "args" : "--enable ANL-R00-R01-2048"},
    {"tc_name" : "activate_partition_ANL_R00_R01_2048" , "command" : "partadm", "args" : "--activate ANL-R00-R01-2048"},
    {"tc_name" : "add_partition_ANL_R00_1024"          , "command" : "partadm", "args" : "-a ANL-R00-1024"},
    {"tc_name" : "enable_partition_ANL_R00_1024"       , "command" : "partadm", "args" : "--enable ANL-R00-1024"},
    {"tc_name" : "activate_partition_ANL_R00_1024"     , "command" : "partadm", "args" : "--activate ANL-R00-1024"},
    {"tc_name" : "add_partition_ANL_R01_1024"          , "command" : "partadm", "args" : "-a ANL-R01-1024"},
    {"tc_name" : "enable_partition_ANL_R01_1024"       , "command" : "partadm", "args" : "--enable ANL-R01-1024"},
    {"tc_name" : "activate_partition_ANL_R01_1024"     , "command" : "partadm", "args" : "--activate ANL-R01-1024"},
    {"tc_name" : "add_partition_ANL_R00_M0_512"        , "command" : "partadm", "args" : "-a ANL-R00-M0-512"},
    {"tc_name" : "enable_partition_ANL_R00_M0_512"     , "command" : "partadm", "args" : "--enable ANL-R00-M0-512"},
    {"tc_name" : "activate_partition_ANL_R00_M0_512"   , "command" : "partadm", "args" : "--activate ANL-R00-M0-512"},
    {"tc_name" : "add_partition_ANL_R00_M1_512"        , "command" : "partadm", "args" : "-a ANL-R00-M1-512"},
    {"tc_name" : "enable_partition_ANL_R00_M1_512"     , "command" : "partadm", "args" : "--enable ANL-R00-M1-512"},
    {"tc_name" : "activate_partition_ANL_R00_M1_512"   , "command" : "partadm", "args" : "--activate ANL-R00-M1-512"},
    {"tc_name" : "add_partition_ANL_R01_M0_512"        , "command" : "partadm", "args" : "-a ANL-R01-M0-512"},
    {"tc_name" : "enable_partition_ANL_R01_M0_512"     , "command" : "partadm", "args" : "--enable ANL-R01-M0-512"},
    {"tc_name" : "activate_partition_ANL_R01_M0_512"   , "command" : "partadm", "args" : "--activate ANL-R01-M0-512"},
    {"tc_name" : "list_1"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "delete_default_que"                  , "command" : "cqadm"  , "args" : "--delq default"},
    {"tc_name" : "add_queues"                          , "command" : "cqadm"  , "args" : "--addq default q_1 q_2 q_3 q_4"},
    {"tc_name" : "start_default"                       , "command" : "cqadm"  , "args" : "--start default q_1 q_2 q_3 q_4"},
    {"tc_name" : "get_queues"                          , "command" : "cqadm"  , "args" : "--getq"},
    {"tc_name" : "qstat_1"                             , "command" : "qstat"  , "args" : "-Q"},
    {"tc_name" : "add_que_associations_1"              , "command" : "partadm", "args" : """--queue q_1:q_2:q_3:q_4 ANL-R00-R01-2048 ANL-R00-1024"""},
    {"tc_name" : "list_3"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "add_que_associations_2"              , "command" : "partadm", "args" : """--queue q_1:q_2:q_3:q_4 ANL-R01-1024 ANL-R00-M1-512"""},
    {"tc_name" : "list_4"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "add_que_associations_3"              , "command" : "partadm", "args" : """--queue default:q_1 ANL-R00-M0-512"""},
    {"tc_name" : "list_5"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "rmq_1"                               , "command" : "partadm", "args" : """--queue q_3 --rmq ANL-R00-R01-2048 ANL-R00-1024"""},
    {"tc_name" : "list_6"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "rmq_2"                               , "command" : "partadm", "args" : """--queue q_2 --rmq ANL-R00-R01-2048"""},
    {"tc_name" : "list_7"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "appq_1"                              , "command" : "partadm", "args" : """--queue q_3 --appq ANL-R00-R01-2048 ANL-R00-1024"""},
    {"tc_name" : "list_8"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "appq_2"                              , "command" : "partadm", "args" : """--queue q_2 --appq ANL-R00-R01-2048"""},
    {"tc_name" : "list_9"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "qstat_2"                             , "command" : "qstat"  , "args" : "-Q"},
    {"tc_name" : "setres_1"                            , "command" : "setres" , "args" : "-n george -s 2022_06_30-10:30 -d 50  -q q_1 ANL-R00-R01-2048"},
    {"tc_name" : "showres_1"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "setres_2"                            , "command" : "setres" , "args" : "-n george -m -d 300"},
    {"tc_name" : "showres_2"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "setres_3"                            , "command" : "setres" , "args" : "-n res_passed -s 2010_12_1-10:30 -d 50  -q q_1 ANL-R00-R01-2048"},
    {"tc_name" : "showres_3"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "qsub_1"                              , "command" : "qsub"   , "args" : "-h -t 50  -n 30 /bin/ls"},
    {"tc_name" : "qsub_2"                              , "command" : "qsub"   , "args" : "-h -t 100 -n 30 /bin/ls"},
    {"tc_name" : "qsub_3"                              , "command" : "qsub"   , "args" : "-h -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qsub_4"                              , "command" : "qsub"   , "args" : "--dep 1:2:3 -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qsub_5"                              , "command" : "qsub"   , "args" : "--dep 1:2:3:4:60 -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qstat_3"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qalter_1"                            , "command" : "qalter" , "args" : "--debug  -t +10 1 2 3 4 5"},
    {"tc_name" : "qstat_4"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qalter_2"                            , "command" : "qalter" , "args" : "--debug  -t -5 1 2 3 4 5"},
    {"tc_name" : "qstat_5"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qalter_3"                            , "command" : "qalter" , "args" : "--debug  -t +10 1 2 3 4 5"},
    {"tc_name" : "qstat_6"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qrls_1"                              , "command" : "qrls"   , "args" : "-d 1 2 3 4 5"},
    {"tc_name" : "qstat_7"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qrls_2"                              , "command" : "qrls"   , "args" : "-d --dep 4 5"},
    {"tc_name" : "qstat_8"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qsub_6"                              , "command" : "qsub"   , "args" : "--debug -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qsub_7"                              , "command" : "qsub"   , "args" : "--debug -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qstat_9"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qalter_4"                            , "command" : "qalter" , "args" : "--debug  --defer 6 7"},
    {"tc_name" : "qstat_10"                            , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "setres_4"                            , "command" : "setres" , "args" : "-n res1 -s 2032_12_1-10:30 -d 50  -q q_1 ANL-R00-R01-2048 ANL-R00-1024"},
    {"tc_name" : "setres_5"                            , "command" : "setres" , "args" : "-n res2 -s 2033_12_1-10:30 -d 50  -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "showres_4"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "releaseres_1"                        , "command" : "releaseres" , "args" : "-d res1 res2 george", },
    {"tc_name" : "setres_6"                            , "command" : "setres" , "args" : "-n r1 -u <USER> -s 2033_12_1-10:30 -d 50 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "setres_7"                            , "command" : "setres" , "args" : "-n r2 -u <USER> -s 2033_12_2-10:30 -d 50 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "setres_8"                            , "command" : "setres" , "args" : "-n rc1 -u <USER> -s 2033_12_3-10:30 -d 50 -c 72 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "setres_9"                            , "command" : "setres" , "args" : "-n rc2 -u <USER> -s 2033_12_4-10:30 -d 50 -c 72 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "showres_5"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "userres_1"                           , "command" : "userres", "args" : "r1 r2"},
    {"tc_name" : "userres_2"                           , "command" : "userres", "args" : "rc1 rc2"},
    {"tc_name" : "releaseres_2"                        , "command" : "releaseres" , "args" : "-d rc1 rc2", },
    {"tc_name" : "setres_10"                           , "command" : "setres" , "args" : "-n r1 -s 2033_12_1-10:30 -d 50 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "userres_3"                           , "command" : "userres", "args" : "r1 r2"},
    {"tc_name" : "showres_6"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "releaseres_3"                        , "command" : "releaseres" , "args" : "-d r1", },
    {"tc_name" : "showres_7"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "setres_11"                           , "command" : "setres" , "args" : "-n r1 -s now -d 50 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "releaseres_4"                        , "command" : "releaseres" , "args" : "-d r1", },
    ]
