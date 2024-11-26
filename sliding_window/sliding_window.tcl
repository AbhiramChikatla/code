set ns [new Simulator]

 

#puts "Starting program..."

 

# Creating Output files

set namf [open stop_wait_protocol.nam w]

$ns namtrace-all $namf

 

set trf [open stop_wait_protocol.tr w]

$ns trace-all $trf

 

# Finishing procedures

proc finish {} {          

            global ns namf trf

            $ns flush-trace

            #puts "Saving namf and trf..."

            close $namf

            close $trf

            #puts "Opening Network animator..."

            exec nam stop_wait_protocol.nam &

            #puts "Closing program..."

            exit 0

}

 

# Creating nodes

set n0 [$ns node]

set n1 [$ns node]

 

# Setting links and setting queue size

$ns duplex-link $n0 $n1 0.2Mb 200ms DropTail

$ns duplex-link-op $n0 $n1 orient right

$ns queue-limit $n0 $n1 10

 

# Defining agents and setting src and dest

set tcp [new Agent/TCP]

set sink [new Agent/TCPSink]

$ns attach-agent $n0 $tcp

$ns attach-agent $n1 $sink

$ns connect $tcp $sink

 

# Creating FTP

set ftp [new Application/FTP]

$ftp attach-agent $tcp

 

# Stop and wait protocol

$tcp set window_ 1

$tcp set maxcwnd_ 1

 

# Use below 2 # for sliding window

#$tcp set windowInit_ 4

#$tcp set maxcwnd_ 4

 

# I dont know what these are.

$tcp set nam_tracevar_ true

$ns add-agent-trace $tcp tcp

$ns monitor-agent-trace $tcp

$tcp tracevar cwnd_

 

# Finishing and closing procedures

$ns at 0.1 "$ftp start"

$ns at 3.0 "$ns detach-agent $n0 $tcp"

$ns at 3.0 "$ns detach-agent $n1 $sink"

$ns at 3.5 "$ftp stop"

$ns at 5.0 "finish"

$ns run