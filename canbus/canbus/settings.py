import socket
print(socket.gethostname())

if "skhan" in socket.gethostname():
    print "using development settings"
    from conf.dev import *
else:
    print "using production settings"
    from conf.prod import *