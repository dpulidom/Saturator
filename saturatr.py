import socket
import sys
import acker

SaturateServo( s_name, log_file, s_listen, s_send, s_remote,const s_server, s_send_id )






def main(argc, argv[] ):

	for i in argv:
		sys.stdout = stderr
		printf( "Usage: " + argv[ 0 ] + "[RELIABLE_IP RELIABLE_DEV TEST_IP TEST_DEV SERVER_IP]\n")

    	raise SystemExit


	data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #duda de como traducir esto a python
	feedback_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	if argc == 1: # /* server */
    	server = true
    	data_socket.bind( Socket::Address( "0.0.0.0", 9001 ) )
    	feedback_socket.bind( Socket::Address( "0.0.0.0", 9002 ) )
  	else :#/* client */
    	server = false

    reliable_ip = sys.argv[ 1 ]
    reliable_dev = sys.argv[ 2 ]

    test_ip = sys.argv[ 3 ]
    test_dev = sys.argv[ 4 ]

    server_ip = sys.argv[ 5 ]

	sender_id = (ts/1e9)

	data_socket.bind(test_ip, 9003)
	# data_socket.bind_to_device( test_dev ) No se traducirlo
	remote_data_address = [ server_ip, 9001 ]

	feedback_socket.bind( reliable_ip, 9004 )
	# feedback_socket.bind_to_device( reliable_dev )
	remote_feedback_address = [server_ip, 9002]




	  while True:
	    # flush(NULL)No se que hace

	     # possibly send packet
	    saturatr.tick()
	    acker.tick()

	     # wait for incoming packet OR expiry of timer
	    struct pollfd poll_fds[ 2 ]
	    poll_fds[ 0 ].fd = data_socket.get_sock()
	    poll_fds[ 0 ].events = POLLIN
	    poll_fds[ 1 ].fd = feedback_socket.get_sock()
	    poll_fds[ 1 ].events = POLLIN

	    struct timespec timeout
	    uint64_t next_transmission_delay = std::min( saturatr.wait_time(), acker.wait_time() )

	    if ( next_transmission_delay == 0 ) {
	      printf(  "ZERO %ld %ld\n", saturatr.wait_time(), acker.wait_time() )
	    }

	    timeout.tv_sec = next_transmission_delay / 1000000000
	    timeout.tv_nsec = next_transmission_delay % 1000000000
	    ppoll( poll_fds, 2, &timeout, NULL )

	    if poll_fds[ 0 ].revents & POLLIN:
	      acker.recv()


	    if poll_fds[ 1 ].revents & POLLIN:
	      saturatr.recv()
