#!/usr/bin/env python

#
# ** The MIT License **
#
# Copyright (c) 2013 Andrei Gherzan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

#
# Helper class to encrypt and decrypt text using AES from Crypto.Cipher
#
# Home: https://github.com/agherzan/notifmail
#
# Author: Andrei Gherzan <andrei@gherzan.ro>
#

try:
    import os, sys, stat
    from Crypto import Random
    from Crypto.Cipher import AES
    import base64
except Exception as e:
    print "ERROR : Can't import at least one module in notifmail_utils. Check README."
    print "ERROR :" , str(e)
    sys.exit(1)

class aesCryptor:
    BLOCK_SIZE = 32     # must be 16, 24, or 32 for AES
    PADDING = '*'       # use as charater to fill the string size requirements
    KEYFILEMODE = '600' # keyfile must have a strict permission

    def __init__ (self, keyfilepath):
        '''
        Constructor
        '''
        # Create or read Key
        keyfile = os.open(str(keyfilepath), os.O_RDWR | os.O_CREAT, 0600)
        # First of all make sure the keyfile has KEYFILEMODE mode
        if not stat.S_IMODE(os.stat(keyfilepath).st_mode) == int(self.KEYFILEMODE, 8):
            raise OSError("Keyfile %s does not the right permissions which is %s" 
                % (keyfilepath, self.KEYFILEMODE))
        os.lseek(keyfile, 0, 0)
        key = os.read(keyfile, os.stat(keyfilepath).st_size)
        if key:
            self.key = key
        else:
            self.key = os.urandom(self.BLOCK_SIZE)
            os.write(keyfile, self.key)
        os.close(keyfile)

        self.cipher = AES.new(self.key)

    def pad(self, s):
        '''
        Sufficiently pad the text to be encrypted
        '''
        return s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING

    def encode(self, cleartext):
        '''
        Encode text
        '''
        return base64.b64encode(self.cipher.encrypt(self.pad(cleartext)))

    def decode(self, codedtext):
        '''
        Decode text
        '''
        return self.cipher.decrypt(base64.b64decode(codedtext)).rstrip(self.PADDING)
