## Return the current status of the Tennessee State Flag

[![Build Status](https://travis-ci.org/pconwell/tn-state-flag-status.svg?branch=master)](https://travis-ci.org/pconwell/tn-state-flag-status)

Checks the current status of the Tennessee State Flag and sends an email (sms) to a chosen email (phone number). To send to a phone number, find the email address associated with the phone's SMS. Typically it is something like <PHONENUMBER>@<carrier>.com.

## Usage

`$ python ./status.py --user <SMTP user> --password "<SMTP password>" --server <SMTP server> --from <from email address> --to <to email address>`
