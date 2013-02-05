This includes pygooglevoice from:
http://code.google.com/p/pygooglevoice/source/browse/?r=f8cd16dbdd6a981630e2dea527a87b0547ee7028
There is a modification to the accounts login url as noted by the issue tracker.
The license for that is in LICENSE.txt. It looks BSD-ish.

This uses Kivy which uses pygame and a bunch of other stuff. Kivy is awesome and
pretty easy to use. Check it out here: www.kivy.org

Anything that is my work is placed into the public domain. There is no warranty
suckers.

This is an extremely simple dialer that calls you back. I'm using it for my
stock Nexus 7 to call back my SIP number. (If someone knows of a way to do this
that doesn't involve rooting/flashing my tablet or using GrooveIP (which seems
to have awful call quality in my experience), please let me know.)

This uses Kivy which uses pygame and a bunch of other stuff. Kivy is awesome and

Caveat: The code is extremely simple, there is no error handling, and I'm not packaging
it as an apk as of yet. It uses an undocumented API and is liable to stop
working (or worse) at any point. 
If you want to run it, rename gvoice_config.py.example to
gvoice_config.py and edit it accordingly. Put this directory in /sdcard/kivy/phone
and search the Play store for Kivy Launcher. After you install that, you can
click on Google Voice Dialer and dial a number.

TODO: basically everything, but it's close to good enough for my needs

- add support for a basic contact list, maybe prioritizing favorites
- package this as a native app to avoid the kivy launcher song and dance
- config screen to put in credentials and select callback number
- some sort of integration with a sip client to let it automatically answer
without blanket auto-answering (do any sip clients for android do this?)
- get this working for my Nokia N9, which also lacks a good way of making free
phone calls

