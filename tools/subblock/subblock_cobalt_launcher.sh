#!/bin/sh
#COBALT --disable_preboot
#COBALT --mode script
# Cobalt
# 
# 
# description: Cobalt resource manager/scheduler
#
# qsub --mode script --disable_preboot -t 8:00:00 -n 128 -A JCESR -q Q.JCESR --mode script ./subblock_setup.sh

umask 022

# Local site paths:
export MPIRUN_VERBOSE=0
export LD_LIBRARY_PATH=/bgsys/drivers/ppcfloor/lib64:$LD_LIBRARY_PATH
if [ -z "${FW_DIR}" ]; then
#	export FW_DIR=/projects/JCESR/fireworks
	if [ -z "${BASH_SOURCE[0]}" ]; then
		FW_DIR=$( cd $(dirname $0)/../ && pwd -P )
	else
		FW_DIR=$(cd $(dirname "${BASH_SOURCE[0]}")/../ && pwd -P)
	fi
fi

export PROJECTBASEDIR=/projects/JCESR/runs

# Paths based on site paths
export PATH=${FW_DIR}/bin:${PATH}
export LD_LIBRARY_PATH=${FW_DIR}/lib:${LD_LIBRARY_PATH}
export SC_RUNDIR=${PROJECTBASEDIR}/${USER}/${COBALT_JOBID}
export SC_CONFIGPATH=${SC_RUNDIR}/etc
export SC_CONFIGFILE="${SC_CONFIGPATH}/cobalt.conf"
export SC_DAEMON_PATH=${FW_DIR}/bin
export COBALT_CONFIG_FILES=${SC_CONFIGFILE}


#
mkdir -p ${SC_RUNDIR}/{log,etc,lock,state,run}
prefix=${FW_DIR}
exec_prefix=${FW_DIR}/bin


# choose semi-random open port
export COBALT_COMPONENTS="slp bgqsystem user_script_forker cqm bgsched system_script_forker bg_runjob_forker cdbwriter"
${FW_DIR}/bin/gen_config_file.py
${FW_DIR}/bin/gen_keys.sh


echo "Session starting, to use set COBALT_CONFIG_FILES=${SC_CONFIGFILE}"


# Starts the component specified as the first argument.
# Optional second argument used for extra arguments to 
# pass to the component.
start_component () {
    component=$1
    if [ -n $2 ] ; then
	component_args=$2
    else
	component_args=''
    fi
    pid=`pgrep -f "${component}.py $component_args --config-files ${SC_CONFIGFILE}"`
    echo -n "Starting ${component}: "
    if [ -z "$pid" ]
    then
        {
         date=`/bin/date`
         echo "--- $date: START ${component} ---" >>${SC_RUNDIR}/log/${component}.out
         "${SC_DAEMON_PATH}/${component}.py" $component_args --config-files "${SC_CONFIGFILE}" >>${SC_RUNDIR}/log/${component}.out 2>&1 &
         export LASTDAEMON="${LASTDAEMON} $!"
 	 }
        echo "done"
        return 0
    else
        echo "failed -- $component already running (pid $pid)"
        return 1
    fi
}

# Stops the component specified as the first argument.
stop_component () {
    component=$1
       echo -n "Stopping ${component}: "
	pkill -f ${SC_DAEMON_PATH}/${component}.py
        echo "done"
    return 0
}



for component in ${COBALT_COMPONENTS}; do

    if [ "$component" == "bgqsystem" ] ; then
    #	source ~bgqsysdb/sqllib/db2profile
    	sleep 1
    else
    	source ~db2cat/sqllib/db2profile
    fi

    start_component $component
 
    if [ "$component" == "slp" ] ; then
	sleep 30
    fi

done


touch ${SC_RUNDIR}/lock/cobalt

while [[ "$(slpstat | grep -q -e "^system\s"; echo $?)" -ne 0 ]] || [[ "$(slpstat | grep -q queue; echo $?)" -ne 0 ]] 
do
	sleep 1
done

echo "Adding partitions from: ${COBALT_PARTNAME}" >> ${SC_RUNDIR}/log/partition.log  2>&1
partadm.py -r -a ${COBALT_PARTNAME} >> ${SC_RUNDIR}/log/partition.log  2>&1
partadm.py --activate ${COBALT_PARTNAME} >> ${SC_RUNDIR}/log/partition.log  2>&1
partadm.py --enable ${COBALT_PARTNAME} >> ${SC_RUNDIR}/log/partition.log  2>&1
echo "Adding default queue" >> ${SC_RUNDIR}/log/partition.log  2>&1
cqadm.py --addq default >> ${SC_RUNDIR}/log/partition.log  2>&1
cqadm.py --startq default >> ${SC_RUNDIR}/log/partition.log  2>&1
echo "Readding subblocks of ${COBALT_PARTNAME}" >> ${SC_RUNDIR}/log/partition.log  2>&1
grep Creating ${SC_RUNDIR}/log/bgqsystem.out | awk '{print $6}' | sed 's/,//g' | xargs partadm.py -a >> ${SC_RUNDIR}/log/partition.log  2>&1
grep Creating ${SC_RUNDIR}/log/bgqsystem.out | awk '{print $6}' | sed 's/,//g' | xargs partadm.py --enable >> /dev/null 2>&1
grep Creating ${SC_RUNDIR}/log/bgqsystem.out | awk '{print $6}' | sed 's/,//g' | xargs partadm.py --activate >> /dev/null 2>&1
echo "Please set COBALT_CONFIG_FILES=${SC_CONFIGFILE}"

sleep $(( $COBALT_ENDTIME-$COBALT_STARTTIME )) &

wait

for component in ${COBALT_COMPONENTS}; do 
   stop_component $component
done
rm ${SC_RUNDIR}/lock/cobalt
