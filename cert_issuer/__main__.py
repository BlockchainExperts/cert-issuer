#!/usr/bin/env python3

import os.path
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __package__ is None and not hasattr(sys, 'frozen'):
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))


def cert_issuer_main(args=None):
    from cert_issuer import config
    parsed_config = config.get_config()
    from cert_issuer import issue_certificates, trx_utils
    trx_utils.set_cost_constants(parsed_config.tx_fee, parsed_config.dust_threshold, parsed_config.satoshi_per_byte)
    issue_certificates.main(parsed_config)


def cert_signer_main(args=None):
    from cert_issuer import config
    parsed_config = config.get_config()
    from cert_issuer import sign_certificates
    sign_certificates.main(parsed_config)


if __name__ == '__main__':
    cert_issuer_main()
