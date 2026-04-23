#!/usr/bin/env python
#    This file is part of python-evtx.
#   Version v0.1.1
import Evtx.Evtx as evtx
import Evtx.Views as e_views


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Dump a binary EVTX file into XML.")
    parser.add_argument("evtx", type=str, help="Path to the Windows EVTX event log file")
    args = parser.parse_args()

    with evtx.Evtx(args.evtx) as log:
        print(e_views.XML_HEADER)
        print("<Events>")
        for record in log.records():
            print(record.xml())
        print("</Events>")


if __name__ == "__main__":
    main()
