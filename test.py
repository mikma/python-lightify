#!/usr/bin/python
#
# Copyright 2014 Mikael Magnusson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import lightify
import sys

def main(argv):

    conn = lightify.Lightify(argv[1])

    conn.update_all_light_status()

    for (addr, light) in conn.lights().iteritems():
        print "%x %d %d %d %s %s" % (addr, light.on(), light.lum(), light.temp(), light.rgb(), light)

    sys.exit(0)

    groups = conn.group_list()

    for group in groups.iterkeys():
        lights = conn.group_info(group)
        print "Lights: %s" % lights

#        for light in lights:
#            conn.read_light_status(light)

    #conn.read_all_light_status(1)

    sys.exit(0)

#seq = seq + 1
#data = build_command(seq, 0x35, 2, "") #, struct.pack("<B", 0))
#print 'sending "%s"' % binascii.hexlify(data)
##, struct.pack(""))
#sock.sendall(data)
#recv(sock)
#sock.close()
#sys.exit(0)

    seq = seq + 1
#data = onoff(seq, 2, 0)
#data = build_temp(seq, 2, 2700)
    data = build_luminance(seq, 2, 85, 2)
#data = colour(seq, 2, 0, 0, 255, 1)
    print 'sending "%s"' % binascii.hexlify(data)
    sock.sendall(data)
    recv(sock)

    time.sleep(2)

    seq = seq + 1
#data = onoff(seq, 2, 0)
#data = build_temp(seq, 2, 2700)
    data = build_luminance(seq, 2, 65, 2)
#data = colour(seq, 2, 255, 0, 0, 10)
    print 'sending "%s"' % binascii.hexlify(data)
    sock.sendall(data)
    recv(sock)

    time.sleep(2)

    seq = seq + 1
#data = onoff(seq, 2, 1)
#data = build_temp(seq, 2, 6500)
    data = build_luminance(seq, 2, lum, 10)
#data = colour(seq, 2, 255, 255, 255, 1)
    print 'sending "%s"' % binascii.hexlify(data)
    sock.sendall(data)
    recv(sock)



    sock.close()
    sys.exit(0)


main(sys.argv)
