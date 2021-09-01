
import sys
import acker.hh
#include "payload.hh"
#include "saturateservo.hh"

class Acker(s_name,log_file_handle, s_listen, s_send, s_remote, s_server, s_ack_id ):

    def __init__:
        _name= s_name
        _log_file=log_file_handle
        _listen= s_listen
        _send= s_send
        _remote= s_remote
        _server= s_server
        _ack_id= s_ack_id
        _saturatr= NULL
        _next_ping_time( Socket::timestamp() #buscar esto
        _foreign_id= -1

def recv( ):
{

# PRUEBA
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind((ip, port))
  data = sock.recv(8192)
######################################################################

  Socket::Packet incoming( _listen.recv() );
  SatPayload *contents = (SatPayload *) incoming.payload.data();
  contents.recv_timestamp = incoming.timestamp;
# esto trata de recibir el payload
  int64_t oneway_ns = contents->recv_timestamp - contents->sent_timestamp;
  double oneway = oneway_ns / 1.e9;

  if ( _server ) {
    if ( _saturatr ) {
      if ( contents.sender_id > _foreign_id ) {
	_foreign_id = contents.sender_id;
	_saturatr.set_remote( incoming.addr );
      }
    }

    if ( _remote == UNKNOWN ) {
      return;
    }
  }

  assert( !(_remote == UNKNOWN) );

  Socket::Address fb_destination( _remote );

  # send ack
  SatPayload outgoing( *contents ); #Mirar esto
  outgoing.sequence_number = -1;
  outgoing.ack_number = contents.sequence_number;
  _send.send( Socket::Packet( _remote, outgoing.str( sizeof( SatPayload ) ) ) );

  _log_file.write("%s DATA RECEIVED senderid=%d, seq=%d, send_time=%ld, recv_time=%ld, 1delay=%.4f \n",
     _name.c_str(),  _server ? contents.sender_id : _ack_id, contents.sequence_number, contents.sent_timestamp, contents.recv_timestamp,oneway)

   # printf( _log_file,"%s DATA RECEIVED senderid=%d, seq=%d, send_time=%ld, recv_time=%ld, 1delay=%.4f \n",
   #    _name.c_str(),  _server ? contents->sender_id : _ack_id, contents->sequence_number, contents->sent_timestamp, contents->recv_timestamp,oneway );
}

def tick():
{
  if ( _server ) {
    return;
  }


  if ( _remote == UNKNOWN ) {
    _next_ping_time = Socket::timestamp() + _ping_interval;
    return;
  }

  if ( _next_ping_time < Socket::timestamp() ) {
    SatPayload contents;
    contents.sequence_number = -1;
    contents.ack_number = -1;
    contents.sent_timestamp = Socket::timestamp();
    contents.recv_timestamp = 0;
    contents.sender_id = _ack_id;

    _send.send( Socket::Packet( _remote, contents.str( sizeof( SatPayload ) ) ) );

    _next_ping_time = Socket::timestamp() + _ping_interval;
  }
}

def wait_time( ):
{
  if _server :
    return 1000000000

  int diff = _next_ping_time - Socket.timestamp()
  if ( diff < 0 ) {
    diff = 0;
  }

  return diff;
}
