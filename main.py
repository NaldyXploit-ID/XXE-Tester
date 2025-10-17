#!/usr/bin/env python3
import argparse, hashlib, base64
def main():
    p=argparse.ArgumentParser(); p.add_argument("action", choices=["encode","md5"]); p.add_argument("data"); args=p.parse_args()
    if args.action=="encode": print(base64.b64encode(args.data.encode()).decode())
    else: print(hashlib.md5(args.data.encode()).hexdigest())
if __name__=="__main__": main()
