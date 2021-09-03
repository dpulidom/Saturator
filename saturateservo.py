const std::string _name;
  FILE* _log_file;

  const Socket _listen;
  const Socket _send;
  Socket::Address _remote;

  const bool _server;
  const int _send_id;

  Acker *_acker;

  uint64_t _next_transmission_time;

  static const int _transmission_interval = 1000 * 1000 * 1000;

  int _foreign_id;

  int _packets_sent, _max_ack_id;

  int _window;

  static const int LOWER_WINDOW = 20;
  static const int UPPER_WINDOW = 1500;

  static constexpr double LOWER_RTT = 0.75;
  static constexpr double UPPER_RTT = 3.0;

  class SaturateServo:
     def _init_(self, name,log_f,listen,send, remote, server, send_id):
         self.s_name= name
         self.log_file= log_f
         self.s_listen=listen
         self.s_send= send
         self.s_remote=remote
         self.s_server= server
         self.s_send_id=send_id
         _acker( NULL ),
         _next_transmission_time( Socket::timestamp() ),
         _foreign_id( -1 ),
         _packets_sent( 0 ),
         _max_ack_id( -1 ),
         _window( LOWER_WINDOW )


    def recv(self):

        Socket::Packet incoming( _listen.recv() );
        SatPayload *contents = (SatPayload *) incoming.payload.data();
        contents->recv_timestamp = incoming.timestamp;

      if contents.sequence_number != -1 :
        printf("MARTIAN!\n")
        return

      # possibly roam
      if _server :
        if _acker :
          if ( (contents->sender_id > _foreign_id) && (contents->ack_number == -1) ) {
    	_foreign_id = contents->sender_id;
    	_acker->set_remote( incoming.addr );
          }
        }
      }

      /* process the ack */
      if ( contents->sender_id != _send_id ) {
        /* not from us */
        return;
      } else {
        if ( contents->ack_number > _max_ack_id ) {
          _max_ack_id = contents->ack_number;
        }

        /*    printf( "%s pid=%d ACK RECEIVED senderid=%d seq=%d, send_time=%ld, recv_time=%ld\n",
    	  _name.c_str(), getpid(), contents->sender_id, contents->sequence_number, contents->sent_timestamp, contents->recv_timestamp ); */

        int64_t rtt_ns = contents->recv_timestamp - contents->sent_timestamp;
        double rtt = rtt_ns / 1.e9;

        fprintf( _log_file, "%s ACK RECEIVED senderid=%d, seq=%d, send_time=%ld,  recv_time=%ld, rtt=%.4f, %d => ",
           _name.c_str(),_server ? _foreign_id : contents->sender_id , contents->ack_number, contents->sent_timestamp, contents->recv_timestamp, (double)rtt,  _window );
        /* increase-decrease rules */

        if ( (rtt < LOWER_RTT) && (_window < UPPER_WINDOW) ) {
          _window++;
        }

        if ( (rtt > UPPER_RTT) && (_window > LOWER_WINDOW + 10) ) {
          _window -= 20;
        }

        fprintf( _log_file, "%d\n", _window );
      }
    }



  uint64_t wait_time( void ) const;

  void tick( void );

  void set_acker( Acker * const s_acker ) { _acker = s_acker; }

  void set_remote( const Socket::Address & s_remote ) { _remote = s_remote; }

  SaturateServo( const SaturateServo & ) = delete;
  const SaturateServo & operator=( const SaturateServo & ) = delete;
};
