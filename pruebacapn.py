import capnp
import payload_capnp

capnp.remove_import_hook()
payload_capnp = capnp.load('payload.capnp')


# payload.capnp
@0x934efea7f017fff0;


struct Payload {
  sent_timestamp @0 :UInt32;
  recv_timestamp @1 :UInt32;
  sequence_number @2 :UInt32;
  ack_number @3 :UInt32;
  sender_id @4 :int;

  const std::string str( const size_t len ) const;
  bool operator==( const Payload & other ) const;

  }


  struct SatPayload {
    sent_timestamp @0 :UInt32;
    recv_timestamp @1 :UInt32;
    sequence_number @2 :UInt32;
    ack_number @3 :UInt32;
    sender_id @4 :int;

    }


def operator( Payload, other ):
    return (Payload.sequence_number == other.sequence_number
	  && Payload.sent_timestamp == other.sent_timestamp
	  && Payload.recv_timestamp == other.recv_timestamp
	  && Payload.sender_id == other.sender_id)

#endif
