# swlt.protonvpn-availability

This is a python script for automatically pinging every server of ProtonVPN for checking if some ProtonVPN IPs are blocked within your network.

## What you need

You need to have pythonping installed. This can be done by:

```bash
pip install pythonping
```

## Usage

And now, just call your python3 interpreter and let the script do it's job.
Remember that pythonping needs root permissions to work.

```
cd protonvpnchecker/src
sudo python3 script.py
```

While running, you can always see the current process and which server has just been checked. This will look like that:

```
CH#10 is reachable: True remaining servers to test: 1176
CH#11 is reachable: False remaining servers to test: 1175
CH#12 is reachable: True remaining servers to test: 1174
```

After letting the script run (This takes around 10 minutes), you will get a list as a result like this:

```
Reachable servers:
CA#1
CA#2
...
Non-reachable servers:
US-VA#4
SE#2
...
```
